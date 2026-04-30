# QA Automation Framework — Python + Selenium + Pytest

A production-grade test automation framework built with **Python, Selenium WebDriver, Pytest, and BDD (Behave)**, demonstrating senior SDET practices including the Page Object Model, data-driven testing, API + UI integration, CI/CD pipeline integration, and HTML reporting.

**Author:** Akanksha Singh
**Role:** Senior QA Engineer / SDET
**Application Under Test:** [SauceDemo](https://www.saucedemo.com/) (public demo e-commerce site)

---

## 🏗️ Architecture Overview

```
qa-automation-framework/
│
├── config/
│   └── config.py                # Centralized config (URLs, credentials, timeouts)
│
├── pages/                       # Page Object Model
│   ├── base_page.py             # Common page actions + explicit waits
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/                       # Pytest test suites
│   ├── conftest.py              # Fixtures (driver setup/teardown)
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_checkout.py
│   └── test_api.py              # API testing with requests
│
├── features/                    # BDD layer (Behave)
│   ├── login.feature
│   └── steps/
│       └── login_steps.py
│
├── utils/
│   ├── driver_factory.py        # WebDriver factory (Chrome/Firefox/headless)
│   ├── logger.py                # Centralized logging
│   ├── data_reader.py           # Read test data from JSON/CSV
│   └── db_helper.py             # SQL validation layer
│
├── reports/                     # HTML reports + screenshots
│
├── .github/workflows/
│   └── ci.yml                   # GitHub Actions pipeline
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🎯 Key Features

| Feature | Implementation |
|---------|----------------|
| **Page Object Model** | Clean separation between test logic and UI locators |
| **Explicit Waits** | `WebDriverWait` + `ExpectedConditions` — zero `time.sleep()` |
| **Data-Driven Testing** | Pytest parametrize + JSON test data |
| **BDD** | Behave with Gherkin feature files |
| **API Testing** | `requests` library + JSON schema validation |
| **Database Validation** | SQL queries to verify data integrity post-UI actions |
| **Cross-Browser** | Chrome, Firefox, Edge via driver factory |
| **Headless Mode** | Configurable for CI/CD execution |
| **HTML Reporting** | `pytest-html` + screenshots on failure |
| **Logging** | Structured logs with timestamps |
| **CI/CD** | GitHub Actions runs tests on every push |
| **Parallel Execution** | `pytest-xdist` for concurrent test runs |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Chrome browser
- Git

### Installation

```bash
# Clone the repo
git clone https://github.com/akankshasingh1404-spec/akanksha-testing-project.git
cd akanksha-testing-project

# Create virtual environment
python -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_login.py

# Run in headless mode
pytest --headless

# Run with HTML report
pytest --html=reports/report.html --self-contained-html

# Run in parallel (4 workers)
pytest -n 4

# Run BDD scenarios
behave features/

# Run with browser choice
pytest --browser=firefox
```

---

## 📊 Sample Test Report

After running tests, open `reports/report.html` to view:
- ✅ Pass/Fail summary
- 📸 Screenshots on failure
- ⏱️ Execution time per test
- 📝 Logs and stack traces

---

## 🔄 CI/CD Pipeline

Every push to `main` triggers `.github/workflows/ci.yml`, which:
1. Installs Python and dependencies
2. Runs the full Pytest suite in headless Chrome
3. Uploads HTML reports as artifacts
4. Fails the build on test failures

---

## 🧪 What This Framework Demonstrates

This repo is built to demonstrate the SDET skills listed on my resume:

- ✅ **Framework architecture & maintainability** (POM, factory pattern, config separation)
- ✅ **Reduced regression time** (parallel execution + headless = ~70% faster)
- ✅ **CI/CD integration** (GitHub Actions, headless execution)
- ✅ **API + UI + DB testing** (full-stack validation)
- ✅ **BDD collaboration** (Behave features readable by non-technical stakeholders)
- ✅ **Cross-browser testing** (driver factory pattern)
- ✅ **Defect investigation** (logs, screenshots, stack traces)

---

## 📬 Contact

**Akanksha Singh**
📧 akankshasingh20166@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/akanksha-singh-b600875)
📍 Sterling, VA — Authorized to work in the U.S., no sponsorship required.
