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

# I assume that this is a delay between get requests? Is it in seconds?
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

##############################################################################################################
# Source code for a team page to test without get requests
##############################################################################################################


test_team_page = """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>

<meta http-equiv="content-type" content="text/html; charset=utf-8">

<title>cfbstats.com - 2009 Boston College Eagles</title>

<link rel="stylesheet" type="text/css" href="/css/cfbstats.css">

<link rel="stylesheet" type="text/css" href="/css/leader.css">

<style type="text/css">

<!--

table.team-statistics {width: 80%;}

table.team-statistics th.statistic-name {width: 50%;}

table.team-statistics th.team-stat {width: 25%;}

table.team-statistics th.opponent-stat {width: 25%;}

table.team-schedule {width: 60%;}

table.team-schedule th.date {width: 11%;}

table.team-schedule th.opponent {width: 34%;}

table.team-schedule th.result {width: 15%;}

table.team-schedule th.game-time {width: 20%;}

table.team-schedule th.attendance {width: 20%;}

table.team-record {width: 30%;}

table.team-record th.split-name {width: 50%;}

table.team-record th.w-l-record {width: 50%;}
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

  <a href="/2009/team/index.html">2009 Teams</a>

  <span class="separator">&gt;</span>

  <span class="selected">Boston College</span>

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

<h1 id="pageTitle">2009 Boston College Eagles

through 01/07/2010</h1>

<div id="seasons">

<ul>

  <li><a href="/2020/team/67/index.html">2020</a></li>

  <li><a href="/2019/team/67/index.html">2019</a></li>

  <li><a href="/2018/team/67/index.html">2018</a></li>

  <li><a href="/2017/team/67/index.html">2017</a></li>

  <li><a href="/2016/team/67/index.html">2016</a></li>

  <li><a href="/2015/team/67/index.html">2015</a></li>

  <li><a href="/2014/team/67/index.html">2014</a></li>

  <li><a href="/2013/team/67/index.html">2013</a></li>

  <li><a href="/2012/team/67/index.html">2012</a></li>

  <li><a href="/2011/team/67/index.html">2011</a></li>

  <li><a href="/2010/team/67/index.html">2010</a></li>

  <li class="selected">2009</li>

</ul>

</div>

<div class="team-statistics">

<table class="team-statistics">

  <caption>Team Statistics</caption>
  <tr>
    <th scope="col" class="statistic-name"></th>

    <th scope="col" class="team-stat">Boston College</th>

    <th scope="col" class="opponent-stat">Opponents</th>
  </tr>
  <tr>

    <td class="statistic-name">Scoring:  Points/Game</td>

    <td>24.8</td>

    <td>19.8</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name">Scoring:  Games - Points</td>

    <td>13 - 322</td>

    <td>13 - 257</td>
  </tr>
  <tr>

    <td class="statistic-name row-group">First Downs:  Total</td>

    <td class="row-group">214</td>

    <td class="row-group">235</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name">First Downs:  Rushing - Passing - By Penalty</td>

    <td>91 - 102 - 21</td>

    <td>78 - 145 - 12</td>
  </tr>
  <tr>

    <td class="statistic-name row-group">Rushing:  Yards / Attempt</td>

    <td class="row-group">3.78</td>

    <td class="row-group">2.99</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name">Rushing:  Attempts - Yards - TD</td>

    <td>473 - 1788 - 17</td>

    <td>448 - 1340 - 11</td>
  </tr>
  <tr>

    <td class="statistic-name row-group">Passing:  Rating</td>

    <td class="row-group">117.95</td>

    <td class="row-group">118.70</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name">Passing:  Yards</td>

    <td>2423</td>

    <td>2919</td>
  </tr>
  <tr>

    <td class="statistic-name">Passing:  Attempts - Completions - Interceptions - TD</td>

    <td>350 - 176 - 18 - 21</td>

    <td>448 - 277 - 15 - 12</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">Total Offense:  Yards / Play</td>

    <td class="row-group">5.12</td>

    <td class="row-group">4.75</td>
  </tr>
  <tr>

    <td class="statistic-name">Total Offense:  Plays - Yards</td>

    <td>823 - 4211</td>

    <td>896 - 4259</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">Punt Returns:  Yards / Return</td>

    <td class="row-group">12.21</td>

    <td class="row-group">8.31</td>
  </tr>
  <tr>

    <td class="statistic-name">Punt Returns:  Returns - Yards - TD</td>

    <td>14 - 171 - 1</td>

    <td>29 - 241 - 1</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">Kickoff Returns:  Yards / Return</td>

    <td class="row-group">21.18</td>

    <td class="row-group">19.25</td>
  </tr>
  <tr>

    <td class="statistic-name">Kickoff Returns:  Returns - Yards - TD</td>

    <td>44 - 932 - 0</td>

    <td>48 - 924 - 0</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">Punting:  Yards / Punt</td>

    <td class="row-group">41.03</td>

    <td class="row-group">37.73</td>
  </tr>
  <tr>

    <td class="statistic-name">Punting:  Punts - Yards</td>

    <td>80 - 3282</td>

    <td>78 - 2943</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">Interceptions:  Returns - Yards - TD</td>

    <td class="row-group">15 - 155 - 1</td>

    <td class="row-group">18 - 323 - 3</td>
  </tr>
  <tr>

    <td class="statistic-name">Fumbles:  Number - Lost</td>

    <td>17 - 8</td>

    <td>13 - 8</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name">Penalties:  Number - Yards</td>

    <td>64 - 561</td>

    <td>80 - 724</td>
  </tr>
  <tr>

    <td class="statistic-name">Time of Possession / Game</td>

    <td>29:19.00</td>

    <td>30:41.00</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">3rd Down Conversions: Conversion %</td>

    <td class="row-group">30.23%</td>

    <td class="row-group">34.01%</td>
  </tr>
  <tr>

    <td class="statistic-name">3rd Down Conversions:  Attempts - Conversions</td>

    <td>172 - 52</td>

    <td>197 - 67</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">4th Down Conversions: Conversion %</td>

    <td class="row-group">63.64%</td>

    <td class="row-group">40%</td>
  </tr>
  <tr>

    <td class="statistic-name">4th Down Conversions:  Attempts - Conversions</td>

    <td>11 - 7</td>

    <td>20 - 8</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">Red Zone:  Success %</td>

    <td class="row-group">88.64%</td>

    <td class="row-group">77.5%</td>
  </tr>
  <tr>

    <td class="statistic-name">Red Zone:  Attempts - Scores</td>

    <td>44 - 39</td>

    <td>40 - 31</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">Field Goals:  Success %</td>

    <td class="row-group">92.9%</td>

    <td class="row-group">80%</td>
  </tr>
  <tr>

    <td class="statistic-name">Field Goals:  Attempts - Made</td>

    <td>14 - 13</td>

    <td>25 - 20</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">PAT Kicking:  Success %</td>

    <td class="row-group">97.5%</td>

    <td class="row-group">100%</td>
  </tr>
  <tr>

    <td class="statistic-name">PAT Kicking:  Attempts - Made</td>

    <td>40 - 39</td>

    <td>27 - 27</td>
  </tr>

  <tr class="even-row">

    <td class="statistic-name row-group">2-Point Conversions:  Success %</td>

    <td class="row-group">-</td>

    <td class="row-group">100%</td>
  </tr>
  <tr>

    <td class="statistic-name">2-Point Conversions:  Attempts - Made</td>
    <td>0 - 0</td>

    <td>1 - 1</td>
  </tr>

</table>

</div> <!-- team-statistics -->

<div class="team-schedule">

<table class="team-schedule">

  <caption>Team Schedule</caption>
  <tr>

    <th scope="col" class="date">Date</th>

    <th scope="col" class="opponent">Opponent</th>

    <th scope="col" class="result">Result</th>

    <th scope="col" class="game-time">Game Time</th>

    <th scope="col" class="attendance">Attendance</th>
  </tr>
  <tr>

    <td class="date">09/05/09</td>

    <td class="opponent">Northeastern</td>

    <td class="result">W 54-0</td>

    <td>2:48</td>

    <td>33,262</td>
  </tr>

  <tr class="even-row">

    <td class="date">09/12/09</td>

    <td class="opponent"><a href="/2009/team/331/index.html">Kent St.</a></td>

    <td class="result">W 34-7</td>

    <td>2:46</td>

    <td>25,165</td>
  </tr>
  <tr>

    <td class="date">09/19/09</td>

    <td class="opponent">@ 24 <a href="/2009/team/147/index.html">Clemson</a></td>

    <td class="result">L 7-25</td>

    <td>4:46</td>

    <td>77,000</td>
  </tr>

  <tr class="even-row">

    <td class="date">09/26/09</td>

    <td class="opponent"><a href="/2009/team/749/index.html">Wake Forest</a></td>

    <td class="result">W 27-24</td>

    <td>3:06</td>

    <td>40,892</td>
  </tr>
  <tr>

    <td class="date">10/03/09</td>

    <td class="opponent"><a href="/2009/team/234/index.html">Florida St.</a></td>

    <td class="result">W 28-21</td>

    <td>3:24</td>

    <td>40,029</td>
  </tr>

  <tr class="even-row">

    <td class="date">10/10/09</td>

    <td class="opponent">@ 10 <a href="/2009/team/742/index.html">Virginia Tech</a></td>

    <td class="result">L 14-48</td>

    <td>3:02</td>

    <td>66,233</td>
  </tr>
  <tr>

    <td class="date">10/17/09</td>

    <td class="opponent"><a href="/2009/team/490/index.html">North Carolina St.</a></td>

    <td class="result">W 52-20</td>

    <td>3:23</td>

    <td>35,261</td>
  </tr>

  <tr class="even-row">

    <td class="date">10/24/09</td>

    <td class="opponent">@ <a href="/2009/team/513/index.html">Notre Dame</a></td>

    <td class="result">L 16-20</td>

    <td>3:30</td>

    <td>80,795</td>
  </tr>
  <tr>

    <td class="date">10/31/09</td>

    <td class="opponent">23 <a href="/2009/team/129/index.html">Central Mich.</a></td>

    <td class="result">W 31-10</td>

    <td>2:57</td>

    <td>34,128</td>
  </tr>

  <tr class="even-row">

    <td class="date">11/14/09</td>

    <td class="opponent">@ <a href="/2009/team/746/index.html">Virginia</a></td>

    <td class="result">W 14-10</td>

    <td>3:09</td>

    <td>44,324</td>
  </tr>
  <tr>

    <td class="date">11/21/09</td>

    <td class="opponent"><a href="/2009/team/457/index.html">North Carolina</a></td>

    <td class="result">L 13-31</td>

    <td>3:10</td>

    <td>41,272</td>
  </tr>

  <tr class="even-row">

    <td class="date">11/28/09</td>

    <td class="opponent">@ <a href="/2009/team/392/index.html">Maryland</a></td>

    <td class="result">W 19-17</td>

    <td>2:59</td>

    <td>35,042</td>
  </tr>
  <tr>

    <td class="date">12/26/09</td>

    <td class="opponent">+ 22 <a href="/2009/team/657/index.html">Southern California</a></td>

    <td class="result">L 13-24</td>

    <td>3:18</td>

    <td>40,121</td>
  </tr>
  <tfoot>
    <tr>

      <td class="legend" colspan="5">@ : Away, + : Neutral Site</td>
    </tr>
  </tfoot>

</table>

</div> <!-- team-schedule -->

<div class="team-record">

<table class="team-record">

  <caption>Team Record</caption>
  <tr>

    <th scope="col" class="split-name">Split</th>

    <th scope="col" class="w-l-record">Record</th>
  </tr>
  <tr>

    <td class="split-name">All Games</td>

    <td>8-5</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">at Home</td>

    <td>6-1</td>
  </tr>
  <tr>

    <td class="split-name">on Road/Neutral Site</td>

    <td>2-4</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">vs. Conference</td>

    <td>5-3</td>
  </tr>
  <tr>

    <td class="split-name">vs. Non-Conference</td>

    <td>3-2</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">vs. Ranked (AP)</td>

    <td>1-3</td>
  </tr>
  <tr>

    <td class="split-name">vs. Unranked (AP)</td>

    <td>7-2</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">vs. FBS (I-A)</td>

    <td>7-5</td>
  </tr>
  <tr>

    <td class="split-name">vs. FCS (I-AA)</td>

    <td>1-0</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">vs. FBS Winning</td>

    <td>2-4</td>
  </tr>
  <tr>

    <td class="split-name">vs. FBS Non-Winning</td>

    <td>5-1</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">vs. BCS AQ</td>

    <td>5-5</td>
  </tr>
  <tr>

    <td class="split-name">vs. BCS non-AQ</td>

    <td>2-0</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">vs. FBS Power 5</td>

    <td>5-4</td>
  </tr>
  <tr>

    <td class="split-name">vs. FBS non-Power 5</td>

    <td>2-1</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">in August/September</td>

    <td>3-1</td>
  </tr>
  <tr>

    <td class="split-name">in October</td>

    <td>3-2</td>
  </tr>

  <tr class="even-row">

    <td class="split-name">in November</td>

    <td>2-1</td>
  </tr>
  <tr>

    <td class="split-name">in December/January</td>

    <td>0-1</td>
  </tr>

</table>

</div> <!-- team-record -->

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

<div id="leftColumn">

<div class="section">

<ul>

  <li class="selected">Team Home</li>

  <li><a href="/2009/team/67/roster.html">Roster</a></li>

  <li><a href="/2009/team/67/rushing/index.html">Rushing</a></li>

  <li><a href="/2009/team/67/passing/index.html">Passing</a></li>

  <li><a href="/2009/team/67/receiving/index.html">Receiving</a></li>

  <li><a href="/2009/team/67/puntreturn/index.html">Punt Returns</a></li>

  <li><a href="/2009/team/67/kickreturn/index.html">Kickoff Returns</a></li>

  <li><a href="/2009/team/67/punting/index.html">Punting</a></li>

  <li><a href="/2009/team/67/kickoff/index.html">Kickoffs</a></li>

  <li><a href="/2009/team/67/kicking/index.html">Place Kicking</a></li>

  <li><a href="/2009/team/67/scoring/index.html">Scoring</a></li>

  <li><a href="/2009/team/67/total/index.html">Total Offense</a></li>

  <li><a href="/2009/team/67/allpurpose/index.html">All-Purpose Running</a></li>

  <li><a href="/2009/team/67/interception/index.html">Interceptions</a></li>

  <li><a href="/2009/team/67/fumblereturn/index.html">Fumble Returns</a></li>

  <li><a href="/2009/team/67/tackle/index.html">Tackles</a></li>

  <li><a href="/2009/team/67/tackleforloss/index.html">Tackles For Loss</a></li>

  <li><a href="/2009/team/67/sack/index.html">Sacks</a></li>

  <li><a href="/2009/team/67/miscdefense/index.html">Misc. Defense</a></li>

  <li><a href="/2009/team/67/firstdown/offense/split.html">First Downs</a></li>

  <li><a href="/2009/team/67/penalty/offense/split.html">Penalties</a></li>

  <li><a href="/2009/team/67/thirddown/offense/split.html">3rd Down Conversions</a></li>

  <li><a href="/2009/team/67/fourthdown/offense/split.html">4th Down Conversions</a></li>

  <li><a href="/2009/team/67/redzone/offense/split.html">Red Zone Conversions</a></li>

  <li><a href="/2009/team/67/turnovermargin/split.html">Turnover Margin</a></li>

</ul>

</div> <!-- section -->

</div> <!-- leftColumn -->

<div id="wrapperClear"/>

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


##############################################################################################################

# Scrape stats from individual team pages
##############################################################################################################


stats = []
team_stats = []
opp_stats = []


# These are populated with the stat names and actual numbers
team_stats_dict = {}
opp_stats_dict = {}


# This will allow you to loop through each team's page and gather stats from each.
# for team_url in team_urls:
#     team_page_soup = Scraper.soup_recipe(team_url)
#     time.sleep(0.25)


# Delete below line of code when using GET requests
team_page_soup = BeautifulSoup(test_team_page, "html.parser")


# finds the statistics table
stats_table = team_page_soup.find("table", class_="team-statistics")


# find all rows
table_rows = stats_table.find_all("tr")

# The first row in useless for this program and is removed below
table_rows.pop(0)

# loops through each row and names each stat while separating team stats from opponent stats to a different list. .strip is removing whitespace at the beginning and end of strings. Would like to use float to convert strings to numbers, but can't because time of possession won't convert to a number.
for tr in table_rows:
    cell1 = tr.find("td")
    cell1_split = cell1.text.split("-")
    for c in cell1_split:
        stats.append(c.strip())

    cell2 = cell1.find_next()
    cell2_text = cell2.text

    if cell2_text == "-":
        cell2_text = "0"
    cell2_split = cell2_text.split("-")

    for c in cell2_split:
        team_stats.append(c.strip())

    cell3 = cell2.find_next()
    cell3_text = cell3.text

    if cell3_text == "-":
        cell3_text = "0"
    cell3_split = cell3_text.split("-")

    for c in cell3_split:
        opp_stats.append(c.strip())

for stat, team_stat in zip(stats, team_stats):
    team_stats_dict[stat] = team_stat

for stat, opp_stat in zip(stats, opp_stats):
    opp_stats_dict[stat] = opp_stat

print(team_stats_dict)
print(opp_stats_dict)