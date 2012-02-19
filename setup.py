#!/usr/bin/env python

import sys
from distutils.core import setup
import musicdir

if sys.version < '2.7':
    print "musicdir requires Python 2.7+"
    sys.exit(1)

setup(
        name             = 'musicdir',
        version          = musicdir.version,
        description      = 'Symlink-mirrors directories of tagged music',
        long_description = open('README.md').read(),
        author           = 'Dominic Scheirlinck',
        author_email     = 'dominic@varspool.com',
        url              = 'http://github.com/dominics/musicdir',
        license          = 'GNU General Public License (GPL) 3+',
        packages         = ['musicdir'],
        package_data     = {'musicdir': ['data/*.cfg']},
        scripts          = ['scripts/musicdir'],
        requires         = ['mutagen (>=1.10.1)', 'argparse', 'ConfigParser'],
        classifiers      = [
            'Environment :: Console',
            'Development Status :: 4 - Beta',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Topic :: Multimedia :: Sound/Audio :: Conversion',
        ]
     )
