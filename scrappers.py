from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from click import style, echo
def getAIResponse(driver: webdriver):
    try:
        load_more_button = driver.find_element(by=By.ID,value="llm-show-more-button")
        while (not load_more_button.is_displayed()):
            sleep(.1)
        load_more_button.click()
        while (True):
            try:
                driver.find_element(by=By.ID,value="chatllm-conversation")
                break
            except Exception as e:
                sleep(.1)
        llm_title_element = driver.find_element(by=By.ID,value="chatllm-title")
        llm_body_element = driver.find_element(by=By.ID,value="chatllm-main-answer-content")
        llm_body_element = driver.find_element(by=By.CLASS_NAME, value="llm-output")
        llm_response = ""
        llm_response+= style(llm_title_element.get_attribute("innerText"),bold=True,italic=True)
        llm_response+="\n\n"
        all_children_of_llm = llm_body_element.find_elements(By.XPATH, "./*")
        for i in all_children_of_llm:
            if "inline-refs" in i.get_attribute("class"):
                continue
            if (i.tag_name=="h1" or i.tag_name=="H1"):
                llm_response+= style("\n"+i.get_attribute("innerText").replace("\n",""),fg="white",bold=True)
            else:
                llm_response+= style(i.get_attribute("innerText").replace("\n",""),fg="cyan")
            llm_response+="\n"
        return llm_response
    except Exception as e:
        with open("logs.txt","w") as file:
            file.write(e)
        echo(style("Some Error Occured",fg="red"))
        return ""