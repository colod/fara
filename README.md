#Foreign Influence

This project is the data-entry and scraping scripts that generate an API and will power a Foreign Influence Explorer website. See the front-facing app [here](https://github.com/sunlightlabs/bulgogi).

Foreign Influence Explorer documents some of the ways foreign entities influence U.S. policy and opinions. The two main datasets are the Department of Justice's Foreign Agent Registration Act(FARA) and press releases from The Defense Security Cooperation Agency(DSCA) records. 

##FARA Records

The management command create_feed, in the fara_feed app, scrapes the PDFs from the DOJ. Web forms in the FaraData app create pages for people to normalize the data according to instructions. The project uses a sql database. The data can be accesses through the API and RSS feeds. 

##DSCA Records

The arms_sales app scrapes press releases from the DSCA for proposed arms sales. These sales are purposed and may not happen, but these documents can add context to some of the lobbying that is visible in the FARA dataset. 


##Hacking

To set up this project to scrape FARA feeds locally:

1. Create a virtual environment (specify python2.7)
2. In your virtual environment, run pip install -r requirements.txt
3. In fara_feed/management/commands/ add an empty file called __init__.pyc
4. In fara/ create the file local_settings.py
5. Add the following to local_settings.py:
    a) SECRET_KEY="something"
    b) ES_CONFIG={}
6. If mysql is not installed, install it
7. Create a mysql database called FaraData.
8. Run python manage.py syncdb
9. Run python manage.py migrate
10. Run python manage.py create_feed

---

This is project is under construction. If you are interested in contributing in some way email Lindsay at lyoung@sunlightfoundation.com