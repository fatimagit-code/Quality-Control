# Swag Labs E-commerce Automation Project (Selenium/Pytest)

## Project Overview

This repository contains a comprehensive suite of automated end-to-end (E2E) tests for the **Swag Labs** e-commerce application. The solution is built using **Python**, the **Selenium WebDriver** framework for browser interaction, and **Pytest** for test execution and reporting.

The goal of this project was to establish a robust, maintainable, and highly readable test foundation using the **Page Object Model (POM)** design pattern. This approach ensures high code reusability and simplifies maintenance as the application UI evolves.

---

## Key Achievements & Test Coverage (29 Test Cases)

This project successfully implemented **29 distinct test scenarios** covering all major functional areas of the Swag Labs application.

### 1. User Authentication & Access Control (Major Focus)
* **Successful Login:** Verification of standard, visual, and performance users.
* **Error Handling:** Validation of locked-out user login failures.
* **Credential Integrity:** Verification of failed login attempts with invalid username/password combinations.

### 2. Shopping Cart Functionality & Data Integrity
The majority of testing focused on the integrity and state management of the shopping cart.

| Scenario | Coverage Area | Status |
| :--- | :--- | :--- |
| **Add/Remove Items** | Adding single and multiple items (up to 3). | Complete |
| **Cart Persistence** | Testing cart contents after logout/re-login (Verifying expected non-persistence). | Complete |
| **UI Toggling** | Verifying the "Add to Cart" button correctly toggles to "Remove" on the Inventory page. | Complete |
| **Quantity & Price** | Verification that the product quantity (e.g., `1`) and price displayed in the cart match the inventory data. | Complete |

### 3. Checkout Workflow & Financial Integrity
Critical flow testing to ensure accurate transaction processing.

* **Checkout Flow:** Successful navigation through the Information, Cart, and Overview steps.
* **Mandatory Fields:** Verification of error handling when required checkout fields (Name, ZIP Code) are missing.
* **Price Calculation (Critical):** Verification that `Item Subtotal + Tax` mathematically equals the `Grand Total` on the final Overview page.
* **Order Confirmation:** Asserting the presence of the final "Thank You" message after a successful order completion.

### 4. Application UI State & Navigation
* **Logout Functionality:** Correctly logging out and redirecting to the login page.
* **Page Accessibility:** Ensuring all key pages (Inventory, Cart, Checkout) are accessible and display the correct header titles.

---

## Project Structure and Technology Stack

### Technology Used
| Technology | Purpose |
| :--- | :--- |
| **Python** | Primary programming language. |
| **Selenium WebDriver** | Browser automation tool. |
| **Pytest** | Testing framework for execution, parametrization, and reporting. |
| **Page Object Model (POM)** | Design pattern for maintainability and code organization. |

### Page Object Model (POM) Implementation

The solution is highly maintainable due to its POM structure:

* **`BasePage`:** Contains shared WebDriver logic (e.g., `click()`, `get_text()`, `is_element_present()`).
* **Dedicated Page Classes:** Separate classes for each major application screen (`LoginPage`, `InventoryPage`, `CartPage`, `CheckoutInformationPage`, etc.).
* **Data Isolation:** All locators are defined as constants within their respective page classes, ensuring UI changes only require modification in one place.

## How to Run the Tests

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/fatimagit-code/Quality-Control.git](https://github.com/fatimagit-code/Quality-Control.git)
    cd swag_labs # Change to your project directory
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    # (Ensure requirements.txt lists selenium, pytest, etc.)
    ```

3.  **Execute Tests:**
    ```bash
    # Run all tests using pytest
    pytest
    
    # Run tests marked as 'major'
    pytest -m major
    
    # Generate an HTML report (optional)
    pytest --html=report.html
    ```

---

*This project was completed as part of a comprehensive quality control and test automation initiative.*
