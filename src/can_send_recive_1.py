#!/usr/bin/env python
import can
bus = can.interface.Bus(bustype='socketcan',channel='can0',bitrate=1000000)
msg = can.Message(arbitration_id=0X01,data=[0x00,0x11,0x22,0x33,0x44,0x55,0x66,0x77],is_extended_id=False)  
try:
    #bus.send(msg)
    bus.send_periodic(msg,1)
    print("mesage sent {}",format(bus.channel_info))
    while 1:
        message=bus.recv()
        print(message)
        print("recive",message.arbitration_id)
        if (message.arbitration_id==1):
            msg1 = can.Message(arbitration_id=0X03,data=[0x00,0x11,0x22],is_extended_id=False)  
            bus.send(msg1)
            print("again send",msg1.arbitration_id)
            print("msgs1",msg1,format(bus.channel_info))

except can.CanError:
    print("no")


