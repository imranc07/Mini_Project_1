"""
test_homepage.py - Python selenium scripts for executing tests cases to
1. Verify and validate the GUVI URL and title.
2. Verify and validate the login button is visible and clickable.
3. Verify and validate the signup button is visible and clickable.
4. Verify and validate the signup page exists.
5. Verify and validate the user login with valid credentials.
6. Verify and validate the user login for invalid credentials.
7. Verify and validate the user logout.

"""

# import GuviHomePage and the data
from PageObjects.HomePage import GuviHomePage
from TestData.data import GuviData


def test_guvi_url():
    """
    Test case to verify the URL of the GUVI homepage.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.fetch_url() == GuviData.guvi_homepage_url
        print("SUCCESS: GUVI URL VERIFIED")
    finally:
        homepage.shutdown()

def test_negative_url():
    """
    Test case to verify the URL is not the incorrect (negative) one.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.fetch_url() != GuviData.guvi_negative_url
        print("SUCCESS: GUVI NEGATIVE URL VERIFIED")
    finally:
        homepage.shutdown()

def test_guvi_title():
    """
    Test case to verify the title of the GUVI webpage.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.fetch_title() == GuviData.guvi_page_title
        print("SUCCESS: GUVI WEBPAGE TITLE VERIFIED")
    finally:
        homepage.shutdown()

def test_negative_title():
    """
    Test case to verify the title is not the incorrect (negative) one.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.fetch_title() != GuviData.guvi_negative_title
        print("SUCCESS: GUVI WEBPAGE NEGATIVE TITLE VERIFIED")
    finally:
        homepage.shutdown()

def test_login_button_visible():
    """
    Test case to verify if the login button is visible on the homepage.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.is_login_button_visible()
        print("SUCCESS: LOGIN BUTTON IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_login_button_clickable():
    """
    Test case to verify if the login button is clickable.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.is_login_button_clickable()
        print("SUCCESS: LOGIN BUTTON IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_signup_button_visible():
    """
    Test case to verify if the signup button is visible on the homepage.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.is_signup_button_visible()
        print("SUCCESS: SIGNUP BUTTON IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_signup_button_clickable():
    """
    Test case to verify if the signup button is clickable.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.is_signup_button_clickable()
        print("SUCCESS: SIGNUP BUTTON IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_signup_page_navigation():
    """
    Test case Navigate to the signup page and verify the URL.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.navigate_to_signup_page()
        print("SUCCESS: SIGNUP PAGE AND URL VERIFIED.")
    finally:
        homepage.shutdown()

def test_user_login():
    """
    Positive test case to verify user login with valid credentials.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.user_login()
        print("SUCCESS: LOGGED IN.")
    finally:
        homepage.shutdown()

def test_logout():
    """
    Test case to verify user logout functionality.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.logout()
        print("SUCCESS: LOGGED OUT.")
    finally:
        homepage.shutdown()

def test_invalid_email_login():
    """
    Negative test case to verify user login with an invalid email.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.invalid_email_login() 
        print("SUCCESS: ERROR MESSAGE DISPLAYED FOR INVALID EMAIL AS EXPECTED.")
    finally:
        homepage.shutdown()

def test_invalid_password_login():
    """
    Negative test case to verify user login with an invalid password.
    """
    homepage = GuviHomePage()
    homepage.start()
    try:
        assert homepage.invalid_password_login()
        print("SUCCESS: ERROR MESSAGE DISPLAYED FOR INVALID PASSWORD AS EXPECTED.")
    finally:
        homepage.shutdown()
