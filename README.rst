.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.


==============
vk.analyzehtml
==============

An Plone add-on analyzing html tags and classes used in News Items and in Documents

Features
--------

Adds a view ``@@analyze-html-view`` which lists the tags and classes used in News Items and Documents.

It ist meant
- to check if the CSS configuration is ok
- to check if the TinyMCE configuration is ok

especially for migration purposes.

It is not intended to be used in a production environment.

Usage
--------

Calling the view ``@@analyze-html-view`` on any object in the site will show you a List of tags and classes with the number of elements using the
them in the site. If you click on a tag or class you will get a list of links to the News Items and Documents using the tag or class.


Translations
------------

TODO


Installation
------------

Install vk.analyzehtml by adding it to your buildout::

TODO: put on PyPI or in collective
(((
    [buildout]

    ...

    eggs =
        vk.analyzehtml


and then running ``bin/buildout``
)))

Authors
-------

Provided by awesome people ;)


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/verena-km/vk.analyzehtml/issues
- Source Code: https://github.com/verena-km/vk.analyzehtml


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the GPLv2.
