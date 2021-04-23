# Bamadrew95's stat compiler. Uses Beautiful Soup and Panda to grab stats from web and compile and sort them by team.
# Based on Bamaham93's FBS Scraper program

######################################################################################################

# This will be used to store static html for a single teams page so that I don't have to keep using get requests while developing
testingSourceCode = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>cfbstats.com - 2009 Teams</title>
<link rel="stylesheet" type="text/css" href="/css/cfbstats.css">
<style type="text/css">
<!--
#wrapper {
	background: none;
}

#content {
	width: 100%;
}

div.conferences {
	width: 90%;
	margin: 20px auto;
}

div.conference {
	float: left;
	width: 23.5%;
	margin-left: 1%;
}

div.conference h1 {
	text-align: center;
	font-size: 95%;
	color: white;
	font-weight: bold;
	background-color: #616161;
	padding: 2px 0px;
	border-bottom-color: #616161;
	border-bottom-style: solid;
	border-bottom-width: 1px;
}

div.conference li {
	padding-left: 5px;
	padding-top: 2px;
	padding-bottom: 3px;
}	

div.conference ul {
	list-style: none;
	width: 100%;
}
-->
</style>

<!-- START Drew's Adds -->
<script type="text/javascript" src="http://coachesbythenumbers.com/wp-content/custom-php/jquery/jquery.min.js?version=133"></script>
<script type="text/javascript" src="http://coachesbythenumbers.com/wp-content/custom-php/cfbstats.js"></script>
<link rel="image_src" type="image/jpeg" href="http://coachesbythenumbers.com/wp-content/custom-php/images/socialLogo.png" />

<link rel="stylesheet" href="http://coachesbythenumbers.com/wp-content/custom-php/bootstrap/css/bootstrap.min.css?version=1">
<link rel="stylesheet" href="http://coachesbythenumbers.com/wp-content/custom-php/bootstrap/css/bootstrap-theme.min.css?version=1">
<link rel="stylesheet" href="http://coachesbythenumbers.com/wp-content/custom-php/cfbstats.css">

<!-- Start DFP SETUP - Header Tags -->
<script type='text/javascript'>
    var gptadslots=[], googletag = googletag || {}; googletag.cmd = googletag.cmd || [];
    (function(){ var gads = document.createElement('script');
        gads.async = true; gads.type = 'text/javascript';
        var useSSL = 'https:' == document.location.protocol;
        gads.src = (useSSL ? 'https:' : 'http:') + '//www.googletagservices.com/tag/js/gpt.js';
        var node = document.getElementsByTagName('script')[0];
        node.parentNode.insertBefore(gads, node);
    })();
</script>
<script type='text/javascript' src='https://img.bnqt.com/lib/js/sdpdfphelper.js'></script>
<script type='text/javascript'>
    googletag.cmd.push(function() {
        googletag.pubads().enableAsyncRendering(); googletag.pubads().enableSingleRequest();
        googletag.pubads().setTargeting('title', sdpTargeting.title)
            .setTargeting('targetPaths', sdpTargeting.targetPaths)
            .setTargeting('fullPath', sdpTargeting.fullPath)
            .setTargeting('queryStr', sdpTargeting.queryStr)
            .setTargeting('domainName', sdpTargeting.domainName);
    });
</script>
<!-- DFP SETUP end -->
<!-- END Drew's Adds -->
</head>

<body>
<div id="wrapper">
<div id="breadcrumb">
  <span class="label">You are here:</span>
  <a href="/">Home</a>
  <span class="separator">&gt;</span>
  <span class="selected">2009 Teams</span>
</div> <!-- breadcrumb -->

<!-- New navbar, added by Drew -->
<nav class="navbar navbar-default navbar-static-top navbar-inverse navbar-thin" role="navigation" style="margin-bottom:0px;">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <img src="http://coachesbythenumbers.com/wp-content/custom-php/images/sportsourcenav.png" width="210" style="border:0;margin-top:13px"/>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav navbar-nav-thin navbar-right">
        <li><a href="mailto:team@sportsourceanalytics.com">Advertise?</a></li>
        <li><a href="mailto:feedback@cfbstats.com">Contact Us</a></li>
        <li><a href="https://twitter.com/SportSourceA"><img src="http://coachesbythenumbers.com/wp-content/custom-php/images/twitter_icon_24.png" width="14" style="margin-bottom:5px"/> @SportSourceA</a></li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>

