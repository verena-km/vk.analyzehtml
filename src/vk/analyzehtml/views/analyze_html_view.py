# -*- coding: utf-8 -*-

# from vk.analyzehtml import _
from bs4 import BeautifulSoup
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IAnalyzeHtmlView(Interface):
    """Marker Interface for IAnalyzeHtmlView"""


@implementer(IAnalyzeHtmlView)
class AnalyzeHtmlView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('analyze_html_view.pt')

    def __call__(self):
        # Implement your own actions:
        # print("AnalyzeHtmlView Called")
        # results = api.content.find(portal_type='Document')
        # for result in results:
        #     print(result.Title)
        #     object = result.getObject()
        #     soup = BeautifulSoup(object.text.raw, "html.parser")
        #     for tag in soup.findAll(True):
        #         print(tag.name)
        # print(object.text.raw)
        # print(object.text.output)
        return self.index()

    def bla(self):
        return "Huhu"

    def tags_old(self):
        tag_dict = {}
        results = api.content.find(portal_type="Document")
        for result in results:
            # print(result.Title)
            # print(result.Path)
            object = result.getObject()
            soup = BeautifulSoup(object.text.raw, "html.parser")
            for tag in soup.findAll(True):
                # print(tag.name)
                if not tag.name in tag_dict.keys():
                    tag_dict[tag.name] = {result.Title}
                else:
                    tag_dict[tag.name].add(result.Title)
            print(tag_dict)

            # print(object.text.raw)
            # print(object.text.output)
        return tag_dict

    def tags(self):
        tag_dict = {}
        results = api.content.find(portal_type=["Document", "News Item"])
        for result in results:
            # print(result.Title)
            # print(result.Path)
            object = result.getObject()
            soup = BeautifulSoup(object.text.raw, "html.parser")
            for tag in soup.findAll(True):
                # print(tag.name)
                if not tag.name in tag_dict.keys():
                    tag_dict[tag.name] = {object}
                else:
                    tag_dict[tag.name].add(object)
            # print(tag_dict)

            # print(object.text.raw)
            # print(object.text.output)
        return tag_dict

    def classes(self):
        class_dict = {}
        results = api.content.find(portal_type=["Document", "News Item"])
        for result in results:
            object = result.getObject()
            soup = BeautifulSoup(object.text.raw, "html.parser")
            classes = [
                value
                for element in soup.find_all(class_=True)
                for value in element["class"]
            ]
            print(classes)

            for classname in classes:
                if not classname in class_dict.keys():
                    class_dict[classname] = {object}
                else:
                    class_dict[classname].add(object)
        return class_dict
