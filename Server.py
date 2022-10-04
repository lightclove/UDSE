# -*- coding: utf-8 -*-
from dpa.server.Application import Application
from dpa.server.HTTPDispatcher import HTTPRequestPathDispatcher
from dpa.server.HTTPHandler import HTTPHandler
from dpa.server.Server import QueuedThreadingTCPServer
from dpa.server.XMLRPCProcessor import XMLRPCProcessor

from API import API

testService = API()
app = Application()
disp = HTTPRequestPathDispatcher()
xrp = XMLRPCProcessor()
xrp.addServiceAPI(testService, 'API')

disp.addProcessor("/test", xrp)

hh = HTTPHandler()
hh.processor = disp

serv = QueuedThreadingTCPServer(('localhost',), 12345, hh)
serv.allowReuseAddress = True
app.addServer('TEST', serv)
app.run()
