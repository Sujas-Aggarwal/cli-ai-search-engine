from selenium.webdriver import ChromeOptions

# Set up Selenium WebDriver (assumes ChromeDriver is installed)
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")  # Disable GPU (recommended for headless)
options.add_argument("--no-sandbox")  # Often needed for headless in some environments
options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues
options.add_argument("--log-level=3")  # Minimize Chrome browser logs (3 = ERROR only)
options.add_argument("--silent")  # Further suppress browser output
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable logging switches
options.add_argument("--disable-extensions")  # Disable extensions that might log
options.add_argument("--disable-infobars")   # Disable info bars

