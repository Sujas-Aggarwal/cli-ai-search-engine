from selenium import webdriver
import urllib.parse
from config import options
import click
import scrappers

@click.command()
@click.option('--prompt', prompt=click.style('Enter Your Prompt',fg="green"), help='Enter Your Prompt for AI Solution')
def AiHandler(prompt):
    """Handle AI Search Requests"""
    driver = webdriver.Chrome(options=options)
    query = "https://search.brave.com/search?q=" + urllib.parse.quote(prompt)
    driver.get(query)
    try:
        llm_response = scrappers.scrapAiResponse(driver=driver)
        if (llm_response==""):
            raise Exception
        click.echo("\n\n")
        click.echo(click.style("AI Response:",  bg="white",fg="black", bold=True))
        click.echo(llm_response)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