<div id="globalHeader">
  <a id="imagemap" href="/"></a>
  <ul id="globalNav">
    <li><a href="/">Home</a></li>
    <li><a href="/2020/national/index.html">National</a></li>
    <li><a href="/2020/conference/index.html">Conferences</a></li>
    <li><a href="/2020/team/index.html">Teams</a></li>
    <li><a href="/2020/player/index.html">Players</a></li>
  </ul>
</div> <!-- globalHeader -->
<div id="content">
<h1 id="pageTitle">2009 Teams</h1>
<div id="seasons">
<ul>
  <li><a href="/2020/team/index.html">2020</a></li>
  <li><a href="/2019/team/index.html">2019</a></li>
  <li><a href="/2018/team/index.html">2018</a></li>
  <li><a href="/2017/team/index.html">2017</a></li>
  <li><a href="/2016/team/index.html">2016</a></li>
  <li><a href="/2015/team/index.html">2015</a></li>
  <li><a href="/2014/team/index.html">2014</a></li>
  <li><a href="/2013/team/index.html">2013</a></li>
  <li><a href="/2012/team/index.html">2012</a></li>
  <li><a href="/2011/team/index.html">2011</a></li>
  <li><a href="/2010/team/index.html">2010</a></li>
  <li class="selected">2009</li>
</ul>
</div>
<div class="conferences">
<div class="conference">
<h1>Atlantic Coast Conference</h1>
<ul>
  <li><a href="/2009/team/67/index.html">Boston College</a></li>
  <li class="even-row"><a href="/2009/team/147/index.html">Clemson</a></li>
  <li><a href="/2009/team/193/index.html">Duke</a></li>
  <li class="even-row"><a href="/2009/team/234/index.html">Florida State</a></li>
  <li><a href="/2009/team/255/index.html">Georgia Tech</a></li>
  <li class="even-row"><a href="/2009/team/392/index.html">Maryland</a></li>
  <li><a href="/2009/team/415/index.html">Miami (Florida)</a></li>
  <li class="even-row"><a href="/2009/team/457/index.html">North Carolina</a></li>
  <li><a href="/2009/team/490/index.html">North Carolina State</a></li>
  <li class="even-row"><a href="/2009/team/746/index.html">Virginia</a></li>
  <li><a href="/2009/team/742/index.html">Virginia Tech</a></li>
  <li class="even-row"><a href="/2009/team/749/index.html">Wake Forest</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Big 12 Conference</h1>
<ul>
  <li><a href="/2009/team/51/index.html">Baylor</a></li>
  <li class="even-row"><a href="/2009/team/157/index.html">Colorado</a></li>
  <li><a href="/2009/team/311/index.html">Iowa State</a></li>
  <li class="even-row"><a href="/2009/team/328/index.html">Kansas</a></li>
  <li><a href="/2009/team/327/index.html">Kansas State</a></li>
  <li class="even-row"><a href="/2009/team/434/index.html">Missouri</a></li>
  <li><a href="/2009/team/463/index.html">Nebraska</a></li>
  <li class="even-row"><a href="/2009/team/522/index.html">Oklahoma</a></li>
  <li><a href="/2009/team/521/index.html">Oklahoma State</a></li>
  <li class="even-row"><a href="/2009/team/703/index.html">Texas</a></li>
  <li><a href="/2009/team/697/index.html">Texas A&amp;M</a></li>
  <li class="even-row"><a href="/2009/team/700/index.html">Texas Tech</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Big East Conference</h1>
