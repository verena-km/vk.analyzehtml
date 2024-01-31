# -*- coding: utf-8 -*-

# from vk.analyzehtml import _
from bs4 import BeautifulSoup
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IAnalyzeHtmlView(Interface):
    """Marker Interface for IAnalyzeHtmlView"""


@implementer(IAnalyzeHtmlView)
class AnalyzeHtmlView(BrowserView):

    def __call__(self):
        return self.index()

    def tags(self):
        tag_dict = {}
        results = api.content.find(portal_type=["Document", "News Item"])
        for result in results:
            object = result.getObject()
            if object.text: # es muss text haben
                soup = BeautifulSoup(object.text.raw, "html.parser")
                for tag in soup.findAll(True):

                    if not tag.name in tag_dict.keys():
                        tag_dict[tag.name] = {object}
                    else:
                        tag_dict[tag.name].add(object)

        return tag_dict

    def classes(self):
        class_dict = {}
        results = api.content.find(portal_type=["Document", "News Item"])
        for result in results:
            object = result.getObject()
            if object.text: # es muss text haben
                soup = BeautifulSoup(object.text.raw, "html.parser")
                classes = [
                    value
                    for element in soup.find_all(class_=True)
                    for value in element["class"]
                ]

                for classname in classes:
                    if not classname in class_dict.keys():
                        class_dict[classname] = {object}
                    else:
                        class_dict[classname].add(object)
        return class_dict
