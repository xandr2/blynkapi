#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
#

from urllib2 import Request, urlopen, HTTPError, URLError
import json

class Blynk(object):
	"""Class for simple use blynk API

	Attributes:
		server: A string representing the customer's name.
		token: A string project token hash
		protocol: A string http or https
		port: A string server port
		pin: A string pin number (default = None)
		value: A string value for API requests (default = None)
	"""

	def __init__(self, token, **kwargs):
		"""Return a Customer object whose name is *name*.""" 
		self.token = token
		self.server = kwargs.get('server', 'blynk-cloud.com')
		self.protocol = kwargs.get('protocol', 'http')
		self.port = kwargs.get('port', '8080')
		self.pin = kwargs.get('pin', None)
		self.value = kwargs.get('value', None)
		self.headers = {
		  'Content-Type': 'application/json'
		}
		self.val_on = '["1"]'
		self.val_off = '["0"]'
		self.to = None
		self.title = None
		self.subj = None

	def on(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/pin/"+self.pin, data=self.val_on, headers=self.headers)
		request.get_method = lambda: 'PUT'
		return self.__check(request)

	def off(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/pin/"+self.pin, data=self.val_off, headers=self.headers)
		request.get_method = lambda: 'PUT'
		return self.__check(request)

	def set_val(self, value):
		#value = "[\""+value+"\"]"
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/update/"+self.pin, data=str(value), headers=self.headers)
		request.get_method = lambda: 'PUT'
		return self.__check(request)

	def set_val_old(self, value):
		#value = "[\""+value+"\"]"
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/pin/"+self.pin, data=str(value), headers=self.headers)
		request.get_method = lambda: 'PUT'
		return self.__check(request)

	def get_val(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/pin/"+self.pin)
		return self.__check(request)

	def push(self, value):
		self.value = { "body" : value }
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/notify", data=json.dumps(self.value), headers=self.headers)
		return self.__check(request)

	def email(self, to, title, subj):
		self.value = { "to" : str(to), "title" : str(title), "subj" : str(subj) }
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/email", data=json.dumps(self.value), headers=self.headers)
		return self.__check(request)

	def hw_status(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/isHardwareConnected")
		return self.__check(request)

	def app_status(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/isAppConnected")
		return self.__check(request)

	def history(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/data/"+self.pin)
		return self.__check(request)

	def qr(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/qr")
		return self.__check(request)

	def get_project(self):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/project")
		return self.__check(request)

	def query_api(self, groupBy, aggregation, pin, value):
		request = Request(self.protocol+"://"+self.server+":"+self.port+"/"+self.token+"/query?groupBy="+str(groupBy)+"&aggregation="+str(aggregation)+"&pin="+str(pin)+"&value="+str(value))
		return self.__check(request)

	def __check(self, request):
		try:
			response_body = urlopen(request).read()
			if len(response_body) == 0:
				result = "Done."
			else:
				result = json.loads(response_body)
		except HTTPError, e:
			result = 'HTTPError code = ' + str(e.code) + ' HTTPError msg = ' + str(e.msg)
		except URLError, e:
			result = 'URLError = ' + str(e)	
		return result







