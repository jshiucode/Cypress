"""
Main Gordian file; runs at localhost:8080

"""
from graph_creator import create_graph, get_crossings_for_links, get_edges, get_crossings_for_knots
from fundamental_set_cycles import find_fund_set
from all_cycles import find_all_cycles
from helpers import dictify_cycles
from links import find_links
from knots import find_knots


from links import listify_cycles
from links import find_links
from functools import cached_property
from urllib.parse import parse_qsl, urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import http.server
from http.cookies import SimpleCookie
import numpy as np
import time

"""
Full integration of all other files
"""
def Gordian(graph_filepath):
    if graph_filepath != 'favicon.ico':
        start_time = time.time()
        print("================ Graph_filepath ================ ", graph_filepath)
        graph  = create_graph("./Graph data files/" + graph_filepath)
        graph_edges = get_edges("./Graph data files/" + graph_filepath)
        crossing_data_for_links = get_crossings_for_links("./Graph data files/" + graph_filepath, graph)
        crossing_data_for_knots = get_crossings_for_knots("./Graph data files/" + graph_filepath)
        fundamental_set_cycles = find_fund_set(graph, graph_edges)
        all_cycles = find_all_cycles(dictify_cycles(fundamental_set_cycles))
        links = find_links(all_cycles, crossing_data_for_links)

        # FOR WHEN KNOT FUNCTION IS MADE:
        # knots = find_knots(all_cycles, crossing_data_for_knots, crossing_data_for_links)

        end_time = time.time()
        elapsed_time = end_time - start_time

        return links, elapsed_time
        # return {links: knots}    , then integrate as key/values into html

"""
HTTPServer Handler
"""
class handler(BaseHTTPRequestHandler):
    @cached_property
    def url(self):
        return urlparse(self.path)

    @cached_property
    def query_data(self):
        return dict(parse_qsl(self.url.query))

    @cached_property
    def post_data(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    @cached_property
    def form_data(self):
        return dict(parse_qsl(self.post_data.decode("utf-8")))

    @cached_property
    def cookies(self):
        return SimpleCookie(self.headers.get("Cookie"))

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>Gordian 2.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>Input graph data file as path in URL. (ex: localhost:9090/k7.txt) </p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed file: %s</p>" % self.path[1:], "utf-8"))

        graph_filepath = self.path[1:]
        links, elapsed_time = Gordian(graph_filepath)
        for link in links:
            self.wfile.write(bytes("<p>%s</p>" %str(link), "utf-8"))

        # for knot in knots:
        #     self.wfile.write(bytes("<p>%s</p>" %str(knot), "utf-8"))

        self.wfile.write(bytes('There are: ' + str(len(links)) + ' links', "utf-8"))
        self.wfile.write(bytes('<p>Time taken to run algorithm ' + str(elapsed_time) + '</p>', "utf-8"))        
        # self.wfile.write(bytes('There are: ' + str(len(knots)) + ' links', "utf-8"))



"""
Server executiion
"""
host = 'localhost'
port = 8080
try:
    server = http.server.HTTPServer((host, port), handler)
    print('Started server. Running Gordian 2')
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    server.socket.close()
