import pdfplumber
def extract_text(file_path):
    content=""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            content=content+text
        return content

page_content=extract_text(r"C:\Users\akash\Documents\Local_serv\server\SONUAKASHSOUNDARARAJAN_RESUME.pdf")
print(page_content)