# November 11, 2025

'''Web Scraping:
Web scraping is the process of extracting data from websites.
It involves fetching the HTML content of a webpage and then parsing that content to extract the desired information.
To perform web scraping in Python, we often use libraries such as requests and BeautifulSoup.
1.Requests Library: This library allows you to send HTTP requests to a webpage and retrieve its content.
2.BeautifulSoup Library: This library is used to parse HTML and XML documents. It provides Pythonic idioms for iterating, searching, and modifying the parse tree.
3.webbrowser Library: This library provides a high-level interface to allow displaying Web-based documents to users.
4.Selenium Library: launches and contorls web browsers. Used for automating tasks such as filling out forms, clicking buttons, and navigating between pages.
Example Usage:'''

import webbrowser

webbrowser.open('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')  # Opens the specified URL in the default web browser


#Using the Requests Library to fetch a webpage
import requests
#NB: The 'pg1112.txt' is the plain text version of Shakespeare's play "Romeo and Juliet" from Project Gutenberg.
#NB: Make sure you have an active internet connection to run this code successfully.
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') # Fetches the content of the webpage


print(type(res)) #)utput >>> <class 'requests.models.Response'>
print(res.status_code == requests.codes.ok)  # Output >>> True
print(len(res.text))  # depending on the content of the pg1112.txt Output >>>163338

print(res.text[:250]) # Prints the first 250 characters of the webpage content

# November 12, 2025

'''BeautifulSoup Library
BeautifulSoup is a Python library used for parsing HTML and XML documents.
It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
To use BeautifulSoup, you need to install it first using pip:
pip install beautifulsoup4
After, you then have to create a BeautifulSoup object by passing the HTML content and a parser to it.
Example Usage:
'''
from bs4 import BeautifulSoup
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

soup = BeautifulSoup(res.text,'html.parser')  # Create a BeautifulSoup object
print(type(soup))  # Output >>> <class 'bs4.BeautifulSoup'>

'''Finding an Element with the select() Method:
The select() Method allows you to find elements in the HTML document using CSS selectors.
It returns a list of all matching elements.
Example Usage:
'''
import bs4
exampleFile = open('example.html')  # Open an HTML file
exampleSoup = BeautifulSoup(exampleFile, 'html.parser')  # Create a BeautifulSoup object
elems = exampleSoup.select('#author')  # Select elements with the id 'author'
print(type(elems))  # Output >>> <class 'list'>
print(len(elems))  # Output >>> 1
print(type(elems[0]))  # Output >>> <class 'bs4.element.Tag'>
print(elems[0].getText())  # Output >>> Al Sweigart
print(str(elems[0]))  # Output >>> <span id="author">Al Sweigart</span>
print(elems[0].attrs)  # Output >>> {'id': 'author'}


# November 13, 2025
'''Using Selenium for Web Scraping:
Selenium is a powerful tool for automating web browsers.
It can be used for web scraping, especially for websites that use JavaScript to load content dynamically.
To use Selenium, you need to install the Selenium package and a web driver for your browser (e.g., ChromeDriver for Google Chrome).
You can install Selenium using pip:
pip install selenium
You can install ChromeDriver by downloading it from the official site and ensuring it's in your system's PATH.

Example Usage:'''

