import csv
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs 
from time import sleep
import pandas as pd




def connect(identifiant, password,path,url):
    driver = webdriver.Chrome(path)
        #get the linkedin url
    driver.get('https://www.linkedin.com/')

        #send your identifiant into the login zone
    username_input = driver.find_element_by_name('session_key')
    username_input.send_keys(identifiant)

        #send your password into the password zone
    password_input = driver.find_element_by_name('session_password')
    password_input.send_keys(password)
    
        # click on the sign in button
        # we're finding Sign in text button as it seems this element is seldom to be changed
    driver.find_element_by_class_name('sign-in-form__submit-button').click()



    # visit each profile in linkedin and grab detail we want to get
    for i in url:
        driver.get(i)
        sleep(1.5)

        try:
                
            #find name:
            name = driver.find_element_by_class_name('pv-top-card--list').text #scrap the name for add it in the customize message
            name = name.split('\n')[0]
            name = name.rsplit(' ', 1)[0]
                #Add a Note
            driver.find_element_by_class_name('pv-s-profile-actions').click()  
            sleep(1.5)
            driver.find_element_by_xpath("//span[text()='Ajouter une note']").click()
            sleep(1.5)

            message = "Hello" + " " + name + ",\nJe suis chargé d'études pour la French Tech Toulouse. J'ai ajouté ta startup dans notre base de données, ça te dirait de compléter sa fiche ? Voici le lien : https://airtable.com/shrVyjCYiYkch9vn8\nCes informations permettront de te proposer comme solution à nos partenaires"
            #you can change easily the message but be carafull that the lenght respect the linkedin restriction
            
            elementID = driver.find_element_by_id('custom-message')
            elementID.send_keys(message)
            sleep(1.5)
            driver.find_element_by_css_selector("button[aria-label='Envoyer maintenant']").click();

            
        except:
            pass

    
