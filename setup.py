# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join

name = 'dolmen.relations'
version = '2.0a4'

readme = open(join('src', 'dolmen', 'relations', 'README.txt')).read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'cromlech.container',
    'dolmen.container',
    'grokcore.component',
    'setuptools',
    'zc.relation >= 1.0',
    'zope.component',
    'zope.event',
    'zope.i18n',
    'zope.i18nmessageid',
    'zope.interface',
    'zope.intid',
    'zope.lifecycleevent',
    'zope.location',
    'zope.schema',
    ]

tests_require = [
    'ZODB3 >= 3.9.1',
    'cromlech.configuration',
    'pytest',
    'transaction',
    'zope.keyreference',
    ]

setup(name=name,
      version=version,
      description='Dolmen relations',
      long_description=readme + '\n\n' + history,
      keywords='Grok Cromlech Dolmen Relations',
      author='The Dolmen team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://gitweb.dolmen-project.org',
      download_url='',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['dolmen'],
      include_package_data=True,
      platforms='Any',
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
      )
