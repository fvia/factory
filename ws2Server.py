#!/usr/bin/env python
import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import EchoWebSocket

import threading
import time
import pika

ElsWebSockets = []

def EhTots(msg):
    for x in ElsWebSockets:
        x.send(msg)     

def llegeixCua():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()
    def callback(ch, method, properties, body):
        print (" [x] Received %r" % (body,),flush=True)
        EhTots(body )  
    channel.basic_consume(callback,
                      queue='factory_output',
                      no_ack=True)

    channel.start_consuming()



threading.Thread(target=llegeixCua).start()

def vesContant():
    i = 0;
    while(True):
      time.sleep(10)
      i=i+1 
      if(i>9):
          i =0
      print("({})".format(i),end='',flush=True)

threading.Thread(target=vesContant).start()


cherrypy.config.update({'server.socket_port': 9000})
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()
from ws4py.websocket import WebSocket


class TheWebSocketHandler(WebSocket):
  def received_message(self, message):
     print("received:", message)
     self.send(";-)"+ str(message) ) 

  def opened(self):
     ElsWebSockets.append(self)
     print("opened")
     

  def closed(self,code,reason):
     ElsWebSockets.remove(self)
     print("closed" )
 

class Root(object):
    @cherrypy.expose
    def index(self):
        return 'some HTML with a websocket javascript connection'

    @cherrypy.expose
    def ws(self):
        print("Hoola", self.__dict__)
        # you can access the class instance through
        handler = cherrypy.request.ws_handler
cherrypy.quickstart(
    Root(), 
    '/', 
    config={
        '/ws': {'tools.websocket.on': True,
                 'tools.websocket.handler_cls': TheWebSocketHandler
               }
           }
)

