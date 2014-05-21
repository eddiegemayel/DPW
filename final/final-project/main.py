#Eddie
#final project
#may 19 2014
import webapp2
from page import *
#import json , for json file
from xml.dom import minidom #library for working with xml in python
import urllib2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.form_header = "Trailers"
        view.title = "Movie trailers"
        self.response.write(view.print_out())


        if self.request.GET:
            code = self.request.GET["code"]
            url = "http://api.traileraddict.com/?film=" + code
            #go get the api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)

            #parse it
            xmldoc = minidom.parse(data)


            #look at elements within the xml
            self.response.write(xmldoc.getElementsByTagName("title"))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)