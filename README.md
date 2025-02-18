# Q-Sports Club Management System Test Framework

This project contains automated e2e tests for the Q-Sports Club Management System.

# Stack
* Python
* Selenium
* Pytest


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

# Configuration

By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "/data/config.yaml" file

# Results

To check the report, open the '/results/report.html' file once the execution has finished.

# Troubleshoot