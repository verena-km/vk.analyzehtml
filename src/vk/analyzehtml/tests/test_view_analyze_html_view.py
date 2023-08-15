# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from vk.analyzehtml.testing import VK_ANALYZEHTML_FUNCTIONAL_TESTING
from vk.analyzehtml.testing import VK_ANALYZEHTML_INTEGRATION_TESTING
from vk.analyzehtml.views.analyze_html_view import IAnalyzeHtmlView
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = VK_ANALYZEHTML_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Document", "front-page")

    def test_analyze_html_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST), name="analyze-html-view"
        )
        self.assertTrue(IAnalyzeHtmlView.providedBy(view))

    def test_analyze_html_view_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal["front-page"], self.portal.REQUEST),
                name="analyze-html-view",
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = IAnalyzeHtmlView.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):

    layer = VK_ANALYZEHTML_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
