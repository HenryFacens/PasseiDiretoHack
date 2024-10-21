# Selenium Web Scraping Tool - Passei Direto Hack

This project is a **web scraping tool** built with Python and Selenium. It extracts content from PDFs or question pages based on the provided URL. The extracted text is saved to a `.txt` file for further analysis or use.

---

## 🛠 Features

- **PDF Content Extraction**: Identifies and extracts content from PDF pages.
- **Question and Answer Extraction**: Scrapes question details and all available answers.
- **Error Handling**: Handles timeouts and missing elements gracefully.
- **Automated File Saving**: Saves extracted content to a text file.

---

## 📂 Project Structure


---

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/HenryFacens/PasseiDiretoHack.git
   cd PasseiDiretoHack
    
    python -m venv venv
    source venv/bin/activate  # On Linux/Mac
    .\venv\Scripts\activate   # On Windows

    pip install -r requirements.txt 
## 📋 How it Works
1. **The script accepts a URL to either:**
    * A PDF page (identified by /arquivo/ in the URL).
    *  A Question page (identified by /pergunta/ in the URL).

2. **PDF Pages:**
    * It iterates through pages, extracts the text, and saves it in conteudo_pdf.txt.

3. **Questions and Answers:**
    * It finds the answers and saves them in respostas.txt.

4. **Logging and Exits:**
    * If no valid content is found, the script logs a message and exits gracefully.

## 💡 Usage Example
1. **Extracting a PDF**
    ```bash
    URL: https://www.passeidireto.com/arquivo/123456789
    Output: conteudo_pdf.txt
2. **Extracting Question and Answers**
    ```bash
    URL: https://www.passeidireto.com/pergunta/148438722/...
    Output: respostas.txt
🐞 **Error Handling**
* TimeoutException: 
    If elements are not found within 30 seconds, the script logs a timeout error.
* NoSuchElementException: 
    Handles cases where expected elements are not present.

🔧 **Customization**
Adjust Timeouts: 
* Modify WebDriverWait(driver, 30) for longer or shorter wait times.
Browser Configuration: 
* Replace webdriver.Chrome() with other drivers like Firefox() if needed.

🤝 **Contributing**
* Feel free to open issues or submit pull requests if you want to contribute!
