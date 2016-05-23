#!usr/bin/env python
#http://images.craigslist.org/{key}_600x450.jpg


from bs4 import BeautifulSoup #Using html5lib as engine
import re
import urllib2
import time
import json


DEFAULT_URL = "http://seoul.craigslist.co.kr/search/hhh/"
BASE_URL = "http://seoul.craigslist.co.kr"
PAGES = 1
DELAY = 0
IMAGE_FRAME = "http://images.craigslist.org/{key}_600x450.jpg"


if PAGES > 5:
    DELAY = 60




def room_link_process(room_suffix):
    #img_reg = re.compile(r"http://images.craigslist.org/(.*?)_600x450.jpg")
    img_reg = re.compile(r'"shortid":"(.*?)",')

    master_url = BASE_URL + room_suffix[0]
    url_object = urllib2.urlopen(master_url)


    soup = BeautifulSoup(url_object.read(), "html5lib")
    title = soup.findAll("span",{"id":"titletextonly"})[0].string
    user_info = soup.findAll("section",{"id":"postingbody"})
    images = img_reg.findall(soup.findAll("script",{"type":"text/javascript"})[2].string)
    images = tuple(IMAGE_FRAME.format(key = img) for img in images)
    #print soup.findAll("script",{"type":"text/javascript"})[2].string
    time.sleep(DELAY)
    user_info =  user_info[0].text
    #soup.findAll("section",{"class":"userbody"},
    return (title, str(user_info),images)
    


def scrape_craigslist_linklist(url = DEFAULT_URL):
    linklist = []
    url_object = urllib2.urlopen(url)
    url_read = url_object.read()

    soup = BeautifulSoup(url_read,"html5lib")
    chunk_holder = soup.findAll("p",{"class":"row"})

    link_tuple = (str(no_chunk.a) for no_chunk in chunk_holder)
    return link_tuple   


def crawl_cl_links():
    reg_pattern = re.compile("href=\"(.*)\"")
    links = scrape_craigslist_linklist()
    linkendings = tuple(reg_pattern.findall(suffix) for suffix in links)
    del links
    pages = tuple(room_link_process(room_page) for room_page in linkendings[0:PAGES]) #Break this open to do MORE THAN 5 pages.
    return {'first_100_links' : linkendings, #list of strings 
            'base_url': BASE_URL,  #is a string
            'pages': pages  #is a tuple
           }
    #LIMITING NUM OF PAGES TO NOT GET BLOCKED ON QUERY.  NEED A BETTER SOLUTION FOR THIS.


###AFTER THIS POINT CREATE FUNCTIONS THAT WILL BE CALLED BY THE API APP


    

def refresh():
    return crawl_cl_links()

def getAllFormat(fields_to_display):

    outer_return = {}
    counter = 1
    for info in crawl_cl_links()['pages']:
        return_dict_inner = {"title" : info[0], "user_body" : info[1], "images" : info[2]}
        outer_return["listing {index}".format(index = counter)] = return_dict_inner
        counter += 1
    
    json_struct = json.dumps(outer_return) 
    return json_struct

def runtime_manager(command = "all"):
    '''
    return com_dict[command]()
    '''
    if command = "all":
        return getAllFormat()

#print getAllFormat()
