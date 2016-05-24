#!/usr/bin/env python
import urllib
import re
import json
from bs4 import BeautifulSoup

ROOT_URL = "http://www.nicebang.com{suffix}"
PAGES = 1

if 1 > PAGES > 100:
    PAGES = 1



def get_references(num_to_return,my_url = "http://www.nicebang.com"):
    read_url = urllib.urlopen("http://www.nicebang.com").read()
    bs_obj = BeautifulSoup(read_url,"html5lib")

    nums = tuple(suffix["data-id"] for suffix in bs_obj.body.div.findAll("div",{"class":"view_product"}))

    return nums[0:num_to_return]



def parse_page(ending):
    '''
    This returns a dictionary.
    '''
    page_frame = "http://www.nicebang.com/product/view/{suffix}".format(suffix = ending)  #Formats for suffix
    read_url = urllib.urlopen(page_frame).read()
    bs_obj = BeautifulSoup(read_url,"html5lib")
    
    # BACKTRACK
    url_backtrack = page_frame #For the sake of readibility or any further processing
        
    # IMAGES
    image_parse = bs_obj.body.findAll("img",{"class":"rsTmb"})
    images = tuple(ROOT_URL.format(suffix = img["src"]) for img in image_parse)
    
    # TITLE
    title = bs_obj.h3.string

    # INFO TABLE
    info_raw = bs_obj.findAll("table", {"class":"border-table"})
    keys = tuple(label.string for label in info_raw[0].findAll("th") )
    values = tuple(label.string for label in info_raw[0].findAll("td"))
    kv_pairs = zip(keys,values)
    info_dict = dict(kv_pairs)

    # USERINFO
    descrip = bs_obj.body.findAll("div",{"class":"property_content_inner"})[0].text
    

    # LAT/LONG (UNFINISHED)
    my_reg = re.compile(r'\"[0-9]+.[0-9]+\"')
    lat_long = my_reg.findall(str(bs_obj.body))
    lat_long = [float(ll.replace("\"","")) for ll in lat_long[0:2]]
    
    return_dict = {
        "URL" : url_backtrack,
        "title" : title,
        "images" : images,
        "info_table": info_dict,
        "description" : info_dict,
        "lat/long" : lat_long
    }

    
    return return_dict



def returnAll():
    '''
        Factory Function for the entire scraper.
        Returns all dictionaries in a list
    '''
    counter = 0
    return_list = []


    for ref in get_references(PAGES):
        return_list.append(parse_page(ref))

    return {"listings": return_list}

#endings = get_references()

def return_as_json(house_dict):
    return json.dumps(house_dict)
    

#returnAll()

TEST_REF = 10178
parse_page(TEST_REF)


