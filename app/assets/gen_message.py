#!/usr/bin/env python

import random

from . import reptile_search


class Message():
    def default(self, username):
        text = "What's up, " + username + "?" + "\n" + \
               "If you want to know about pythons, please speak to me with texts including \"real python\"."
        return text

    def animalmsg(self, zl_name, common_name, url):
        text = "ZooLogicalName: " + zl_name + "\n" + \
               "CommonName: " + common_name + "\n" + \
               "PageURL: " + url + "\n"
        return text

    def get_reptile_info(self, word):
        RS = reptile_search.ReptileSearch()
        l = RS.reptile_search(RS.base_url, word)
        zl_name = l[0]
        common_name = l[1]
        url = l[2]
        return self.animalmsg(zl_name, common_name, url)

def main(word):
    MSG = Message()
    return MSG.get_reptile_info(word)

if __name__ == "__main__":
    print(main("python"))