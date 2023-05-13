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

# Part 1: Extract
def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    repos_list = soup.find_all('article', {'class' : 'Box-row'})

    return repos_list