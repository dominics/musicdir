<!--- vim: set tw=79 sw=4 ts=4 et : -->
# Musicdir

A quick Python script I'm throwing together to aid in reorganising directories
of MP3s.

## Dependencies

 - Python 2.7+
 - Mutagen version 1.10.1 or above
     - In Ubuntu/Debian, provided by python-mutagen package
 - argparse
     - In Ubuntu/Debian, provided by python-argparse package

## Getting Started in Debian/Ubuntu

First, install from source using the distutils setup.py:

```
# apt-get install python2.7 python-argparse python-mutagen
$ git clone git://github.com/dominics/musicdir.git
$ cd musicdir
# python setup.py install
```

This should put musicdir in /usr/local/bin. Use `musicdir --help` to get
information about the available subcommands.

## Contact

Dominic Scheirlinck <dominic@varspool.com>

http://github.com/dominics/musicdir

## Similar Projects

Mostly, musicdir differs in its symlink approach, which means it never writes
to the input files or changes their tags. This makes musicdir nice for dealing
with rsynced input directories.

  - [Beets](http://code.google.com/p/beets/)
      - Actually, musicdir works just fine with a beets-based tagging workflow
      - Once [this enhancement](http://code.google.com/p/beets/issues/detail?id=64)
         is completed, it might replace musicdir
  - [Beetfs](http://code.google.com/p/beetfs/)
  - [id3fs](http://erislabs.net/ianb/projects/id3fs/)
  - [pytagfs](http://www.pytagsfs.org/)
      - Great, based on mutagent, and widely available
      - Doesn't persist metadata, so it scans all music on startup
