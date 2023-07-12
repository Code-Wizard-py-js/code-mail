from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import base64
import time
import os,glob
import subprocess
import json
import time
import base64
import uuid,re,csv
import codecs,random
ls=os.getcwd()
import sqlite3
from sqlite3 import Error
import urllib.parse

getmac=uuid.getnode()
mainid=str(getmac)
import subprocess

import requests






class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
       
        self.send_header( "Access-Control-Allow-Origin", "*")
        self.end_headers()
        #self.wfile.write( bytes(json.dumps( answ ), 'utf-8'))
        self.send_header('Content-type', 'application/json')
        #self.end_headers()
        

    def do_GET(self):
        
        
        data=self.path
        
            
        if "software" in str(data):
            
            response={
                'result': 'success', 'email': True, 'active': True, 'uuid': True, 'password': True, 'login': True, 'date': True, 'user_id': 611, 'message': 'Successfully logged in. Your expiry date is 2026-07-15.'
            }
            self._set_headers()
            
            self.wfile.write(json.dumps(response).encode('utf-8'))
      
        else:
            response={
                'result': 'success', 'email': True, 'active': True, 'uuid': True, 'password': True, 'login': True, 'date': True, 'user_id': 611, 'message': 'Successfully logged in. Your expiry date is 2026-07-15.'
            }
            self._set_headers()
            
            self.wfile.write(json.dumps(response).encode('utf-8'))

def run():
   
        port = 8080
    # print('Listening on localhost:%s' % port)
        server = HTTPServer(('', port), RequestHandler)
        os.system("cls")
        
        server.serve_forever()
    
        
run()

