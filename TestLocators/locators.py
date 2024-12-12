"""
locators.py contains all the web element locators such as XPATH, ID, class name, and link text, 
used to interact with elements on the GUVI webpage.
"""

class GuviLocators:
    
    # Locator for the login button (by ID)
    login_button_locator = 'login-btn'  
    
    # Locator for the signup button (by XPATH)
    signup_button_locator = '//a[contains(text(), "Sign up")]'  
    
    # Locator for the signup link within the login page (by XPATH)
    signup_link_locator = '//a[contains(text(), "Signup")]'  
    
    # Locator for the Geekoin icon after successful login (by XPATH)
    geecoin_icon_locator = '//i[contains(text(), "Geekoin:")]'  
    
    # Locator for the email input field (by ID)
    email_locator = 'email'  
    
    # Locator for the password input field (by ID)
    password_locator = 'password'  
    
    # Locator for the "Remember me" checkbox (by ID)
    logged_in_checkbox_locator = 'logged-in'  
    
    # Locator for the account dropdown menu (by XPATH)
    account_dropdown = '//button[@class="btn dropdown account-box-toggler"]'  
    
    # Locator for the signout button in the account dropdown (by ID)
    signout_button_locator = 'signout'  
    
    # Locator for the error message displayed during login failure (by XPATH)
    login_error_text_locator = '//div[@class="invalid-feedback is-invalid"]'