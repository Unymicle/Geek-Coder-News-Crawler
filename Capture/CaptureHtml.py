#!/usr/bin/env
# capture html document from Internet website

import urllib2

class CaptureHtml:
	"""docstring for CaptureHtml"""
	def __init__(self, url):
		self.url = url

	def downloadPage(self):
		con = urllib2.urlopen(self.url)
		document = con.read()
		return document
