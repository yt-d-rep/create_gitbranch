#!/usr/bin/env python

import urllib.request
from urllib.parse import urljoin
import random
from bs4 import BeautifulSoup

class ReptileSearch:
    
    def __init__(self):
        self.base_url = "http://reptile-database.reptarium.cz"

    # search word and return result html
    def search_word(self, url, word):
        values = {
            "search": word,
            "submit": "Search"
        }
        params = urllib.parse.urlencode(values)
        url = url + "/search" + "?" + params
        response = urllib.request.urlopen(url)
        data = response.read()
        html = data.decode("utf-8")
        return html

    # get search result and return the list of results
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

    # select the word by random index number generated within list length
    def select_at_random_from_list(self, l):
        max_int = len(l)
        random_int = random.randrange(0, max_int)
        return l[random_int]

    # get content from the result page
    def get_result_detail(self, base_url, href):
        url = urljoin(base_url, href)
        response = urllib.request.urlopen(url)
        data = response.read()
        html = data.decode("utf-8")

        soup = BeautifulSoup(html, "html.parser")
        # get name
        name_content = soup.select_one("#content > h1")
        name = name_content.em.string

        # get common_name
        common_name_content = soup.select_one("table.species > tr:nth-of-type(3) > td:nth-of-type(2)")
        common_name = common_name_content.text
        if common_name_content.text == None:
            common_name = "no common name"
        else:
            if "\xa0" in common_name:
                common_name = common_name.replace(u"\xa0", u"")
                if common_name == None:
                    common_name = "no common name"
            if "G: " in common_name:
                common_name = common_name.split("G: ")[0]
            if "E: " in common_name:
                common_name = common_name.replace(u"E: ", u"")
        
        return name, common_name, url

    def reptile_search(self, url, word):
        html = self.search_word(url, word)
        result_list = self.get_content_from_html(html)
        selected_result = self.select_at_random_from_list(result_list)
        detail_list = self.get_result_detail(self.base_url, selected_result)
        return detail_list

def main(word):
    RS = ReptileSearch()
    return RS.reptile_search(RS.base_url, word)

if __name__ == "__main__":
    print(main("python"))