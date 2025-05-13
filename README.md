# Web Automation Test Project with Selenium

This project contains Python code to perform web automation testing of the [Website Name] website using the Selenium library. The main goal of this code is to log into the user panel and submit a specific form on the website.

## Prerequisites

Before running this code, ensure that you have the following prerequisites:

* **Python 3:** Make sure Python 3 is installed on your system. You can check your Python version by running `python --version` or `python3 --version` in the command line.
* **Selenium:** The Selenium library must be installed. If not installed, you can install it using pip:
    ```bash
    pip install selenium
    ```
* **WebDriver:** To interact with the Chrome browser, you need ChromeDriver.
    * **Installation via `webdriver-manager` (Recommended):** This project uses `webdriver-manager` to automatically manage ChromeDriver. If you don't have it installed:
        ```bash
        pip install webdriver-manager
        ```
        The code will automatically download and manage the appropriate ChromeDriver version.
    * **Manual Installation:** If you prefer to manage ChromeDriver manually, you need to download the version compatible with your Chrome browser from the [ChromeDriver website](https://chromedriver.chromium.org/downloads) and specify its path in your code (if you are not using `webdriver-manager`).

## How to Use

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone [https://github.com/reyhanefarahii/kudos.git](https://github.com/reyhanefarahii/kudos.git)
    cd kudos
    ```

2.  **Install prerequisites (if not using `webdriver-manager`, set up ChromeDriver manually):**
    ```bash
    pip install selenium webdriver-manager
    ```

3.  **Run the Python script:**
    ```bash
    python kudos.py
    ```

    Or replace `kudos.py` with the name of your file if it's different.
