from selenium import webdriver
from selenium.webdriver import ChromeOptions
import urllib.parse
from click import echo, style
import scrappers


# Example usage with your query
query = "https://search.brave.com/search?q=" + urllib.parse.quote("how to make pizza")

# Set up Selenium WebDriver (assumes ChromeDriver is installed)
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--log-level=OFF")
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the initial query
    driver.get(query)
    try:
        driver.find_elements()
        llm_response = scrappers.getAIResponse(driver=driver)
        echo("\n\n")
        echo(style("\nAI Response:\n",  bg="white",fg="black", bold=True))
        echo(llm_response)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)
finally:
    # Clean up
    driver.quit()