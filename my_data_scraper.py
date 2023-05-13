######
###
##
from bs4 import BeautifulSoup
import requests
import csv
##
###
######


#Part 0: Request
def request_github_trending(url):
    res = requests.get(url)
    return res.text