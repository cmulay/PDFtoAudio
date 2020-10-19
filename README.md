# Python-Automation-Script

This Python Automation Script will read PDF's out loud.

## Installation

Check whether  you are running latest package manager [pip](https://pip.pypa.io/en/stable/)
```bash
pip install --upgrade pip
```
Use the package manager to install pyttsx3.
```bash
pip install pyttsx3
```
Similarly install PyPDF2.
```bash
pip install PyPDF2
```

## Usage

Import installed packages
```python
import pyttsx3 # Python Text to Speech Version 3
import PyPDF2 # Python PDF Reader/Writer 2
```
Copy & Paste your desired PDF in project folder.
Open the book you want to listen  
```python
book = open('pdf_name.pdf', 'rb') # Opens pdf in book (replace pdf_name.pdf with you pdf name)
```
Pre-work such as reading total number of pages from the book
```python
pdfReader = PyPDF2.PdfFileReader(book) # Reads book
pages = pdfReader.numPages # Calculates total number of pages from book
print(pages) # prints total number of pages  
```

Initialize Python Text to Speech
```python
bot = pyttsx3.init()
```

```python
for num in range(0, pages): # from first page (0) to calculated last page
    page = pdfReader.getPage(0)
    # to skip index and pdf clutter replace 0 with your desired page number - 1
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()
```

## License
[GNU GENERAL PUBLIC LICENSE](https://github.com/cmulay/Python-Automation-Script/blob/main/LICENSE)
