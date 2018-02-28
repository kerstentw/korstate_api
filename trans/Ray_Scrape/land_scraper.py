#!/bin/python2.7

import os
import sys
import json
import requests
import csv_handler #From Local

"""
# http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun=F&p_apt_code=1500058656&p_house_cd=1&p_acc_year=2016&areaCode=&priceCode=

# First Seek out Apartment Lists
# Second Comb through Years
# Third Save data to Database

FORM {
menuGubun:E
srhType:
srhYear:2018
srhLastYear:2017
gubunCode:LAND
sidoCode:11
gugunCode:11170
danjiName:
roadCode:
roadBun1:
roadBun2:
dongCode:1117012200
rentAmtType:3
}
"""



SEARCH_ENDPOINT = "http://123.141.115.52/new/gis/getDanjiComboAjax.do"

BUILDING_CODES = {
    "seoul" : "25000"


}

APT_ENDPOINT = "http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun={menu_gubun}&p_apt_code={apt_code}&p_house_cd={p_house_cd}&p_acc_year={acc_year}&areaCode={area_code}&priceCode={price_code}"

