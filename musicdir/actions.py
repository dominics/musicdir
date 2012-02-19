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
    None

def update(config):
    mapping = {}

    log.info("Updating audio links")
    for filename in util.audio_input(config):
        filename_dir = os.path.dirname(filename)
        new = util.audio_filename(config, filename)
        new_dir = os.path.dirname(new)

        util.ensure_directories(new_dir)
        util.link(filename, new)

        # Keep a mapping to provide %{audio_dir} to art_template
        if filename_dir not in mapping:
            mapping[filename_dir] = new_dir

    log.info("Updating art links")
    for filename in util.art_input(config):
        new = util.art_filename(config, filename, mapping)
        new_dir = os.path.dirname(new)

        util.ensure_directories(new_dir)
        util.link(filename, new)

    log.info("Ensured %d links in place" % (util.get_link_count()))


def config(config):
    pprint(config)
