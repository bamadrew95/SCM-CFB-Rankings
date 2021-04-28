# This will send get requests to each teams stat page, gather stats, and write those stats to a DataBase file using Pandas

# Import necessary modules
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook

# Import GET_HTML file
import get_request as req


class Compile:
    def __init__(self, year):
        # initial names
        self.year = year
        self.test_url = ["http://www.cfbstats.com/2012/team/472/index.html"]
        self.team_urls = []
        self.team_stats = []
        self.stats = []
        self.team_stat_titles = [
            "Points/Game",
            "Games",
            "Total Points",
            "First Downs",
            "Rush First Downs",
            "Pass First Downs",
            "First Downs by Penalty",
            "Rush Yards/Att",
            "Rush Att",
            "Rush Yards",
            "Rush TDs",
            "Pass Rating",
            "Pass Yards",
            "Pass Att",
            "Pass Comp",
            "INTs",
            "Pass TDs",
            "Total Off Yards/Play",
            "Total Off Plays",
            "Total Off Yards",
            "Punt Yards/Return",
            "Punt Returns",
            "Punt Return Yards",
            "Punt Return TDs",
            "KO Yards/Return",
            "KO Returns",
            "KO Return Yards",
            "KO Return TDs",
            "Yards/Punt",
            "Punts",
            "Punt Yards",
            "INT returns",
            "INT Yards",
            "INT TDs",
            "Fumbles",
            "Fumbles Lost",
            "Penalties",
            "Penalty Yards",
            "TOP/Game",
            "3rd Down Conversion %",
            "3rd Down Conversion Att",
            "3rd Down Conversions",
            "4th Down Conversion %",
            "4th Down Conversion Att",
            "4th Down Conversions",
            "RZ Success %",
            "RZ Att",
            "RZ Scores",
            "FG Success %",
            "FG Att",
            "FGs Made",
            "PAT Success %",
            "PAT Att",
            "PATs Made",
            "2-Point Success %",
            "2-Point Att",
            "2-Point Conversions",
        ]
        self.opp_stat_titles = ["Opp " + title for title in self.team_stat_titles]
        self.stat_titles = self.team_stat_titles + self.opp_stat_titles

    # Read info from spreadsheet
    def read_db(self):

        self.team_index = pd.read_excel(
            self.year + "stats.xlsx", sheet_name="Team Index"
        )

    def compile_info(self):
        # Compile urls from spreadsheet into usable url list
        self.read_db()
        urls = self.team_index["url"].to_list()
        # Add prefix to each url
        for url in urls:
            self.team_urls.append("http://cfbstats.com" + url)

        # Compile Team names from spreadsheet into usable url list
        self.team_names = self.team_index["Team"].to_list()

    def compile_stats(self):
        html_class = req.GET_HTML(1)

        # Run compile_info function so urls and team names are compiled before running this code
        self.compile_info()
        # Loop through each url and send a GET request to each
        for url in self.team_urls:
            # Clears list after each team
            single_team_stats = []
            single_opp_stats = []
            html = html_class.soup_recipe(url)
            # Grabs stats table
            stat_table = html.find("table", class_="team-statistics")
            # Make list of rows
            stat_table_rows = stat_table.find_all("tr")
            # Drop first row
            stat_table_rows.pop(0)

            # Loop through each row and separate team stats from oppoennt stats in different lists.
            for tr in stat_table_rows:
                # isolate the three different columns
                cell1 = tr.find_next()
                cell2 = cell1.find_next()
                cell3 = cell2.find_next()

                # process cells and append results to the lists given below.
                self.process_stat_cell(cell2, single_team_stats)
                self.process_stat_cell(cell3, single_opp_stats)

            # Combine team and opp stats into one long list for each team
            self.team_stats = single_team_stats + single_opp_stats

            self.stats.append(self.team_stats)

        self.stats_df = pd.DataFrame(self.stats, columns=self.stat_titles)

        # Add team names column at the start
        self.stats_df.insert(0, "Team", self.team_names)

        # create dict to change dtypes
        dtype_dict = {}
        self.stat_titles.insert(0, "Team")

        for title in self.stat_titles:
            dtype_dict[title] = "float64"

        # Set custom dtypes
        dtype_dict["Team"] = "object"
        dtype_dict["TOP/Game"] = "object"
        dtype_dict["Opp TOP/Game"] = "object"

        self.stats_df = self.stats_df.astype(dtype_dict)

        # Write data to Excel file
        filename = self.year + "stats.xlsx"
        book = load_workbook(filename)
        writer = pd.ExcelWriter(filename, engine="openpyxl")
        writer.book = book

        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        self.stats_df.to_excel(writer, "Raw Stats", index=False)
        writer.save()

    def process_stat_cell(self, cell, stat_list):
        # Get text from each td given
        cell_text = cell.text

        if cell_text == "-":
            cell_text = "0"

        cell_split = cell_text.split(" - ")

        for c in cell_split:
            if c == "":
                c = "0"
            stripped = c.strip(" %")
            replaced = stripped.replace(",", "")
            stat_list.append(replaced)