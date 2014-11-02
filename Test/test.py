#!/usr/bin/env python2.7
# program file demonstration
import CapturePage
import HtmlParser

capturePage = CapturePage.CapturePage('http://yfsw.org/index.php/Index/detail/id/85')
document = capturePage.downloadPage()
htmlParser = HtmlParser.HtmlParser(document)
title = htmlParser.getTitle()
content = htmlParser.getContent()
print title+content