<ul>
  <li><a href="/2009/team/140/index.html">Cincinnati</a></li>
  <li class="even-row"><a href="/2009/team/164/index.html">Connecticut</a></li>
  <li><a href="/2009/team/367/index.html">Louisville</a></li>
  <li class="even-row"><a href="/2009/team/545/index.html">Pittsburgh</a></li>
  <li><a href="/2009/team/587/index.html">Rutgers</a></li>
  <li class="even-row"><a href="/2009/team/651/index.html">South Florida</a></li>
  <li><a href="/2009/team/688/index.html">Syracuse</a></li>
  <li class="even-row"><a href="/2009/team/768/index.html">West Virginia</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Big Ten Conference</h1>
<ul>
  <li><a href="/2009/team/301/index.html">Illinois</a></li>
  <li class="even-row"><a href="/2009/team/306/index.html">Indiana</a></li>
  <li><a href="/2009/team/312/index.html">Iowa</a></li>
  <li class="even-row"><a href="/2009/team/418/index.html">Michigan</a></li>
  <li><a href="/2009/team/416/index.html">Michigan State</a></li>
  <li class="even-row"><a href="/2009/team/428/index.html">Minnesota</a></li>
  <li><a href="/2009/team/509/index.html">Northwestern</a></li>
  <li class="even-row"><a href="/2009/team/518/index.html">Ohio State</a></li>
  <li><a href="/2009/team/539/index.html">Penn State</a></li>
  <li class="even-row"><a href="/2009/team/559/index.html">Purdue</a></li>
  <li><a href="/2009/team/796/index.html">Wisconsin</a></li>
</ul>
</div> <!-- conference -->
<div style="clear:both;"></div>
</div> <!-- conferences -->
<div class="conferences">
<div class="conference">
<h1>Conference USA</h1>
<ul>
  <li><a href="/2009/team/196/index.html">East Carolina</a></li>
  <li class="even-row"><a href="/2009/team/288/index.html">Houston</a></li>
  <li><a href="/2009/team/388/index.html">Marshall</a></li>
  <li class="even-row"><a href="/2009/team/404/index.html">Memphis</a></li>
  <li><a href="/2009/team/574/index.html">Rice</a></li>
  <li class="even-row"><a href="/2009/team/663/index.html">SMU</a></li>
  <li><a href="/2009/team/664/index.html">Southern Mississippi</a></li>
  <li class="even-row"><a href="/2009/team/718/index.html">Tulane</a></li>
  <li><a href="/2009/team/719/index.html">Tulsa</a></li>
  <li class="even-row"><a href="/2009/team/9/index.html">UAB</a></li>
  <li><a href="/2009/team/128/index.html">UCF</a></li>
  <li class="even-row"><a href="/2009/team/704/index.html">UTEP</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Independent</h1>
<ul>
  <li><a href="/2009/team/725/index.html">Army</a></li>
  <li class="even-row"><a href="/2009/team/726/index.html">Navy</a></li>
  <li><a href="/2009/team/513/index.html">Notre Dame</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Mid-American Conference</h1>
<ul>
  <li><a href="/2009/team/5/index.html">Akron</a></li>
  <li class="even-row"><a href="/2009/team/47/index.html">Ball State</a></li>
  <li><a href="/2009/team/71/index.html">Bowling Green</a></li>
  <li class="even-row"><a href="/2009/team/86/index.html">Buffalo</a></li>
  <li><a href="/2009/team/129/index.html">Central Michigan</a></li>
  <li class="even-row"><a href="/2009/team/204/index.html">Eastern Michigan</a></li>
  <li><a href="/2009/team/331/index.html">Kent State</a></li>
  <li class="even-row"><a href="/2009/team/414/index.html">Miami (Ohio)</a></li>
  <li><a href="/2009/team/503/index.html">Northern Illinois</a></li>
  <li class="even-row"><a href="/2009/team/519/index.html">Ohio</a></li>
  <li><a href="/2009/team/690/index.html">Temple</a></li>
  <li class="even-row"><a href="/2009/team/709/index.html">Toledo</a></li>
  <li><a href="/2009/team/774/index.html">Western Michigan</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Mountain West Conference</h1>
