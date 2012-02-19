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

import os
import os.path
import logging
import fnmatch
from pprint import pprint

import ConfigParser

import musicdir.actions

log = logging.getLogger('musicdir')

class Application:
    """ The main musicdir application

    This class reads musicdir configuration files, merges configuration
    passed in from the command line, and runs action methods """

    parser = None
    config = {}

    def __init__(self, parser = None):
        if parser is None:
            parser = ConfigParser.SafeConfigParser()
            parser.readfp(open(os.path.join(os.path.dirname(__file__), 'data/defaults.cfg')))
            parser.read(['/etc/musicdir.cfg',
                os.path.expanduser('~/.musicdir.cfg')])
        self.parser = parser
        self.updateConfig()

    def getConfigParser(self):
        return self.parser

    def setArgumentNamespace(self, ns):
        """ Merges arguments from argparse into the self.parser
            configparser """
        arguments = vars(ns)

        for (key, value) in arguments.items():
            if value:
                if key == 'input':
                    i = 0
                    for directory in value:
                        self.parser.set('input', 'cli' + str(i), directory)
                        i = i + 1
                else:
                    self.parser.set('general', key, str(value))

        self.updateConfig()

    def updateConfig(self):
        self.config = {
            key: value for (key, value) in self.parser.items('general')
        }
        for key in ['output']:
            self.config[key] = os.path.expanduser(self.config.get(key))
        self.config['input'] = [
            os.path.expanduser(value)
            for (key, value)
            in self.parser.items('input')
        ]
        self.setupLogging()

    def setupLogging(self):
        verbose = int(self.config.get('verbose', 0))
        if verbose > 1:
            log.setLevel(logging.DEBUG)
        elif verbose > 0:
            log.setLevel(logging.INFO)
        else:
            log.setLevel(logging.WARNING)

    def validateConfig(self):
        log.debug(self.config)

        if not self.config.get('input'):
            raise "No inputs specified"
        if not self.config.get('output'):
            raise "No output specified"

    def executeAction(self, action):
        log.info("Executing %s action" % (action))
        method = getattr(musicdir.actions, action)
        method(self.config)

    def execute(self):
        self.validateConfig()
        self.executeAction(self.config['action'])
