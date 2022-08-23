#https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())