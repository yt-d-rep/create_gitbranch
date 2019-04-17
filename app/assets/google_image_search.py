#!/usr/bin/env python

# -----------------Import Modules----------------- #

import json
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# -----------------Classes----------------- #

class GoogleImageSearch:

    def __init__(self):
        self.base_url = "https://www.google.com/search"
        self.values = {
            "q": "searchword",
            "source": "lnms",
            "tbm": "isch"
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

    # Search image on Google and return the metadata dictionary of the first image of result    
    def get_first_image_meta(self, word):
        # Get html
        self.values["q"] = word
        params = urllib.parse.urlencode(self.values)
        url = self.base_url + "?" + params
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # Parse html
        soup = BeautifulSoup(html, "html.parser")
        elements = soup.select(".rg_meta.notranslate")
        j_dict = json.loads(elements[0].text)
        # Extract image meta data for message
        meta_dict = {
            "image_url": j_dict["ou"],
            "width": j_dict["ow"],
            "height": j_dict["oh"]
        }

        return meta_dict

# -----------------Main Functions----------------- #

def main(word):
    GIS = GoogleImageSearch()
    print(GIS.get_first_image_meta(word))

if __name__ == "__main__":
    word = "Python bivittatus"
    main(word)
