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

You might like to check out some of these other projects.

  - Beets
  - Beetfs
  - id3fs
