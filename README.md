# Mini Project - 1

This project implements a Page Object Model (POM) structure for automated testing of the [GUVI](https://www.guvi.in).

Website Link: https://www.guvi.in/


## Test Objective:

The objective of this project is to implement an automated testing framework for the [GUVI](https://www.guvi.in) web application using Python Selenium. The primary goals are to:

- **Validate Functionalities:** Ensure the core functionalities of the GUVI platform (such as navigation, login, and sign-up processes) work as expected.
- **Improve Test Maintenance:** Utilize a structured approach to separate web page interaction logic from test scripts, making it easier to maintain and extend as the application evolves.
- **Enhance Test Reusability:** Promote reusability of code for interactions with page elements, reducing duplication across test scripts.
- **Support Data-Driven Testing:** Leverage test data (stored in TestData/data.py) to run multiple test scenarios with different input sets to verify robustness and edge case handling.
- **Increase Test Coverage:** Automate critical paths such as user authentication, button functionality, and error handling to ensure high test coverage across essential user flows.
- **Ensure Browser Compatibility:** Run tests across multiple browsers (e.g., Chrome, Firefox, Edge, Safari) to validate cross-browser compatibility and identify potential issues.
- **Enable Continuous Testing:** Integrate with continuous integration (CI) tools to run tests automatically, ensuring that new changes do not introduce regressions or break existing functionality.

By achieving these objectives, this project aims to create a robust, maintainable, and scalable test automation framework for the GUVI platform.


## Test Suite:

### Test-Case-1:
1. Validate whether the URL `https://www.guvi.in` is accessible.

### Test-Case-2:
1. Verify whether the title of the webpage is `Guvi | Learn to code in your native language`.

### Test-Case-3:
1. Check whether the **Login** button is visible.
2. Verify whether the **Login** button is clickable.

### Test-Case-4:
1. Check whether the **Sign-Up** button is visible.
2. Verify whether the **Sign-Up** button is clickable.

### Test-Case-5:
1. Click on the **Sign-Up** button and navigate to the URL `https://www.guvi.in/sign-in/` to confirm the page exists.

### Test-Case-6:
1. Log in to your Guvi account using valid email and password credentials to verify successful login.
2. Log out from your Guvi account and verify the operation.

### Test-Case-7:
1. Attempt to log in to your Guvi account using invalid email and password credentials and capture the error message.


## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [License](#license)


## Features

- **Page Object Model (POM):** Separation of test logic and UI interactions. Each web page has its own corresponding class that defines methods for interacting with the elements on that page.
- **Pytest Framework:** Used to manage test cases, execute tests, and generate detailed reports.
- **Reusable Components:** Common actions like login, navigating to sections, and performing shutdown operations are encapsulated in reusable methods, improving maintainability.
- **Cross-Platform Compatibility:** The framework can be run across different environments, supporting different operating systems and web browsers.
- **Automation and Reporting:** Automation of repetitive tests with detailed reports on test results, making it easier to monitor and debug test executions.


## Tech Stack

- **Programming Language**: Python
- **Test Framework**: pytest
- **Automation Tool**: Selenium WebDriver
- **Reporting**: pytest-html
- **Browser Compatibility**: Microsoft Edge, Google Chrome, Mozilla Firefox, Safari
- **CI/CD Integration**: GitHub Actions


## Setup and Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/imranc07/Mini_Project_1.git
   cd Mini_Project_1
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory to store sensitive information such as login credentials and URLs. Example:
     ```
     BASE_URL=https://example.com
     USER_EMAIL=test@example.com
     USER_PASSWORD=yourpassword
     ```

## Running Tests

To execute tests, use the following commands:

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Generate HTML Report**:
   ```bash
   pytest --html=Reports/test_report.html
   ```

3. **Run Tests by Marker** (e.g., only "login" tests):
   ```bash
   pytest TestScripts/test_HomePage.py::test_guvi_url
   ```

4. **Headless Browser Execution**:
   - You can set up tests to run in Headless mode directly in your test script.

---

## Project Structure:
```
Mini_Project_1/
│
├── PageObjects/             # Contains Page Object Models GUVI Web applications
│   ├── HomePage.py          # Handles methods and elements
│
├── Reports/                 # Contains HTML reports
│   ├── test_report.html     # HTML reports generated by pytest
│   
├── TestData/                # Stores test data for the test cases
│   ├── data.py              # Contains reusable test data
│
├── TestLocators/            # Stores locators for web elements
│   ├── locators.py          # Contains locators for all web elements used in the tests
│
├── TestScripts/             # Contains all test cases
│   ├── test_HomePage.py     # Test cases for GUVI Web application
│
├── requirements.txt         # Lists project dependencies
│
└── README.md                # Project documentation
```

---

## License
This project is open-source and available under the **"MIT License"**.

    ```
    Feel free to adjust the content based on your specific project setup!
    ```