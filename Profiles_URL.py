from googlesearch import search   
import pandas as pd

path='/usr/local/bin/chromedriver'
doc_path='/Users/thomasclement/Desktop/startups_demarchage.csv'
new_startups = pd.read_csv('/Users/thomasclement/Desktop/startups-dem.csv', sep=";", keep_default_na=False)
new_startups = new_startups[new_startups != ""]
startups = new_startups['startups:'].to_list()
url = []
profil_url=[]
result = []

def search_link():
        # to search 
    for startup in startups:        
        query = "site:linkedin.com/in 'CEO' OR 'Co-fondateur' OR 'Fondateur' " + startup #query for google to search

        for j in search(query, tld="co.in", num=1, stop=1, pause=5):
            url.append(j)
        
        print(url)
   
def uniform(url): ###because of the "fr." or "uk." it's impossible make a generic URL for the profiles contact's informations
    for link in url :
        link = link.replace('fr.linkedin.com', 'linkedin.com')
        link = link.replace('uk.linkedin.com', 'linkedin.com')
        profil_url.append(link)

    print(profil_url)

    

search_link() #start the function
