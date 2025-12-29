from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_assignments_from_moodle(username, password):
    # ===== Chrome configuration (CRITICAL FOR MOODLE) =====
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")

    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)

    try:
        # ===== Open Moodle login =====
        driver.get("https://moodle.ruppin.ac.il/login/index.php")

        wait.until(EC.presence_of_element_located((By.ID, "username")))

        # ===== Login =====
        driver.find_element(By.ID, "username").send_keys(username)
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # ===== Wait for page load =====
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # ===== Check login success =====
        time.sleep(2)
        current_url = driver.current_url
        login_ok = "login" not in current_url

        print("Current URL after login:", current_url)
        print("Login OK:", login_ok)

        # ===== Get user name =====
        try:
            header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "h2")))
            full_greeting = header.text.strip()
            name = (
                full_greeting.replace("שלום", "")
                .replace("!", "")
                .strip()
                .split()[0]
            )
        except:
            name = "משתמש"

        assignments = []

        # ===== Get assignments =====
        event_items = driver.find_elements(
            By.CSS_SELECTOR, 'div[data-region="event-list-item"]'
        )

        for item in event_items:
            try:
                # Title + link
                title_element = item.find_element(
                    By.CSS_SELECTOR, ".event-name-container a"
                )
                title = title_element.text.strip()
                link = title_element.get_attribute("href")

                # Course
                course = "לא ידוע"
                small_elements = item.find_elements(By.TAG_NAME, "small")
                for el in small_elements:
                    text = el.text.strip()
                    if "·" in text:
                        course = text.split("·")[-1].strip()
                        break

                # Due time
                try:
                    time_element = item.find_element(
                        By.CSS_SELECTOR,
                        "small.text-end.text-nowrap.align-self-center.ms-1",
                    )
                    due_time = time_element.text.strip()
                except:
                    due_time = None

                # Due date
                try:
                    date_elements = item.find_elements(
                        By.XPATH,
                        "./preceding::h5[contains(@class, 'font-weight-bold')]",
                    )
                    due_date = (
                        date_elements[-1].text.strip()
                        if date_elements
                        else None
                    )
                except:
                    due_date = None

                assignments.append(
                    {
                        "title": title,
                        "course": course,
                        "due_date": due_date,
                        "due_time": due_time,
                        "link": link,
                        "name": name,
                    }
                )

            except Exception as e:
                print("⚠️ Error parsing assignment:", e)

        return {
            "name": name,
            "assignments": assignments,
            "login_ok": login_ok,
        }

    finally:
        driver.quit()
