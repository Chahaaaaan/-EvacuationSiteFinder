#-*- coding: utf-8 -*-
from math import pi
from math import tanh
from math import sin
from math import asin
from math import sqrt
from numpy import arctanh
import requests
import json
import base64
import os
from datetime import datetime
def tile2latlon(x, y, z):
    L = 85.05112878
    lon = ((x / 2.0**(z+7) )-1) * 180
    lat = 180/pi * (asin(tanh(-pi/2**(z+7)*y + arctanh(sin(pi/180*L)))))
    return [lat, lon]

def latlon2tile2(lat, lon, z):
    L = 85.05112878
    x = int((lon/180 + 1) * 2**(z+7))
    y = int( (2**(z+7) / pi * ( -arctanh(sin(pi*lat/180)) + arctanh(sin(pi*L/180)) ) ))
    return [x, y]
geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
geo_data = requests.get(geo_request_url).json()
z = 10
pix = 256
print('現在地の座標を入力してください')
x = input()
y = input()
print('調べる災害の数字を入力してください。洪水:1　崖崩れ、土石流及び地滑り:2 高潮:3 地震:4 津波:5 大規模な火事:6 内水氾濫:7 火山現象:8')
datype=input()
a,b = latlon2tile2(x, y, z)
placeToGo ='http://cyberjapandata.gsi.go.jp/xyz/skhb0{0}/{1}/{2:d}/{3:d}.geojson'.format(datype,z,a/pix,b/pix)
places = requests.get(placeToGo)
data = places.json()

placename = ''
distance = 9999999999999999999
ansx = 0
ansy=0
for i in data['features']:
    placex = i['geometry']['coordinates'][1]
    placey = i['geometry']['coordinates'][0]
    tmpdistance=sqrt((x-placex)**2+(y-placey)**2)
    if (tmpdistance < distance):
        distance = tmpdistance
        placename = i['properties']['name']
        ansx = placex
        ansy=placey
print(placename)
print(x, y)
print(ansx,ansy)
#{u'geometry': {u'type': u'Point', u'coordinates': [137.1318640578, 35.333353740384]}, u'type': u'Feature', u'properties': {u'disaster6': 1, u'disaster4': 1, u'name': u'\u5e02\u5f79\u6240\u99d0\u8eca\u5834', u'address': u'\u5c90\u961c\u770c\u591a\u6cbb\u898b\u5e02\u65e5\u30ce\u51fa\u753a1-60-1'}}