# coding: utf-8
import asyncio
import time
import codecs
import struct
import datetime
import serial

class EchoServerProtocol:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        nowis=0
        
        # data = data.hex()
        data = [data[i: i+4] for i in range(0, len(data), 4)]
        data[0]=data[0].hex()
        data[1]=data[1].hex()
        data[2]=data[2].hex()
        data[3]=int(data[3].hex(),16)
        data[4]=data[4].hex()
        data[5]=int(data[5].hex(),16)
        data[6]=int(data[6].hex(),16)
        data[10]=int(data[10].hex(),16)
        data[11]=data[11].hex()
        data[12]=int(data[12].hex(),16)
        data[13]=data[13].hex()
        data[14]=data[14].hex()
        data[15]=data[15].hex()
        data[11]=data[11].replace("000000","")
        data[13]=data[13].replace("000000","")
        data[14]=data[14].replace("000000","")
        data[15]=data[15].replace("000000","")
        data[255]=data[255].hex()
        data[255]=data[255].replace("000000","")
        data[255]=int(data[255],16)
        speed = str(data[255])
        speed = speed
        speed = speed.encode('utf-8')
        print('Received')
        arduino1.write(speed)
        for i in range(16):
            b=i+1
            if b == 1:
                c='   const'
            elif b == 2:
                c='location'
            elif b == 3:
                c='location'
            elif b == 4:
                c='  +speed'
            elif b == 5:
                c='    time'
            elif b == 6:
                c='bp press'
            elif b == 7:
                c='mr press'
            elif b == 8:
                c='er press'
            elif b == 9:
                c='    null'
            elif b == 10:
                c='    null'
            elif b == 11:
                c=' current'
            elif b == 12:
                c=' door is'
            elif b == 13:
                c=' +-speed'
            elif b == 14:
                c=' delta t'
            elif b == 15:
                c='br notch'
            elif b == 16:
                c='pw notch'
            

            print('%s : %s' % (c, data[i]))
            print()
            if b == 16:
                print('    speed : %s' % (speed))

loop = asyncio.get_event_loop()
arduino1 = serial.Serial('COM4',38400)
#bpsは適宜変更のこと
print("Starting UDP server")
listen = loop.create_datagram_endpoint(
    EchoServerProtocol, local_addr=('192.168.114.514', 9032))
transport, protocol = loop.run_until_complete(listen)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

transport.close()
loop.close()

