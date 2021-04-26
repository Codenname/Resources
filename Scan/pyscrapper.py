#!/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

# request the web page
def web_request(url):
    response = requests.get(url)
    html = response.text
    return html
    
def help():
    print('''Simple web scrapper that saves the contents into "scrape.txt"
    
    Syntax:\n
    pyscrapper <option>
    
    Options:
    -u		Url 
    -help 	Print help
    ''')

def main():
    try:
        if len(sys.argv) <= 1: 
            help()
        # gets the page
        elif sys.argv[1] == "-u":
            try:
                url = sys.argv[2]
                print(f"[+] Scraping {url}")
                response = web_request(url)
                beautified = BeautifulSoup(response, 'html.parser')
                word_list_page = beautified.get_text()
                beautified = beautified.prettify()
                word_list = word_list_page.replace(" ", "\n")
                print("[+] Scraped Content: ")
                print(word_list)
                # writes the webpage info to a file
                output_file = open("scrape.txt", "w")
                lines_to_write = word_list
                output_file.writelines(lines_to_write)
                output_file.close()
            except IndexError:
                print("[-] Url not provided!")
                help()
        else:
            print("\n")
            help()
    except KeyboardInterrupt:
        print("[*] Keyboard Interrupt Exiting...")
        exit()
    
main()
