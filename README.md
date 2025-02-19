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
7. If needed, install the Faker Library: `pip install Faker`

 
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

![](output.gif)

## Future Automation Enhancements
* Have a default .env file with the application credentials and URLs, this can be encrypted for better security
* The Data can be validated through API to confirm data creation 
* Add a headless mode to run the tests faster or in a automated pipeline
* Reporting can be enhanced using the Allure library

# Exploratory Testing Results (Exercise 1)
### UX Issues
* Responsive mode hides the main menu, and it shows profile options, the profile Options are hardcoded
* Side Menu can be collapsible
* On the Dashboard screen, the chart of total contributions is overflowing the panel

### UI Issues
* On the Report screen, the Exporting button does not work, action throws an API error:
```bash
'500 Internal server Error ->    
 "detail": "Handler dispatch failed; nested exception is java.lang.NoClassDefFoundError: Could not initialize class sun.awt.X11FontManager",'
```
* All the forms does not have any constraints, it's necessary to add character limit, also to accept only numbers or decimals for PAYMENTS.
* When the user tries to save a payment with a string, the application throws the following error:

```bash
"detail": "JSON parse error: Cannot deserialize value of type `java.math.BigDecimal` 
from String \"cnadjncdancjad\": not a valid representation; 
nested exception is com.fasterxml.jackson.databind.exc.InvalidFormatException: Cannot deserialize value of type `java.math.BigDecimal` from String \"cnadjncdancjad\": not a valid representation\n at [Source: (PushbackInputStream); line: 1, column: 41] (through reference chain: uy.com.club.administration.dto.request.ContributionSuggestedDTO[\"amount\"])",
```
* When the length of a category/sub category/ members and all the name inputs exceeds 300 characters, the 3 dots menu is not visible and the record it cannot be modified or deleted
* When adding Inactive members and partners, They are not displayed in the table, they cannot be modified and deleted
* In all the forms, whenever the user adds a new record, it is being added at the end of the table, and pages, causing the user to make more calls to the API, harming the performance of the application, a simple solution could be to sort the lists from recent records to old records
* On the partners screen, the View Details 3 dots menu option does not work

# Suggestions (Exercise 2)
* Add constraints to all the inputs on each of the forms, reason: the errors on API calls for these forms will be reduced due previous validation, and the application data will be more accurate
* Order the tables lists from resents records to old records, reason: it will reduce the number of API calls when clicking pagination to find the new records created, improving the application performance
* The tables filters and sorting can be added to the columns, reason: it improves the user experience, having those actions as a web application standards
#### By: Freddy Ayala