#!/bin/python2.7
# Date: 20 May 2016 - ongoing
# Py version: python2.7
# TARGET STRING: {"images":['https://d33gsw7jcnaxas.cloudfront.net/512/032e6b0b-f23e-4510-a57e-863c0fd72081', 'https://d33gsw7jcnaxas.cloudfront.net/512/032e6b0b-f23e-4510-a57e-863c0fd72081']}

# TO DO: Set this up into a linear functional implementation

#http://www.dabangapp.com/room/56ca7a1a79c4b721990b1f15

from bs4 import BeautifulSoup
import re
import urllib2

write_to_debug = True
resolution = "512"

'''
target_url = "http://www.dabangapp.com/room/56ca7a1a79c4b721990b1f15"
'''

# TO DO: GET request determines the dabang app with a try/except
target_url = "http://www.dabangapp.com/room/5719edbd40a0b05fbb9bc734"


#TO DO: Build a canvas refresh for if CDN changes URL.


canvas_frame = "https://d33gsw7jcnaxas.cloudfront.net/{res}/{key}"   #use .format(key = 'key_string')


my_url = urllib2.urlopen(target_url)

BS_Obj = BeautifulSoup(html_string, "html.parser")

for string_rep in BS_Obj.strings:
    if "dabang.web.detail" in string_rep:
        html_string = string_rep

    else:
        html_string = my_url.read()

#print html_string

re_pattern = re.compile(r'"photo":\[(.*?)\]')

tuple_of_dictionaries = eval(re_pattern.findall(html_string)[0])
image_dict =  {"images":[canvas_frame.format(res = resolution, key = entry['key']) for entry in tuple_of_dictionaries]}


if write_to_debug == True:
    
    with open("imgcheck.html","w+") as test_file:
        for img_link in image_dict['images']:
            test_file.write( "<img src = %s></img>" % img_link)


