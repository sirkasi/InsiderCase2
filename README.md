# InsiderCase2
Ahmet Kasidecioglu QA Engineer Selenium Task 2

# Project Documentation

## Overview

This project implements a comprehensive test automation suite for both UI and API functionalities related to the [Insider](https://useinsider.com/) careers website and the Petstore API.

**Key Components:**
- **UI Tests:**  
  - Validate that navigating through the Insider careers page works as intended.
  - Perform end-to-end checks such as selecting filters (location and department), confirming that job listings are filtered correctly, and verifying job details.
  - Check “View Role” redirections and ensure that expected content is displayed.
- **Load Tests (Locust):**  
  - Evaluate the performance and response times of certain functionalities like searching on n11.com.
  - Ensure the application handles concurrent requests gracefully.
- **API Tests (Petstore):**  
  - Validate the correctness of CRUD operations on the Petstore `/pet` endpoint.
  - Include both positive and negative scenarios to ensure robust error handling and compliance with API specifications.

## Prerequisites

- **Python 3.7+**
- **pip** (Python package manager)
- **WebDrivers:**
  - **ChromeDriver** for Chrome  
  - **GeckoDriver** for Firefox  
- **Selenium:**
  ```bash
  pip install selenium
- **pytest & pytest plugins:**
  ```bash
  pip install pytest pytest-repeat
- **requests (for API tests):**
  ```bash
  pip install requests
- **Locust (for load testing):**
  ```bash
  pip install locust

## Project Structure

```bash
project/
├─ pages/
│  ├─ base_page.py
│  ├─ home_page.py
│  ├─ careers_page.py
│  ├─ qa_jobs_page.py
│  └─ job_details_page.py
├─ tests/
│  ├─ web/
│  │  ├─ test_careers_page.py
│  │  └─ __init__.py
│  ├─ api/
│  │  ├─ test_pet_api.py
│  │  └─ __init__.py
│  ├─ conftest.py
│  └─ __init__.py
├─ locustfile.py
```

## Configuration
- conftest.py defines fixtures for:
  - Browser initialization (Chrome, Firefox)
  - Parameterization via --browser=chrome or --browser=firefox
  - Screenshot on failure
  - Cookie acceptance
 
## Running Tests
- UI Tests
  Run UI tests on Chrome:
```bash
pytest tests
```
- Run UI tests on Firefox:
```bash
pytest tests --browser=firefox  
```
- Repeat Tests N times (e.g., 10 times) to check stability:
```bash
pytest --count=10 tests/test_careers_page.py::test_insider_careers_page    
```

- API Tests
  Run All API Tests:
```bash
pytest -k api
```








