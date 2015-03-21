#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Javier V. Gómez'

import SimpleHTTPServer
import BaseHTTPServer
import socket
import thread
import webbrowser


def load_url(path):
    port = 8000
    httpd = StoppableHTTPServer(("127.0.0.1", port), SimpleHTTPServer.SimpleHTTPRequestHandler)
    thread.start_new_thread(httpd.serve, ())
    webbrowser.open_new('http://localhost:{0}/{1}'.format(port, path))
    raw_input("Press <RETURN> to stop server\n")
    httpd.stop()


class StoppableHTTPServer(BaseHTTPServer.HTTPServer):

    def server_bind(self):
        BaseHTTPServer.HTTPServer.server_bind(self)
        self.socket.settimeout(1)
        self.run = True

    def get_request(self):
        while self.run:
            try:
                sock, addr = self.socket.accept()
                sock.settimeout(None)
                return sock, addr
            except socket.timeout:
                pass

    def stop(self):
        self.run = False

    def serve(self):
        while self.run:
            self.handle_request()