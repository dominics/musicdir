#!/usr/bin/env python

import sys
from distutils.core import setup

if sys.version < '2.7':
    print "musicdir requires Python 2.7+"
    sys.exit(1)

setup(
        name             = 'musicdir',
        version          = '0.0.1',
        description      = 'Symlink-mirrors directories of tagged music',
        long_description = open('README.md').read(),
        author           = 'Dominic Scheirlinck',
        author_email     = 'dominic@varspool.com',
        url              = 'http://github.com/dominics/musicdir',
        packages         = ['musicdir'],
        package_data     = {'musicdir': ['data/*.cfg']},
        scripts          = ['scripts/musicdir'],
        requires         = ['mutagen (>=1.10.1)', 'argparse', 'ConfigParser']
     )
