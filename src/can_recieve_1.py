#!/usr/bin/env python
import can
bus = can.interface.Bus(bustype='socketcan',channel='can0',bitrate=1000000)
while 1:
    message=bus.recv()
    print("orginal message data",message)
    print(message.arbitration_id)
    mess1=message.data
    print("message data",mess1)
    value =mess1.decode()
    print("data",value)
    
