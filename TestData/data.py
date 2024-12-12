"""
data.py contains all the test data used for validating the GUVI website functionality.
"""

class GuviData:

    # URLs for testing
    guvi_homepage_url = "https://www.guvi.in/"  # GUVI homepage URL
    guvi_negative_url = "http://www.google.com"  # Incorrect/negative URL for testing
    
    # Titles for testing
    guvi_page_title = "GUVI | Learn to code in your native language"  # Expected GUVI homepage title
    guvi_negative_title = "native language"  # Partial/incorrect title for negative testing
    
    # Signup page URL for validation
    signup_page_url = 'https://www.guvi.in/register/'  
    
    # Test credentials for login functionality
    email = 'imranahmad_ah@rediffmail.com'  # Valid email address
    password = 'Guvi#1799'  # Valid password
    
    # Invalid credentials for negative testing
    invalid_password = 'Kbc@com1'  # Invalid password for testing
    invalid_email = 'kbc@kbc.com'  # Invalid email for testing
