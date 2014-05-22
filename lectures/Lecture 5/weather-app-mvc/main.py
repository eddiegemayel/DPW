#Eddie
#lecture 6
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

        if self.request.GET:
            code = self.request.GET["code"]
            w_model = WeatherModel() #creates instance of the model
            w_model.code = self.request.GET["code"]
            w_model.send_req()

            w_view = WeatherView()

            w_view.wdo = w_model.wdo # transfers wdo from model to the view

            w_view.update()

            view.page_content = w_view.content



            #look at elements within the xml
            #self.response.write(xmldoc.getElementsByTagName("title")[2].firstChild.nodeValue+ "<br/>")

            # list = xmldoc.getElementsByTagName("yweather:forecast")
            # #content = "<br/>"
            # for item in list:
            #     c = item.attributes["day"].value
            #     c += "  High of " + item.attributes["high"].value
            #     c += "  Low of " + item.attributes["low"].value
            #     c += "<img width='30' src='images/"+ item.attributes['code'].value +".png' />"
            #     c+= "<br/>"
            #     self.response.write(c)
        self.response.write(view.print_out())

class WeatherModel(object):
    """ this class handles data requests
    """
    def __init__(self):
        self.url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.full_url = ""
        self.__code = ""

    def send_req(self):
        self.full_url = self.url + self.__code
        req = urllib2.Request(self.full_url)
        opener = urllib2.build_opener()
        data = opener.open(req)
        #parse it
        xmldoc = minidom.parse(data)
        #find tags we want..and put it into instance of weather data object
        self.__wdo = WeatherDataObject() #create instance of data object class
        condition = xmldoc.getElementsByTagName("yweather:condition")
        self.__wdo.condition = condition[0].attributes["text"].value
        self.__wdo.temp = condition[0].attributes["temp"].value
        self.__wdo.code = condition[0].attributes["code"].value
        loc = xmldoc.getElementsByTagName("yweather:location")
        self.__wdo.location = loc[0].attributes["city"].value
        print self.__wdo.location


#     """Nodes:
#         nested tags (aka tag pairs) - firstChild
#         standalone tag - no firstChild needed
# """

    #dont want anyone overwriting data object im making it a property
    #with just the getter
    @property
    def wdo(self):
        return self.__wdo

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, c):
        self.__code = c

class WeatherDataObject(object):
    """
    this holds info sent in by the api
    """

    def __init__(self):
        self.location = ""
        self.temp = ""
        self.condition = ""
        self.code = 0  #this code is the weather code

class WeatherView(object):
    #just showing weather info from the api
    def __init__(self):
        self.wdo = WeatherDataObject()
        self.content = ""

    def update(self):
        self.content = '''
        <div>
            <h3>{self.wdo.location}</h3>
            <ul>
                <li><strong>Temperature:</strong> {self.wdo.temp}</li>
                <li><strong>Conditions:</strong> {self.wdo.condition}</li>
            </ul>
        </div>

        '''
        self.content = self.content.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)