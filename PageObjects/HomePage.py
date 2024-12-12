
"""
Homepage.py - Python Selenium Script to 
1. Verify and validate the GUVI URL and title.
2. Verify and validate the login button is visible and clickable.
3. Verify and validate the signup button is visible and clickable.
4. Verify and validate the signup page exists.
5. Verify and validate the user login with valid credentials.
6. Verify and validate the user login for invalid credentials.
7. Verify and validate the user logout.

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import the data and locator
from TestData.data import GuviData
from TestLocators.locators import GuviLocators

# GuviHomePage class to automate the Guvi webpage
class GuviHomePage:

    def __init__(self):
        """
        Initialize the WebDriver and set implicit wait time.
        """
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.implicitly_wait(10)

        except NoSuchDriverException as error:
            print(f"ERROR: Selenium Driver not found! {error}")
            self.driver = None

    def start(self):
        """
        Launch the GUVI homepage URL.
        """
        if not self.driver:
            print("ERROR: Driver initialization failed.")
            return False
        
        try:
            self.driver.maximize_window()
            self.driver.get(GuviData.guvi_homepage_url)
            return True
        
        except TimeoutException as error:
            print(f"ERROR: Timeout occurred while loading the page! {error}")
            return False

    def fetch_title(self):
        """
        Fetch the title of the GUVI homepage.
        """
        try:
            if self.start():
                return self.driver.title
            else:
                return None
            
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(f"ERROR: Unable to fetch GUVI title! {error}")
            return None

    def fetch_url(self):
        """
        Fetch the current URL of the GUVI homepage.
        """
        try:
            if self.start():
                return self.driver.current_url
            else:
                return None
            
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException) as error:
            print(f"ERROR: Unable to fetch GUVI URL! {error}")
            return None
        
    def is_login_button_visible(self):
        """
        Check if the login button is visible on the homepage.
        """
        try:
            # Locate the login button
            login_button = self.driver.find_element(by=By.ID, value=GuviLocators().login_button_locator)
            if login_button.is_displayed():
                return True
            else:
                print("ERROR: Login button is not visible!")
                return False

        except NoSuchElementException as error:
            print(f"ERROR: Login button not found! {error}")
            return False

    def is_login_button_clickable(self):
        """
        Check if the login button is clickable.
        """
        try:
            # Locate the login button
            login_button = self.driver.find_element(by=By.ID, value=GuviLocators().login_button_locator)
            # click the login button 
            login_button.click()
            return True

        except ElementClickInterceptedException as error:
            print(f"ERROR: Login button is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: Login button not found! {error}")
            return False

    def is_signup_button_visible(self):
        """
        Check if the signup button is visible on the homepage.
        """
        try:
            # Locate the signup button
            signup_button = self.driver.find_element(by=By.XPATH, value=GuviLocators().signup_button_locator)
            if signup_button.is_displayed():
                return True
            else:
                print("ERROR: Sign up button is not visible!")
                return False

        except NoSuchElementException as error:
            print(f"ERROR: Sign up button not found! {error}")
            return False

    def is_signup_button_clickable(self):
        """
        Check if the signup button is clickable.
        """
        try:
            # Locate the signup button
            signup_button = self.driver.find_element(by=By.XPATH, value=GuviLocators().signup_button_locator)
            # Click the signup button
            signup_button.click()
            return True

        except ElementClickInterceptedException as error:
            print(f"ERROR: Sign up button is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: Sign up button not found! {error}")
            return False

    def navigate_to_signup_page(self):
        """
        Navigate to the signup page and verify the URL.
        """
        try:
            # Locate the login button and signup link
            self.driver.find_element(by=By.ID, value=GuviLocators().login_button_locator).click()
            self.driver.find_element(by=By.XPATH, value=GuviLocators().signup_link_locator).click()
            return self.driver.current_url == GuviData.signup_page_url

        except ElementClickInterceptedException as error:
            print(f"ERROR: Sign up link is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: Sign up link not found! {error}")
            return False

    def user_login(self):
        """
        Perform user login with valid credentials.
        """
        try:
            # Click Login menu
            self.driver.find_element(By.ID, GuviLocators().login_button_locator).click()

            # Enter valid email
            self.driver.find_element(By.ID, GuviLocators().email_locator).send_keys(GuviData().email)

            # Enter valid password
            self.driver.find_element(By.ID, GuviLocators().password_locator).send_keys(GuviData().password)

            # Click on Logged in checkbox
            self.driver.find_element(By.ID, GuviLocators().logged_in_checkbox_locator).click()

            # Click Login button
            self.driver.find_element(By.ID, GuviLocators().login_button_locator).click()

            # Validate successful login
            geecoin_icon = self.driver.find_element(By.XPATH, GuviLocators().geecoin_icon_locator)
            if geecoin_icon.is_displayed():
                return True
            else:
                print("Login failed!")
                return False
        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            print(error)
            return False

    def invalid_email_login(self):
        """
        Perform login with an invalid email and validate the error message.
        """
        try:
            # Click Login menu
            self.driver.find_element(By.ID, GuviLocators().login_button_locator).click()

            # Enter invalid email
            self.driver.find_element(By.ID, GuviLocators().email_locator).send_keys(GuviData().invalid_email)

            # Enter valid password
            self.driver.find_element(By.ID, GuviLocators().password_locator).send_keys(GuviData().password)

            # Click on Logged in checkbox
            self.driver.find_element(By.ID, GuviLocators().logged_in_checkbox_locator).click()

            # Click Login button
            self.driver.find_element(By.ID, GuviLocators().login_button_locator).click()

            # Wait for error message to be visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, GuviLocators().login_error_text_locator)))

            # Validate error message
            login_error_message = self.driver.find_element(By.XPATH, GuviLocators().login_error_text_locator).text

            if "Incorrect Email or Password" in login_error_message:
                return True
            else:
                print("Unexpected behavior: No error message displayed.")
                return False

        except Exception as error:
            print(f"Exception encountered: {error}")
            return False

    def invalid_password_login(self):
        """
        Perform login with an invalid password and validate the error message.
        """
        try:
            # Click Login menu
            self.driver.find_element(By.ID, GuviLocators().login_button_locator).click()

            # Enter valid email
            self.driver.find_element(By.ID, GuviLocators().email_locator).send_keys(GuviData().email)

            # Enter invalid password
            self.driver.find_element(By.ID, GuviLocators().password_locator).send_keys(GuviData().invalid_password)

            # Click on Logged in checkbox
            self.driver.find_element(By.ID, GuviLocators().logged_in_checkbox_locator).click()

            # Click Login button
            self.driver.find_element(By.ID, GuviLocators().login_button_locator).click()

            # Wait for error message to be visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, GuviLocators().login_error_text_locator)))

            # Validate error message
            login_error_message = self.driver.find_element(by=By.XPATH, value=GuviLocators().login_error_text_locator).text

            if "Incorrect Email or Password" in login_error_message:
                return True
            else:
                print("Unexpected behavior: No error message displayed.")
                return False
            
        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            print(error)
            return False

    def logout(self):
        """
        Perform user logout and validate the process.
        """
        try:
            # Ensure the user is logged in before attempting to logout
            if not self.user_login():
                print("Cannot logout because login failed.")
                return False

            # Click on account dropdown
            self.driver.find_element(By.XPATH, GuviLocators().account_dropdown).click()

            # Click on sign out button
            self.driver.find_element(By.ID, GuviLocators().signout_button_locator).click()

            # Validate successful logout by checking for the login menu button presence on homepage
            login_menu = self.driver.find_element(By.ID, GuviLocators().login_button_locator)
            if login_menu.is_displayed():
                return True
            else:
                print("Logout failed!")
                return False
        except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as error:
            print(error)
            return False

    def shutdown(self):
        """
        Close the browser and cleanup resources.
        """
        self.driver.quit()
