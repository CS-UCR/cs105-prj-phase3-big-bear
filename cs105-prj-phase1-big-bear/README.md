# LinkedIn Web Crawler
### Created by Nikhil Gowda (Educational Use only)

After difficulty avoiding getting banned/IP-blocked trying to web crawl LinkedIn, I figured I can not simply ping and parse using urllib/beauitfulsoup.
I do use urllib + beauitful soup for my first initial crawl of linkedin user profiles given a  list of cities specified in "cities.txt". I then created a second
crawler to crawl the actual linkedin profiles. For this we must use a chrome web driver such as that offered by Sellenium. Using this, we can still capture linkedin data slowly but accurately. 
To accomplish this task, I also used 'xpath' on page sources captured by the web driver. 
Currently I capture (cleaning such as removing white space and handling non-strings) 5 attributes: name (name of LinkedIn user), followers (number of followers), 
location (city, state), experience_count (counts how many experience items exist), education_count (counts how many education items exist), and linkedin_url 
(url connected to LinkedIn profile). Adding more attributes is a simple task. Total amount of web pages crawled is in the few hundred. 

## Deliverables
profile_crawl.py (handles the actual crawling of web pages and parsing out outputting to a 'csv' file)  

parameters.py (handles miscellanious fields such as username/password for linkedin (avoids getting banned immediately))  

cities.txt (holds important cities that are interesting which will be used for cross-state web crawling)  

linkedin_profiles.csv (holds a sample of linkedin profiles with attributes)  

## Usage
After installing modules such as Sellenium (and Chrome if not existent), Parsel, and setting 'webdriver.Chrome(*your path*)' properly:

sample:  

python3 profile_crawl.py  

cat linkedin_profiles.csv


## Notes
You can change 'cities.txt' to include any cities you like seperated by a newline. My crawler will scrape profiles for that given city and then parse each individual profile. 


