# Sends a GET requests and returns html

# Import necessary modules
from bs4 import BeautifulSoup
import requests
import time

# This class will be called every time we need to send a GET request and parse HTML. This has downtime built in to avoid flooding the server with requests
class Get:
    def __init__(self, i):
        self.i = i

    def soup_recipe(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        self.page_status(page)  # Calls the page_status method
        time.sleep(1)
        return soup

    def json(self, url):
        response = requests.get(url)
        self.page_status(response)  # Calls the page_status method
        time.sleep(1)
        return response.text

    # This method is a debug to give info about the GET request results
    def page_status(self, response):
        try:
            response.status_code  # results is the callable object requests module creates, i.e. index_page_soup
            if response.status_code == 200:
                print("Connected" + str(self.i))
                self.i += 1
                pass
            if response.status_code != 200:
                print("Page Connection Error")
        except:
            print("An error occured while attempting to connect to the website.")


############ End get_request class ############