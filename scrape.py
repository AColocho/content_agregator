from bs4 import BeautifulSoup
import requests as r

class ESPN:
    def get_website(self,url):
        return r.get(url).text

    def get_top_news(self):
        x = self.get_website('https://www.espn.com')

        soup = BeautifulSoup(x,'html.parser')
        col_three = soup.find('section',class_='col-three')
        top_stories = col_three.find('ul',class_='headlineStack__list').find_all('a')

        story_data = {}
        for story in top_stories:
            story_data.update({story.text:'https://www.espn.com'+story['href']})
        
        return story_data

