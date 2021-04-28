# Sends a GET requests and returns html

# Import necessary modules
from bs4 import BeautifulSoup
import requests
import time

# This class will be called every time we need to send a GET request and parse HTML. This has downtime built in to avoid flooding the server with requests
class GET_HTML:
    def __init__(self, i):
        self.i = i

    def soup_recipe(self, address):
        page = requests.get(address)
        soup = BeautifulSoup(page.content, "html.parser")
        GET_HTML.page_status(self, page)  # Calls the page_status method
        time.sleep(1)
        return soup

    # This method is a debug to give info about the GET request results
    def page_status(self, results):
        try:
            results.status_code  # results is the callable object requests module creates, i.e. index_page_soup
            if results.status_code == 200:
                print("Connected" + str(self.i))
                self.i += 1
                pass
            if results.status_code != 200:
                print("Page Connection Error")
        except:
            print("An error occured while attempting to connect to the website.")


############ End GET_HTML class ############