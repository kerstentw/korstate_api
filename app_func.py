#!/bin/python2.7
# Date: 20 May 2016 - ongoing
# Py version: python2.7
# TARGET STRING: {"images":['https://d33gsw7jcnaxas.cloudfront.net/512/032e6b0b-f23e-4510-a57e-863c0fd72081', 'https://d33gsw7jcnaxas.cloudfront.net/512/032e6b0b-f23e-4510-a57e-863c0fd72081']}

# TO DO: Set this up into a linear functional implementation

#http://www.dabangapp.com/room/56ca7a1a79c4b721990b1f15

from bs4 import BeautifulSoup
import re
import urllib2
import sys

preview = False
resolution = "512"

'''
target_url = "http://www.dabangapp.com/room/56ca7a1a79c4b721990b1f15"
'''
#TO DO: Build a canvas refresh for if CDN changes URL.
# TO DO: GET request determines the dabang app with a try/except

def refresh_frame():
    '''
    This function refreshes the cdn of the target, compatibility is based
    on implmentation.
    '''

    pass



def scrape_dabang(target_url = "http://www.dabangapp.com/room/5719edbd40a0b05fbb9bc734"):

    '''
    This function takes a target url that is related to dabang (must end with room)
    and then returns a dictionary with the images.  Can go into 'preview mode'
    as well if fed the argument.  
    '''

    canvas_frame = "https://d33gsw7jcnaxas.cloudfront.net/{res}/{key}"   #use .format(key = 'key_string')
    my_url = urllib2.urlopen(target_url)
    html_string = my_url.read()

    BS_Obj = BeautifulSoup(html_string, "html.parser")

    for string_rep in BS_Obj.strings:
        if "dabang.web.detail" in string_rep:
            html_string = string_rep

        # Add additional filters here.

    re_pattern = re.compile(r'"photo":\[(.*?)\]')

    tuple_of_dictionaries = eval(re_pattern.findall(html_string)[0])

    image_dict =  {"images":[canvas_frame.format(res = resolution, 
                   key = entry['key']) for entry in tuple_of_dictionaries]}

    if preview == True:
        return_list = list()
        for img_link in image_dict['images']:
            return_list.append('<img src = "%s"></img><br><h2>%s</h2><br>' % (img_link,img_link))
         
        return unicode(' '.join(return_list))  
    else:
        return image_dict
