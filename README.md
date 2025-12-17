# Test Automation Examples

This repository demonstrates practical test automation approaches commonly used in production systems.
It is intended as a portfolio example for automation, CI/CD, and test strategy and resume / interview example.

---

## Overview

The repository contains three layers of testing:

1. **UI Automation**  
   - Implemented using **Selenium** and **Pytest**.  
   - Demonstrates Page Object Model (POM), headless execution, and explicit waits.  
   - Example test: login flow or search functionality
   - Utilized in Sanity Check post deployment testing to ensure main page and menu links appear and are functional

Selenium functions are grouped into specialized python definitions to avoid flakiness and implement quality wait times.

Outcome:
Produces screens shots of https://catsofwc.com (Cats of West Central Illinois Inc 501c3) menus after Selenium Clicks.
PyTest Reports. Logging, UI Selenium Python commands. 
Code Commits. 
