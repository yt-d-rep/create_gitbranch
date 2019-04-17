#!/usr/bin/env python

# -----------------Import Modules----------------- #

import urllib.request
from urllib.parse import urljoin
import random
from bs4 import BeautifulSoup

# -----------------Classes----------------- #

class ReptileSearch:
    
    def __init__(self):
        self.base_url = "http://reptile-database.reptarium.cz"

    # Search word and return result html
    def search_word(self, word):
        values = {
            "search": word,
            "submit": "Search"
        }
        params = urllib.parse.urlencode(values)
        url = self.base_url + "/search" + "?" + params
        response = urllib.request.urlopen(url)
        data = response.read()
        html = data.decode("utf-8")

        return html

    # Parse html and return the list of href elements
    def get_content_from_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        content = soup.select("#content > ul:nth-of-type(2) > li")
        href_list = []
        for li in content:
            a = li.a
            href = a.attrs["href"]
            if href != None:
                href_list.append(href)

        return href_list

    # Return the word of the random index number generated within the list length
    def select_at_random_from_list(self, l):
        max_int = len(l)
        random_int = random.randrange(0, max_int)
        
        return l[random_int]

    # Get information(ZooLogicalName, CommonName, PageURL) from the result page
    def get_result_detail(self, href):
        url = urljoin(self.base_url, href)
        response = urllib.request.urlopen(url)
        data = response.read()
        html = data.decode("utf-8")

        # Parse html
        soup = BeautifulSoup(html, "html.parser")
        # Get name
        name_content = soup.select_one("#content > h1")
        name = name_content.em.string
        # Get common_name
        common_name_content = soup.select_one("table.species > tr:nth-of-type(3) > td:nth-of-type(2)")
        common_name = common_name_content.text
        if common_name_content.text == None:
            common_name = "no common name"
        else:
            if "\xa0" in common_name:
                common_name = common_name.replace(u"\xa0", u"")
                if common_name == None:
                    common_name = "no common name"
            # Get only English common_name
            if "G: " in common_name:
                common_name = common_name.split("G: ")[0]
            if "E: " in common_name:
                common_name = common_name.replace(u"E: ", u"")
        
        return name, common_name, url

    # Search word and return target information list.
    def reptile_search(self, word):
        html = self.search_word(word)
        result_list = self.get_content_from_html(html)
        selected_result = self.select_at_random_from_list(result_list)
        detail_list = self.get_result_detail(selected_result)
        
        return detail_list

# -----------------Main functions----------------- #

def main(word):
    RS = ReptileSearch()
    return RS.reptile_search(word)

if __name__ == "__main__":
    word = "python"
    print(main(word))