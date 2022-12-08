from bs4 import BeautifulSoup
import requests

url="https://www.lyricsfreak.com/p/passenger/"

req= requests.get(url)
soup= BeautifulSoup(req.content,"lxml")

songContainer= soup.find("div",class_="lf-list__container js-sort-table-container")

songNames= songContainer.find_all("div",class_="lf-list__cell lf-list__title lf-list__cell--full")


for count,song in enumerate(songNames):
   newUrl= "https://www.lyricsfreak.com"+song.find("a",class_="lf-link lf-link--primary")['href']  
   newreq=requests.get(newUrl)
   newSoup= BeautifulSoup(newreq.content,"lxml")
   lyrics= newSoup.find(id="content").get_text().strip().split()
   rememberedWords=["you","three","lungs","four"]

   if all(word in lyrics for word in rememberedWords):
        print("Hey Hey Hey It seems like I found")
        print("Looks Like I have found all the words in the following link")
        print(newUrl)
        print("Enjoyyyyyy")
        exit()

   else:
        pass
   lyrics.clear()
   