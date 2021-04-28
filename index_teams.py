# Creates an index of teams, confs, and urls and writes to DataBase

# Import required modules
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import time
import requests

# Import files
import get_request as get

# This class sends GET requests and compiles data into lists:
# NOTE: instantiating this class will run ALL code in this file.
class Index:
    def __init__(self, year):
        # define init arguments
        self.year = year

        # Define attributes
        self.teams = []
        self.team_urls = []
        self.team_confs = []

    def index_teams(self):
        index_url = "http://cfbstats.com/" + self.year + "/team/index.html"
        index_html = get.GET_HTML(1).soup_recipe(index_url)
        conf_tables = index_html.find_all(class_="conference")

        # Loop through each conf table and find team data
        for conf_table in conf_tables:
            conf_name = conf_table.find("h1").text
            conf_a_tags = conf_table.find_all("a")

            # Loop through each conference
            for a_tag in conf_a_tags:
                # Builds out arrays with team info
                self.teams.append(a_tag.text)
                self.team_urls.append(a_tag.get("href"))
                self.team_confs.append(conf_name)

        # Calls the function to write this info to a database
        self.write_db()

    # This method writes the lists created above to database files
    def write_db(self):
        # Create a dict to house data within keys (column headings)
        df_data = {}
        df_data["Team"] = self.teams
        df_data["Conf"] = self.team_confs
        df_data["url"] = self.team_urls

        # Insert data into Pandas DataFrame
        team_index_df = pd.DataFrame(df_data)

        # Write data to Excel file
        filename = self.year + "stats.xlsx"
        book = load_workbook(filename)
        writer = pd.ExcelWriter(filename, engine="openpyxl")
        writer.book = book

        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        team_index_df.to_excel(writer, "Team Index", index=False)
        writer.save()


############ End Index class ############