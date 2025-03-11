from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from click import style
def getAIResponse(driver: webdriver):
    load_more_button = driver.find_element(by=By.ID,value="llm-show-more-button")
    while (not load_more_button.is_displayed()):
        sleep(.1)
    load_more_button.click()
    llm_title_element = driver.find_element(by=By.ID,value="chatllm-title")
    while (not llm_title_element.is_displayed()):
        sleep(.1)
    llm_body_element = driver.find_element(by=By.ID,value="chatllm-main-answer-content")
    while (not llm_body_element.is_displayed()):
        sleep(.1)
    llm_body_element = driver.find_element(by=By.CLASS_NAME, value="llm-output")
    llm_response = ""
    llm_response+= style(llm_title_element.get_attribute("innerText"),bold=True,fg="blue",italic=True)
    llm_response+="\n\n"
    all_children_of_llm = llm_body_element.find_elements(By.XPATH, ".//*")
    for i in all_children_of_llm:
        llm_response+= style(i.get_attribute("innerText").replace("\n",""))
        llm_response+="\n"
    return llm_response