<ul>
  <li><a href="/2009/team/721/index.html">Air Force</a></li>
  <li class="even-row"><a href="/2009/team/77/index.html">BYU</a></li>
  <li><a href="/2009/team/156/index.html">Colorado State</a></li>
  <li class="even-row"><a href="/2009/team/473/index.html">New Mexico</a></li>
  <li><a href="/2009/team/626/index.html">San Diego State</a></li>
  <li class="even-row"><a href="/2009/team/698/index.html">TCU</a></li>
  <li><a href="/2009/team/465/index.html">UNLV</a></li>
  <li class="even-row"><a href="/2009/team/732/index.html">Utah</a></li>
  <li><a href="/2009/team/811/index.html">Wyoming</a></li>
</ul>
</div> <!-- conference -->
<div style="clear:both;"></div>
</div> <!-- conferences -->
<div class="conferences">
<div class="conference">
<h1>Pacific-10 Conference</h1>
<ul>
  <li><a href="/2009/team/29/index.html">Arizona</a></li>
  <li class="even-row"><a href="/2009/team/28/index.html">Arizona State</a></li>
  <li><a href="/2009/team/107/index.html">California</a></li>
  <li class="even-row"><a href="/2009/team/529/index.html">Oregon</a></li>
  <li><a href="/2009/team/528/index.html">Oregon State</a></li>
  <li class="even-row"><a href="/2009/team/657/index.html">USC</a></li>
  <li><a href="/2009/team/674/index.html">Stanford</a></li>
  <li class="even-row"><a href="/2009/team/110/index.html">UCLA</a></li>
  <li><a href="/2009/team/756/index.html">Washington</a></li>
  <li class="even-row"><a href="/2009/team/754/index.html">Washington State</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Southeastern Conference</h1>
<ul>
  <li><a href="/2009/team/8/index.html">Alabama</a></li>
  <li class="even-row"><a href="/2009/team/31/index.html">Arkansas</a></li>
  <li><a href="/2009/team/37/index.html">Auburn</a></li>
  <li class="even-row"><a href="/2009/team/235/index.html">Florida</a></li>
  <li><a href="/2009/team/257/index.html">Georgia</a></li>
  <li class="even-row"><a href="/2009/team/334/index.html">Kentucky</a></li>
  <li><a href="/2009/team/365/index.html">LSU</a></li>
  <li class="even-row"><a href="/2009/team/433/index.html">Mississippi</a></li>
  <li><a href="/2009/team/430/index.html">Mississippi State</a></li>
  <li class="even-row"><a href="/2009/team/648/index.html">South Carolina</a></li>
  <li><a href="/2009/team/694/index.html">Tennessee</a></li>
  <li class="even-row"><a href="/2009/team/736/index.html">Vanderbilt</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Sun Belt Conference</h1>
<ul>
  <li><a href="/2009/team/30/index.html">Arkansas State</a></li>
  <li class="even-row"><a href="/2009/team/229/index.html">Florida Atlantic</a></li>
  <li><a href="/2009/team/231/index.html">Florida International</a></li>
  <li class="even-row"><a href="/2009/team/671/index.html">Louisiana-Lafayette</a></li>
  <li><a href="/2009/team/498/index.html">Louisiana-Monroe</a></li>
  <li class="even-row"><a href="/2009/team/419/index.html">Middle Tennessee</a></li>
  <li><a href="/2009/team/497/index.html">North Texas</a></li>
  <li class="even-row"><a href="/2009/team/716/index.html">Troy</a></li>
  <li><a href="/2009/team/772/index.html">Western Kentucky</a></li>
</ul>
</div> <!-- conference -->
<div class="conference">
<h1>Western Athletic Conference</h1>
<ul>
  <li><a href="/2009/team/66/index.html">Boise State</a></li>
  <li class="even-row"><a href="/2009/team/96/index.html">Fresno State</a></li>
  <li><a href="/2009/team/277/index.html">Hawai'i</a></li>
  <li class="even-row"><a href="/2009/team/295/index.html">Idaho</a></li>
  <li><a href="/2009/team/366/index.html">Louisiana Tech</a></li>
  <li class="even-row"><a href="/2009/team/466/index.html">Nevada</a></li>
  <li><a href="/2009/team/472/index.html">New Mexico State</a></li>
  <li class="even-row"><a href="/2009/team/630/index.html">San Jose State</a></li>
  <li><a href="/2009/team/731/index.html">Utah State</a></li>
