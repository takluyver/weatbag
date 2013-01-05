#!/usr/bin/env python3
from distutils.core import setup

setup(name='WEATBAG',
      version='1.0',
      description='Written by Everyone Altogether, The Big Adventure Game',
      author='Thomas Kluyver et al.',
      author_email='takowl@gmail.com',
      url='https://github.com/takluyver/weatbag',
      packages=['weatbag', 'weatbag.tiles'],
      scripts=['play-weatbag']
     )
