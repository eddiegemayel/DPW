#Eddie
#lecture
#may 19 2014
import webapp2
from page import *
#import json , for json file
from xml.dom import minidom #library for working with xml in python
import urllib2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.form_header = "Yahoo Weather App"
        self.response.write(view.print_out())


        if self.request.GET:
            code = self.request.GET["code"]
            url = "http://xml.weather.yahoo.com/forecastrss?p=" + code
            #go get the api info
            req = urllib2.Request(url)
            opener = urllib2.build_opener()
            data = opener.open(req)

            #parse it
            xmldoc = minidom.parse(data)


            #look at elements within the xml
            self.response.write(xmldoc.getElementsByTagName("title")[2].firstChild.nodeValue+ "<br/>")

            list = xmldoc.getElementsByTagName("yweather:forecast")
            #content = "<br/>"
            for item in list:
                c = item.attributes["day"].value
                c += "  High of " + item.attributes["high"].value
                c += "  Low of " + item.attributes["low"].value
                c += "<img width='30' src='images/"+ item.attributes['code'].value +".png' />"
                c+= "<br/>"
                self.response.write(c)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)