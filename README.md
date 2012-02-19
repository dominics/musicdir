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

Check example.musicdir.cfg for an example config file. You should move this
file to ~/.musicdir.cfg or /etc/musicdir.cfg. Configuration options specified
in files will be used as defaults, but they may be overriden on the command
line.

The command line interface works like this:

```
usage: musicdir [-h] [--version] [--output OUTPUT] [--input INPUT] [--verbose]
                [--quiet]
                action ...

Tool for mirroring ID3-tagged music with renamed symlinks

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --output OUTPUT, -o OUTPUT
                        The output directory where symlinks will be created
  --input INPUT, -i INPUT
                        An optional directory that contains source music, if
                        not provided, your config file settings will be used.
  --verbose, -v         Be louder (can be supplied multiple times)
  --quiet, -q           Be quiet (don't output anything, overide verbose in
                        config files)

Valid actions:
  action
    update              Updates the output directory
    config              Prints the current configuration
```

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
