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
import fnmatch
import logging
from pprint import pprint
from mutagen.easyid3 import EasyID3

log = logging.getLogger('musicdir')

def pattern_input(config, pattern):
    for directory in config.get('input', []):
        for root, dirs, files in os.walk(directory):
            if not len(files): continue
            for filename in fnmatch.filter(files, pattern):
                yield os.path.join(root, filename)


def audio_input(config):
    pattern = config['audio_pattern']
    return pattern_input(config, pattern)

def art_input(config):
    pattern = config['art_pattern']
    return pattern_input(config, pattern)

def template_filename(config, filename):
    info = dict(EasyID3(filename))

    for i in info:
        if isinstance(info[i], list):
            info[i] = info[i][0]

    info.update({
        'extension': os.path.splitext(filename)[1],
        'track': (
            info['tracknumber'].split('/')[0]
            if 'tracknumber' in info
            else 0
        ),
        'albumartist': (
            info.get('performer', False)
            or info.get('artist', False)
        )
    })

    return os.path.normcase(os.path.normpath(os.path.join(
        config['output'],
        unicode(config['template']).format(**info)
    )))

def ensure_directories(dirname):
    if not os.path.lexists(dirname):
        log.debug("Creating directory %s" % (dirname))
        os.makedirs(dirname)

def link(target, path):
    if os.path.exists(path):
        if not os.path.islink(path):
            log.warning("Skipping link, blocked by existing file: %s" % (path))
            return
        else:
            old = os.readlink(path)
            # TODO: normalize read link
            if old != target:
                log.info(
                    "Replacing symlink pointed at different target: %s -> %s"
                    % (old, target)
                )
                os.remove(path)
            else: return
    elif os.path.lexists(path):
        # Broken link
        log.info(
            "Replacing broken symlink: %s"
            % (path)
        )
        os.remove(path)

    os.symlink(target, path)


