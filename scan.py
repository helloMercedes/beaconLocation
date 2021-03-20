#!/usr/bin/env python
from bluepy.btle import Scanner
from operator import itemgetter
 
scanner = Scanner()
devices = scanner.scan(2.0)
#print(devices) 

list = []

for device in devices:
    print("DEV = {} RSSI = {}".format(device.addr, device.rssi))
    list.append((device.addr.encode("ascii"), device.rssi))

#print(list)

nearestDevs = sorted(list, key=itemgetter(1), reverse=True)
print(nearestDevs)

map = {
    "7f:3f:d1:b1:f1:0a": "fette AMG",
    "39:b1:cf:55:44:de": "history section"
 }

nearestKnown = "undetermined"
for dev in nearestDevs:
    print(map.get(dev[0]))
    if map.get(dev[0]) is not None:
        nearestKnown = dev
        break

print("My nearest known beacon is: "+nearestKnown[0]+" with strength: "+str(nearestKnown[1])+" located: "+map.get(nearestKnown[0]))
print("I'm probably here: "+str(map.get(nearestDevs[0][0])))
