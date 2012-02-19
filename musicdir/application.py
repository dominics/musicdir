#!/usr/bin/env python
# vim: set ts=4 sw=4 tw=79 et :
#
# Copyright 2012 Dominic Scheirlinck <dominic@varspool.com>
#
# This file is part of Musicdir.
#
# Musicdir is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# Musicdir (see COPYING).  If not, see <http://www.gnu.org/licenses/>.
#
# See README.md for usage.

import os
import os.path
import fnmatch
from mutagen.easyid3 import EasyID3
import ConfigParser
from pprint import pprint


class Application:
    parser = None
    arguments = None
    action = None

    def __init__(self, parser = None):
        if parser is None:
            parser = ConfigParser.SafeConfigParser()
            parser.readfp(open('defaults.cfg'))
            parser.read(['/etc/musicdir.cfg',
                os.path.expanduser('~/.musicdir.cfg')])
        self.parser = parser

    def getConfigParser(self):
        return self.parser

    def setArgumentNamespace(self, ns):
        self.arguments = vars(ns)

        for (key, value) in self.arguments.items():
            if key == 'input' and value:
                i = 0
                for directory in value:
                    self.parser.set('input', 'cli' + str(i), directory)
                    i = i + 1
            else:
                self.parser.set('general', key, str(value))

    def executeAction(self):
        print "Executing ", self.action
        pprint(self.parser.items('general'))
        pprint(self.parser.items('input'))


# A set of music directories (musicdir should never write to these)
home = os.environ['HOME']
sources = [
            os.path.join(home, 'Music/dagger'),
          #  os.path.join(home, 'Music/iphone')
          ]


# Output directory
root = os.path.join(home, 'Music/indexed')

# Input patterns
audio_pattern = '*.mp3'
image_pattern = '*.jpg'

# Output patterns
if os.path.supports_unicode_filenames:
    template = unicode("{artist}/{album}/{track} - {title}{extension}")
else:
    template = "{artist}/{album}/{track} - {title}{extension}"
