#November 19, 2025
'''Pdf and Word Documents:
Pdf and word documents are binary files that require special libraries to read and write.
A binary file contains data encoded in binary (0s and 1s), structured for machine interpretation.
Modules for this section:
-PyPDF2 - for reading and writing PDF files
-python-docx - for reading and writing Word (.docx) files

'''
# PDF
'''.pdf: portable document format, a file format developed by Adobe to present documents consistently across various devices and platforms.
'''

#November 20, 2025
'''Extracting Text from PDFs:
To extract text from a PDF file using PyPDF2, follow these steps:
1. Install PyPDF2 using pip if you haven't already:
   pip install PyPDF2
2. Use the following code to read and extract text from a PDF file:
    import PyPDF2

    # Open the PDF file in read-binary mode
    with open('example.pdf', 'rb') as pdf_file:
    
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Extract text from each page
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        print(f'Page {page_num + 1}:\n{text}\n')

Example usage:
'''
import PyPDF2
# Open the PDF file in read-binary mode
with open('.\\Automating_the_boring_stuff\\how to write a business plan.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Extract text from the third page page
    page = pdf_reader.pages[14] # page numbering starts from 0

    text = page.extract_text()
    print(f'Page {num_pages }:{text}')

#Encrypting a PDF:
import PyPDF2

# Open the original PDF file in read-binary mode
with open('original.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_writer = PyPDF2.PdfWriter()

# Copy all pages to the writer object
for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Encrypt the PDF with a password
pdf_writer.encrypt('your_password')

# Write the encrypted PDF to a new file
with open('encrypted.pdf', 'wb') as encrypted_file:
    pdf_writer.write(encrypted_file)

pdf_file.close()
encrypted_file.close()

#Decrypting a PDF:
import PyPDF2
# Open the encrypted PDF file in read-binary mode
with open('encrypted.pdf', 'rb') as encrypted_file:
    pdf_reader = PyPDF2.PdfReader(encrypted_file)

# Check if the PDF is encrypted
if pdf_reader.is_encrypted:
    # Decrypt the PDF with the password
    pdf_reader.decrypt('your_password')

    # Extract text from the first page
    first_page = pdf_reader.pages[0]
    text = first_page.extract_text()
    print(text)