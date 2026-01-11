# Testing Automation Frameworks
This repository is utilizied to UI and API test the CatsOfWC.org website. (Linux/Python/Flask/HTML5)
This repository is utilizied to UI and API test the CatsOfWC.com website. (Linux/PHP/HTML5)

---

## Overview
The repository contains three layers of testing:


1. **UI Automation**  
   - Implemented using **Playwright** and **Pytest**.  
   - Implemented using **Selenium** and **Pytest**.  
   - Demonstrates Page Object Model (POM), headless execution, and explicit waits.  
   - Example test: login flow and menu testings with screenshots.

2. **API Testing**  
   - Implemented using **Pytest** and **Python Requests**.  
   - Demonstrates authentication, status and schema validation, and parameterized tests.
   - Connects to API Petstablished to test Pet widgit display

Each layer is executed independently in **CI/CD pipelines** to mirror real-world test strategies.

---
## Project Overview ##
TEST-AUTOMATION-EXAMPLES
.github\workflows
-Scripts
-tests
-test_results

