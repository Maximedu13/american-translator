import json
import urllib
import random
import requests
from newsapi import NewsApiClient

state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

def news():
    newsapi = NewsApiClient(api_key='395a44b33aa14aceb05cc2d718c8331b')
    gnewskey = "0c2bf6ccd5e99220130263aade4b6542"
    # /v2/top-headlines
    random_states = random.sample(state_names, 5)
    print(random_states)
    list_of_articles = []
    try:
        for query in random_states:
            this_state = query
            query = query.replace(" ", "-")
            top_headlines = newsapi.get_everything(q=query)
            list_of_articles.append(this_state.capitalize() + ": " + top_headlines["articles"][0]["description"])
    except:
        try:
            for query in random_states: 
                this_state = query
                r = requests.get("https://gnews.io/api/v4/search?q=" + query + "&lang=en&country=us&max=1" + "&token=" + gnewskey)
                r = json.loads(r.text)
                list_of_articles.append(this_state.capitalize() + ": " + r["articles"][0]["description"])
        except:
            pass
    return list_of_articles
    