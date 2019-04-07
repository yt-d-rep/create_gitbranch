#!/usr/bin/env python

import json
import random


class Message():
    def default(self, username):
        text = "What's up, " + username + "?" + "\n" + \
               "If you want to know about REAL pythons, please speak to me with texts including 'real python'."
        return text

    def animalmsg(self, name, char, color, url):
        text = "Name: " + name + "\n" + \
               "Character: " + char + "\n" + \
               "Color: " + color + "\n" + \
               "url: " + url + "\n"
        return text

    def pythons(self, p_json):
        # jsonload
        p_j = open(p_json)
        p_dict = json.load(p_j)
        key_pythons = "pythons"
        # select python at random from dict
        max_int = len(p_dict[key_pythons])
        random_int = random.randrange(0, max_int)
        p_name = p_dict[key_pythons][random_int]["name"]
        p_char = p_dict[key_pythons][random_int]["character"]
        p_color = p_dict[key_pythons][random_int]["color"]
        p_url = p_dict[key_pythons][random_int]["url"]
        # return message
        return self.animalmsg(p_name, p_char, p_color, p_url)