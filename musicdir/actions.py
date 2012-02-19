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

import logging
from musicdir import util
from pprint import pprint
import os.path

log = logging.getLogger('musicdir')

def cleanup(config):
    """ Cleans up the output directory by removing symlinks not output on this
    run. Real files are skipped. """
    print "Cleaning up: ", root
#    for r, dirs, files in os.walk(root):
#        print dirs
#        print files
#        print r

def update(config):
    print "Updating output dirs"

    for filename in util.audio_input(config):
        new = util.template_filename(config, filename)
        util.ensure_directories(os.path.dirname(new))
        util.link(filename, new)

        log.debug("Linking %s to %s" % (new, filename))

def config(config):
    pprint(config)

## Old code below

def index_audio(filename):

    return directory

def index_image(filename, destination):
    result = os.path.join(destination, os.path.basename(filename))
    if not os.path.exists(result):
        os.symlink(filename, result)

def index():
    for source in sources:
        print "Reindexing: ", source
        for r, dirs, files in os.walk(source):
            if len(files) == 0:
                continue

            destination = None
            for f in fnmatch.filter(files, audio_pattern):
                destination = index_audio(os.path.join(r, f))
            for f in fnmatch.filter(files, image_pattern):
                index_image(os.path.join(r, f), destination)

