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