</ul>
</div> <!-- conference -->
<div style="clear:both;"></div>
</div> <!-- conferences -->
<div style="clear:both;"></div>
<div id="footer">
<p>Copyright © 2006-2020 www.cfbstats.com All rights reserved.</p>
<p><a href="/?page_id=4">Terms of Use</a></p>
<p id="timestamp">12/13/2020 20:58:21</p>
<!-- SMG_CFBStats/300x250_1a/sports/general -->
<div id="usmg_ad__general_sports_300x250_1a">
<script type='text/javascript'>
googletag.defineSlot('/7103/SMG_CFBStats/300x250_1a/sports/general', [[300,250],[300,600]], 'usmg_ad__general_sports_300x250_1a').addService(googletag.pubads());
googletag.enableServices();
googletag.display('usmg_ad__general_sports_300x250_1a');
</script>
</div>
</div> <!-- footer -->
</div> <!-- content -->
</div> <!-- wrapper -->
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-10344841-1");
pageTracker._trackPageview();
} catch(err) {}</script>
<!-- Start of ADS -->
<div id="usmg_ad__main_sports_skin">
    <script type='text/javascript'>
        //googletag.defineSlot('/7103/SMG_CFBStats/skin/sports/main', [1,1], 'usmg_ad__main_sports_skin').addService(googletag.pubads());
        //googletag.enableServices();
        //googletag.display('usmg_ad__main_sports_skin');
    </script>
</div>

<!-- SMG_CFBStats/skin/sports/general -->
<div id="usmg_ad__general_sports_skin">
    <script type='text/javascript'>
        googletag.defineSlot('/7103/SMG_CFBStats/skin/sports/general', [1,1], 'usmg_ad__general_sports_skin').addService(googletag.pubads());
        googletag.enableServices();
        googletag.display('usmg_ad__general_sports_skin');
    </script>
</div>
<br/><br/><br/><br/>
<!-- End of ADS -->
</body>
</html>"""

######################################################################################################

# import all needed modules

import requests
from bs4 import BeautifulSoup

import pandas as pd
import time

# The year below controls what year of stats the program will grab
year = "2009"
team_index_url = "http://cfbstats.com/" + year + "/team/index.html"

# Will be used to create team objects which will have attributes such as name, url, conference, record, and an attribute for each stat as well as an object for each game played.
class Teams:
    pass


# Below begins code to scrape a given url for html content

# Below is commented out while I use static html to develop
# class Scraper:
#     def soup_recipe(address):
#         url = address
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content, "html.parser")
#         Scraper.page_status(page)
#         return soup

#     def page_status(results):
#         try:
#             results.status_code  # results is the callable object requests module creates, i.e. index_page_soup
#             if results.status_code == 200:
#                 print("Connected")
#             pass
#             if results.status_code != 200:
#                 print("Page Connection Error")
#         except:
#             print("An error occured while attempting to connect to the website.")


# END Scraper Code

# BEGIN gathers urls and team names for each team from team index page

# These are the attributes I'm building so that I can use these later to assign them to team object attributes
teams_by_conf = []
conf_names = []
team_names = []
team_urls = []

# Uncomment the below line of code to GET actual web results
# team_index_soup = Scraper.soup_recipe(team_index_url)

team_index_soup = BeautifulSoup(testingSourceCode, "html.parser")
# delete the above line of code once full developed

time.sleep(0.25)

# creates a list of each conference div
conferences = team_index_soup.find_all(class_="conference")

# Adds conference names to a list
for conf in conferences:
    conf_names.append(conf.h1.string)

# Finds all a tags within conferences and compiles them into a list of lists by conference
for conf in conferences:
    teams_by_conf.append(conf.find_all("a"))

# loop through each conference and then loops through each team and appends name and url to separate lists
for conf_teams in teams_by_conf:
    for team in conf_teams:
        team_names.append(team.string)
        team_urls.append(team.get("href"))

# print(team_names)
# print(team_urls)
# print(conf_names)