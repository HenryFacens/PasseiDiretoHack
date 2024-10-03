from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "Url do arquivo"
driver.get(url)

time.sleep(20)

file_html_content = driver.find_element(By.CLASS_NAME, 'FileHtmlViewer_file-html-content__Q7KGG')

banners = file_html_content.find_elements(By.CLASS_NAME, 'BannerSelector_banner-wrapper__F8hUy')
for banner in banners:
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, banner)

questions = []
elements = file_html_content.find_elements(By.XPATH, "//*[contains(text(), 'Pergunta')]")

for element in elements:
    questions.append(element.text)

for i, question in enumerate(questions, start=1):
    print(f"Questão {i}: {question}")

with open("perguntas.txt", "w", encoding="utf-8") as file:
    for i, question in enumerate(questions, start=1):
        file.write(f"Questão {i}: {question}\n")

driver.quit()
