# Q-Sports Club Management System Test Framework

This project contains automated e2e tests for the Q-Sports Club Management System.

## Stack
* Python
* Selenium
* Pytest

## Solution
The automation solution uses the Page-Object model, having separate files per module, for this sample it only contains 2 modules, login and category, each with locators, a page file, and a test file.


# Requirements
* Python 3.12.3
* pip (24.0)

# Instalation
1. Clone this repository
2. Open a terminal
3. Go to the project root directory "/sports-club-mgmt-sys-test".
4. Create a virtual environment: 
   -`python3 -m venv venv`
5. Activate the virtual environment: 
   - `. venv/bin/activate`
6. Download libraries:  `pip install -r requirements.txt`
 
# Execute Tests

1. Open a terminal
2. From the project root directory run: `TEST_PASSWORD=<login_password>  TEST_USERNAME=<login_username> pytest -v --html=results/report.html`

e.g:

`TEST_PASSWORD=password  TEST_USERNAME=user@mail.com pytest -v --html=results/report.html`

It should run 4 tests and the output should look like this:

```bash
tests/test_category.py::TestCategory::test_new_category PASSED                                                                                                                               [ 25%]
tests/test_category.py::TestCategory::test_new_sub_category PASSED                                                                                                                           [ 50%]
tests/test_login.py::TestLogin::test_title PASSED                                                                                                                                            [ 75%]
tests/test_login.py::TestLogin::test_login PASSED                                                                                                                                            [100%]
```

# Configuration
By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "/data/config.yaml" file

# Results
To check the report, open the '/results/report.html' file once the execution has finished.

## Future Enhancements
* Have a default .env file with the application credentials and URLs, this can be encrypted for better security
* The Data can be validated through API to confirm data creation 
* Add a headless mode to run the tests faster or in a automated pipeline
* Reporting can be enhanced using the Allure library

#### By: Freddy Ayala