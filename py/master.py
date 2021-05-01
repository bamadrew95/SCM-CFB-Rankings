# Bamadrew95's stat compiler. Uses Beautiful Soup and Panda to grab team names, conferences, and urls and put them into tabular form to be used by a data compiler
# Based on Bamaham93's FBS Scraper program

##############################################################################################
#  PLEASE NOTE: YOU MUST CREATE A BLANK EXCEL FILE WITH THE CORRECT NAME FOR THE CODE TO WORK
##############################################################################################

# The year below controls what year of stats the program will grab.
year = "2014"

# Import python files
import index_teams as teams
import compile_stats as stats

# Execute code (Comment out what you don't want to run)
# index = teams.Index(year).index_teams()
compile_stats = stats.Compile(year).compile_stats()
