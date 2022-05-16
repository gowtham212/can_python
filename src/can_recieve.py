#!/usr/bin/env python
import can
bus = can.interface.Bus(bustype='socketcan',channel='can0',bitrate=1000000)
while 1:
    message=bus.recv()
    print(message)
