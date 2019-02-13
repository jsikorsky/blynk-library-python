"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.

  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app

This example shows how to use advanced functions of Blynk library:
- debug logging
- custom server
- changing heartbeat
- connected/disconnected events
"""

from __future__ import print_function
import BlynkLib

BLYNK_AUTH = 'YourAuthToken'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH,
                       server='my-server.com', # set server address
                       port=9442,              # set server port
                       heartbeat=30,           # set heartbeat to 30 secs
                       log=print               # use print function for debug logging
                       )

@blynk.ON("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.ON("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')

while True:
    blynk.run()
