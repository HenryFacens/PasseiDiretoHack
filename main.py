from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "https://www.passeidireto.com/pergunta/148438722/pergunta-1-um-analista-realizou-a-analise-do-teor-de-cloreto-em-uma-amostra-e-ob"
driver.get(url)

wait = WebDriverWait(driver, 30)

def remove_blur_and_extract_text(element):
    driver.execute_script("arguments[0].style.filter = 'none';", element)
    text = element.text.strip()
    return text

all_texts = []

if "/arquivo/" in url:
    print("Conteúdo identificado como PDF com base na URL.")
    is_pdf = True
    is_questions = False

    page_number = 1
    while True:
        try:
            page_id = f"pf{page_number}"
            page_element = wait.until(EC.presence_of_element_located((By.ID, page_id)))
            print(f"Página {page_number} encontrada com ID '{page_id}'.")
            
            page_text = remove_blur_and_extract_text(page_element)
            all_texts.append(page_text)
            
            page_number += 1
        except TimeoutException:
            if page_number == 1:
                print("Nenhuma página de PDF encontrada.")
            else:
                print(f"Nenhuma outra página encontrada após a página {page_number - 1}.")
            break
elif "/pergunta/" in url:
    print("Conteúdo identificado como Pergunta com base na URL.")
    is_pdf = False
    is_questions = True

    try:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[@class='answer-header' and text()='Respostas']")))
        print("Encontrado o cabeçalho 'Respostas' na página.")

        answers_elements = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='answers-list']//div[@id='answer-card']")))
        print(f"Encontrada(s) {len(answers_elements)} resposta(s).")

        for answer_el in answers_elements:
            try:
                answer_text_el = answer_el.find_element(By.XPATH, ".//div[contains(@class, 'answers-text')]//div[@class='ql-editor']")
                answer_text = remove_blur_and_extract_text(answer_text_el)
                all_texts.append(answer_text)
            except NoSuchElementException:
                print("Elemento de texto da resposta não encontrado dentro de 'answer-card'.")
    except TimeoutException:
        print("O cabeçalho 'Respostas' ou as respostas não foram encontrados. Nenhum conteúdo extraído.")
        is_questions = False
else:
    print("A URL não corresponde aos padrões esperados para PDF ou Pergunta.")
    is_pdf = False
    is_questions = False

if is_pdf:
    filename = "conteudo_pdf.txt"
elif is_questions:
    filename = "respostas.txt"
else:
    filename = None

if filename and all_texts:
    with open(filename, "w", encoding="utf-8") as file:
        for i, text in enumerate(all_texts, start=1):
            file.write(f"Resposta {i}:\n{text}\n\n")
    print(f"Extração de texto concluída. O conteúdo foi salvo em '{filename}'.")
else:
    print("Nenhum conteúdo extraído.")

driver.quit()
