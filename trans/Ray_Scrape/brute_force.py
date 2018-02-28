#-*- coding: utf-8 -*-
#!/bin/usr/python2.7

# Wherein we irresponsibly hit a Korean Government endpoint on a national
# holiday such that we get a bunch of info because they did not protect their
# shit.  As much fun as it would be to do this responsibly, I am a shithead
# so fuck it

import json
import csv
import requests
import time
import sqlite3
from random import choice

#Config

ENDPOINT = """http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun={gubun_type}&p_apt_code={code}&p_house_cd=1&p_acc_year={year}"""
MAX = 5000000000
YEARS = [
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018"]

GUBUN = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
         "Q","R","S","T","U","V","W","X","Y","Z"]

INTERVAL = 3 #seconds

# Functions

def getRandomUserAgent():
        headers_useragents = []
        headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
        headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
        headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')

        return choice(headers_useragents)

def buildHeader():
    header = {}
    header["User-Agent"] = getRandomUserAgent()
    return header


def buildLogString(y,c,g):
    query_str = str(y) + str(c) + str(g)
    return query_str

def buildMolitQueryString( _gubun, _code, _year):

    ENDPOINT = """http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?
    menuGubun={gubun_type}&
    p_apt_code={code}&
    p_house_cd=1&
    p_acc_year={year}"""

    return _raw_query.format(gubun_type = _gubun, code = _code, year = _year)


def createLog(_queryString, _file_name = "last_pull.log"):
    with open(_file_name,"w") as f:
        _f.write(_queryString)
        print "Logged to %s" % file_name

    return True


def placeInCSV(_data_dict):
    pass

def createJSON(_data_dict):
    pass

def makeRequest(_endpoint = ENDPOINT):
    resp = requests.get(_endpoint)
    return resp

def buildIndex():
    pass

def checkRequest(_json_str):
    try:
        info_dict = json.loads(_json_str)
        sale_list = info_dict.get("result")

        if sale_list and len(sale_list) > 0:
            return True
        else:
            return False
    except:
        #Assumes Mangled Data
        False



# Main Function

def runScrape():
    for gub in GUBUN:
        for year in YEARS:
            for i in range(MAX):
                endpoint = buildMolitQueryString(gub, i, year)
                resp = makeRequest(endpoint,headers = buildHeader())

                if checkRequest(resp.content) == True:
                    # Make Database Push
                else:
                    pass
