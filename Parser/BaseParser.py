#!/usr/bin/env
# html parser
import BeautifulSoup
import re

class BaseParser:
	"""docstring for BaseParser"""
	def __init__(self, document):
		self.document = document

	def getTitle(self):
		soup = BeautifulSoup.BeautifulSoup(self.document)
		title = soup.html.body.find('div', {'class' : 'art_title'}).text
		return title

	def getContent(self):
		soup = BeautifulSoup.BeautifulSoup(self.document)
		content = soup.html.body.find('div', {'class' : 'art_detail'}).text
		return content
