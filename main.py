from fastapi import FastAPI
from moodle_scraper import get_assignments_from_moodle
from models import LoginRequest
from database import save_user_to_db, save_assignments
import traceback

app = FastAPI()

print("main.py loaded and endpoints are being registered")


#  LOGIN
@app.post("/login", tags=["Auth"])
def login(request: LoginRequest):
    try:
        result = get_assignments_from_moodle(request.username, request.password)

        if result.get("login_ok"):
            # Save/update user in database
            save_user_to_db(
                username=request.username,
                password=request.password,
                name=result.get("name")
            )

            # Save assignments to database
            assignments = result.get("assignments", [])
            save_assignments(request.username, assignments)

            return {
                "success": True,
                "name": result.get("name"),
                "message": "Login successful"
            }
        else:
            return {
                "success": False,
                "error": "Login failed"
            }

    except Exception as e:
        traceback.print_exc()
        return {
            "success": False,
            "error": f"Exception during login: {str(e)}"
        }


#  PENDING ASSIGNMENTS
@app.post("/pending_assignments", tags=["Assignments"])
def pending_assignments_post(request: LoginRequest):
    try:
        result = get_assignments_from_moodle(request.username, request.password)

        if result.get("login_ok"):
            # Save/update user in database
            save_user_to_db(
                username=request.username,
                password=request.password,
                name=result.get("name")
            )

            # Save assignments to database
            assignments = result.get("assignments", [])
            save_assignments(request.username, assignments)

        return result
    except Exception as e:
        traceback.print_exc()
        return {"error": f"Exception fetching assignments (POST): {str(e)}"}
