#!/usr/bin/env python

# -----------------Import Modules----------------- #

import random

# local modules
from . import reptile_search
from . import google_image_search

# -----------------Classes----------------- #

class Message():

    # Generate default message
    def default(self, username):
        text = "What's up, " + username + "?" + "\n" + \
               "If you want to know about pythons, please speak to me with texts including \"real python\"."
        
        return text

    # Get target reptile information and return list of those(ZooLogicalName, CommonName, URL, ImageURL, ImageSize).
    def get_reptile_info(self, word):
        # get name,pageurl
        RS = reptile_search.ReptileSearch()
        l = RS.reptile_search(word)
        zl_name = l[0]
        common_name = l[1]
        url = l[2]
        # get image metadata
        GIS = google_image_search.GoogleImageSearch()
        image_metadata = GIS.get_first_image_meta(zl_name)
        # get image_url
        image_url = image_metadata["image_url"]
        # get image size for posting message
        size_l = self.adjust_size(image_metadata["width"], image_metadata["height"])
        image_size = "=%dx%d" % (size_l[0], size_l[1])
        return zl_name, common_name, url, image_url, image_size

    # Return width and height value
    def adjust_size(self, width, height):
        # multi from 0.9 to 0.1
        ref = 200
        adjust_w = width
        adjust_h = height
        # If width or height of the image is lower than 100px, not adjusted 
        if adjust_w < 100 or adjust_h < 100:
            return adjust_w, adjust_h
        # If width of the image is over 300px, width is adjusted to 300px-100px
        for i in [i/10 for i in range(1, 10)[::-1]]:
            if abs(ref - adjust_w) <= 100:
                break
            else:
                adjust_w = int(width * i)
                adjust_h = int(height * i)
    
        return adjust_w, adjust_h

    # Generate infomation message from get_reptile_info  
    def animalmsg(self, word):
        info_list = self.get_reptile_info(word)
        text = ""
        if info_list[0] != None:
            text += "ZooLogicalName: " + "**" + info_list[0] + "**" +"\n"
        if info_list[1] != None:
            text += "CommonName: " + "**" + info_list[1] + "**" + "\n"
        if info_list[2] != None:
            text += "PageURL: " + info_list[2] + "\n"
        if info_list[3] != None:
            text += "![Image](%s %s \"%s\")" % (info_list[3], info_list[4], info_list[3])
        
        return text

# -----------------Main Functions----------------- #

def main(word):
    MSG = Message()
    return MSG.get_reptile_info(word)

if __name__ == "__main__":
    print(main("python"))