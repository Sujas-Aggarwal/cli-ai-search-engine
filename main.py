from selenium import webdriver
from selenium.webdriver import ChromeOptions
import urllib.parse
import click
import scrappers


# Example usage with your query

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

@click.command()
@click.option('--prompt', prompt='Enter Your Prompt', help='Enter Your Prompt for AI Solution')
def AiHandler(prompt):
    """Handle AI Search Requests"""
    driver = webdriver.Chrome(options=options)
    query = "https://search.brave.com/search?q=" + urllib.parse.quote(prompt)
    driver.get(query)
    try:
        llm_response = scrappers.getAIResponse(driver=driver)
        if (llm_response==""):
            raise Exception
        click.echo("\n\n")
        click.echo(click.style("AI Response:",  bg="white",fg="black", bold=True))
        click.echo(llm_response)
    except Exception as e:
        print(e)
    finally:
        driver.quit()


AiHandler()


