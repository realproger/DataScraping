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

# Part 2: Transform
#  taking an array of all the instances of HTML code of the repository row.
def transform(html_repos):
    repositories_data = []
    for repo in html_repos:
        dev_element = repo.find('h1', {'class': 'h3 lh-condensed'})
        if dev_element is not None:
            devs = dev_element.text.strip().split('/')[0].strip()
        else:
            devs = 'Unknown Developer'
            
        repos_name_element = repo.find('h1', {'class': 'h3 lh-condensed'})
        if repos_name_element is not None:
            repo_name = repos_name_element.text.strip().split('/')[1].strip()
        else:
            repo_name = 'Unknown Repository Name'
            
        stars_el = repo.find('a', {'class': 'Link--muted'})
        if stars_el is not None:
            stars = stars_el.text.strip()
        else:
            stars = 'Unknown Number of Stars'
        
        repositories_data.append({'developer': devs, 'repository_name': repo_name, 'nbr_stars': stars})
    return repositories_data

# Part 3: Format
def format(repositories_data):
    csv_string = 'Developer,Repository Name,Number of Stars\n'

    for data in repositories_data:
        csv_string += f"{data['developer']},{data['repository_name']},{data['nbr_stars']}\n"

    return csv_string


# Main function to run the complete process


def get_top_trending_repositories():

    url = 'https://github.com/trending'
    page = request_github_trending(url)
    html_repos = extract(page)
    repositories_data = transform(html_repos)
    csv_data = format(repositories_data)

    return csv_data

csv_string = get_top_trending_repositories()
print(csv_string)