#!/usr/bin/env python
import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import EchoWebSocket

cherrypy.config.update({'server.socket_port': 9000})
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()
from ws4py.websocket import WebSocket


class TheWebSocketHandler(WebSocket):
  def received_message(self, message):
     print("received:", message)




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

