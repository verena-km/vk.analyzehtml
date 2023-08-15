# -*- coding: utf-8 -*-

# from vk.analyzehtml import _
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
        return self.index()
