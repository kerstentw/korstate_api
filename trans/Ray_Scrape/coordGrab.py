#-*- coding: utf-8 -*-

import json
import requests
import traceback


"""
resp = requests.get("http://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=126.98223798126216&y=37.571113090184284", headers={"Authorization":"KakaoAK c727b85c6c8e4ec346883018dc398bbe","Origin":"http://rt.molit.go.kr","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36","Accept":"*/*","KA":"sdk/4.0.5 os/javascript lang/en-US device/MacIntel origin/http%3A%2F%2Frt.molit.go.kr"})

{"meta":{"total_count":2},"documents":[{"region_type":"B","code":"1120010200","address_name":"서울특별시 성동구 하왕십리동","region_1depth_name":"서울특별시","region_2depth_name":"성동구","region_3depth_name":"하왕십리동","region_4depth_name":"","x":127.02869871459896,"y":37.56190861105771},{"region_type":"H","code":"1123053600","address_name":"서울특별시 동대문구 용신동","region_1depth_name":"서울특별시","region_2depth_name":"동대문구","region_3depth_name":"용신동","region_4depth_name":"","x":127.03726228192635,"y":37.57580677816467}]}

"""

endpoint="http://rt.molit.go.kr/new/gis/getDongAreaMove.do?searchMinX=127.0&searchMinY=37.5&searchMaxX=129&searchMaxY=38&_=1518609630971"

coord_endpoint = "http://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={horizontal}&y={vertical}"

coord_header = {"Authorization":"KakaoAK c727b85c6c8e4ec346883018dc398bbe","Origin":"http://rt.molit.go.kr","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36","Accept":"*/*","KA":"sdk/4.0.5 os/javascript lang/en-US device/MacIntel origin/http%3A%2F%2Frt.molit.go.kr"}


with open("dumps/coords.json","w") as fil:
    resp1 = requests.get(endpoint)
    fil.write(str(resp1.content))

master_list = []

target_json = json.loads(resp1.content)

resp_list = target_json["resultList"]
try:
    for area_json in resp_list:
        print "grabbing BIGJSON::: " + str(area_json)
        for area in eval(area_json["AREA"]):
            print "grabbing area:::" + str(area)
            resp2 = requests.get(coord_endpoint.format(horizontal=area["x"],
                                               vertical = area["y"]), headers = coord_header
                        )
            print "\n\n\n\nDOCU:::" + resp2.content
            master_list.append(json.loads(resp2.content)["documents"])


    with open("dumps/code_list.py","w") as fil:
        fil.write(str(master_list))

except:
    print "exception\n\n\n"
    traceback.print_exc()
    print "\n\n\n"
    with open("dumps/code_list.py","w") as fil:
        fil.write(str(master_list))
