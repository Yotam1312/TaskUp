from sqlalchemy import create_engine, text
import urllib.parse
from security import encrypt_password

# --- Connection Settings ---
SERVER = 'DESKTOP-I4G1A5P'
DATABASE = 'TaskUP_DB'

# Create connection string
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes;"
)

# Create engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


def save_user_to_db(username: str, password: str, name: str | None = None):
    """
    Save or update user in database.
    If user exists -> update password and name.
    If new user -> create in table.
    """
    encrypted_pass = encrypt_password(password)

    query = text("""
    IF EXISTS (SELECT 1 FROM Users WHERE Username = :username)
        UPDATE Users
        SET Password = :password, Name = :name, LastUpdated = GETDATE()
        WHERE Username = :username
    ELSE
        INSERT INTO Users (Username, Password, Name)
        VALUES (:username, :password, :name)
    """)

    try:
        with engine.connect() as conn:
            conn.execute(query, {
                "username": username,
                "password": encrypted_pass,
                "name": name
            })
            conn.commit()
            print(f"User '{username}' saved/updated successfully.")
    except Exception as e:
        print(f"Error saving user to DB: {e}")


def get_all_users():
    """
    Get all users from database.
    Used by scheduler to check assignments for each user.
    """
    query = text("SELECT Username, Password FROM Users")
    users_list = []

    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            for row in result:
                users_list.append({
                    "username": row.Username,
                    "password": row.Password
                })
    except Exception as e:
        print(f"Error fetching users: {e}")

    return users_list


def save_assignments(username: str, assignments_list: list):
    """
    Save assignments for a user.
    Prevents duplicates by checking Link.
    """
    if not assignments_list:
        return

    query = text("""
    DECLARE @UserId INT = (SELECT Id FROM Users WHERE Username = :username);

    IF @UserId IS NOT NULL
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM Assignments WHERE Link = :link AND UserId = @UserId)
        BEGIN
            INSERT INTO Assignments (UserId, Title, Course, DueDate, DueTime, Link)
            VALUES (@UserId, :title, :course, :date, :time, :link)
        END
    END
    """)

    saved_count = 0
    try:
        with engine.connect() as conn:
            for task in assignments_list:
                conn.execute(query, {
                    "username": username,
                    "title": task.get('title'),
                    "course": task.get('course'),
                    "date": task.get('due_date'),
                    "time": task.get('due_time'),
                    "link": task.get('link')
                })
                saved_count += 1
            conn.commit()
            print(f"Processed {saved_count} assignments for {username}.")

    except Exception as e:
        print(f"Error saving assignments: {e}")
