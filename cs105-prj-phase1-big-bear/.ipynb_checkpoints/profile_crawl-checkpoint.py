#helpful tutorial: https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/
#created by Nikhil Gowda
import csv
from parsel import Selector
import parameters
from time import sleep
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.common.keys import Keys
import urllib
import requests
from bs4 import BeautifulSoup


city_page = open("cities.txt", "r")
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}

linkedin_urls = []
url_dict = {}

query = "site:linkedin.com/in/+"
for link in city_page:
	link = link.replace(' ', '+')
	i = 0
	URL = f"https://google.com/search?q={query+link}"
	while i < 100:
		sleep(0.5)
		resp = requests.get(URL, headers = headers)
		if resp.status_code == 200:
			soup = BeautifulSoup(resp.content, "html.parser")
		else:
			print("Response code: ", resp.status_code)
		for g in soup.find_all('div', class_= 'r'):
			anchors = g.find_all('a')
			if anchors: 
				link = anchors[0]['href']
				if url_dict.get(link) == None:
					linkedin_urls.append(link)
					url_dict[link] = True
					i = i + 1
				else:
					print("URL exists")
		anchors = soup.find_all('a', id='pnnext')
		if anchors:
			URL = f"https://google.com{anchors[0]['href']}"
		else:
			print("Can't retrieve next page")

driver = webdriver.Chrome('/mnt/c/Users/blankhil-PC/Downloads/chromedriver_win32/chromedriver.exe')

writer = csv.writer(open(parameters.file_name, 'w'))
writer.writerow(['name','followers','location','experience_count', 'education_count', 'url'])


driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_id('username')
username.send_keys(parameters.linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

log_in_button.click()
sleep(0.5)

# For loop to iterate over each URL in the list
for linkedin_url in linkedin_urls:
    
   # get the profile URL 
   driver.get(linkedin_url)

   # add a 5 second pause loading each URL
   sleep(5)

   #getting selector
   sel = Selector(text=driver.page_source)
   #getting name
   sleep(2)
   name = sel.xpath('//*[@class="inline t-24 t-black t-normal break-words"]/text()').extract_first()
   sleep(1)
   if name:
       name = name.strip()
   sleep(1)
   followers = sel.xpath('//*[@class="t-16 t-black t-normal"]/text()').extract_first()
   sleep(1)
   if followers:
       followers = followers.strip()
   sleep(1)
   location = sel.xpath('//*[@class="t-16 t-black t-normal inline-block"]/text()').extract_first()
   sleep(1)
   if location:
       location = location.strip()

   sleep(1)
   experience_count = len(sel.xpath('//*[@class="pv-entity__position-group-pager pv-profile-section__list-item ember-view"]/text()'))/2
   sleep(1)
   education_count = len(sel.xpath('//*[@class="pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view"]/text()'))
   sleep(1)

   writer.writerow([name,
                 followers,
                 location,
                 experience_count,
                 education_count, linkedin_url])

   sleep(1)
# terminates the application
driver.quit()


