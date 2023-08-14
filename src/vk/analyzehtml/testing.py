# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import vk.analyzehtml


class VkAnalyzehtmlLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=vk.analyzehtml)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "vk.analyzehtml:default")


VK_ANALYZEHTML_FIXTURE = VkAnalyzehtmlLayer()


VK_ANALYZEHTML_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VK_ANALYZEHTML_FIXTURE,),
    name="VkAnalyzehtmlLayer:IntegrationTesting",
)


VK_ANALYZEHTML_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VK_ANALYZEHTML_FIXTURE,),
    name="VkAnalyzehtmlLayer:FunctionalTesting",
)


VK_ANALYZEHTML_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        VK_ANALYZEHTML_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="VkAnalyzehtmlLayer:AcceptanceTesting",
)
