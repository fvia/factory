#!/usr/bin/env python

import pika
import time
import json 


rbconn = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
rbchannel = rbconn.channel()


def send(msg):
     rbchannel.basic_publish(
        exchange='',
        routing_key='factory_output',
        body=msg
     )
 

print("sillySender working: ", end="",flush=True) 

last_sent_time = ""
while(True):
    time.sleep(2)  
    current_time = time.strftime("%H:%M",time.localtime())    
    if(current_time != last_sent_time):
        last_sent_time= current_time
        d = {'time': current_time}
        send(json.dumps(d)) 
        print(".",end='',flush=True) 
