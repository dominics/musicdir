<!--- vim: set tw=79 sw=4 ts=4 et : -->
# Musicdir

Musicdir uses the existing ID3 tags on your music files to produce a sylinked
mirror directory. Musicdir doesn't touch your original music files in any way.
This is useful for dealing with iDevices that mangle filenames, and directories
of music incrementally rsycned from elsewhere.

Because the output directory is static information stored in your filesystem,
the tag metadata is only read to produce the symlinks - on update, not every
time you want to use or access the music. Disk usage is minimal.

In short, it turns this:

```
$ tree ~/Music/iphone
.
├── F00
│   ├── AAXG.mp3
│   ├── ... and 180 other badly named files
│   └── ZRSJ.mp3
├── ... and fifty other directories exactly the same
└── F49
```

into this:

```
$ tree ~/Music/awesome
.
├── Arcade Fire
│   └── Neon Bible
│       ├── 1 - Black Mirror.mp3 -> ~/Music/iphone/F02/AXCH.mp3
│       ├── 2 - Keep the Car Running.mp3 -> ~/iphone/F36/DGOH.mp3
│       └── [...etc...]
├── Augie March
│   └── Moo, You Bloody Choir
│       ├── 1 - Moo, You Bloody Choir.mp3 -> ~/Music/iphone/F13/FMCL.mp3
│       ├── 2 - Victoria's Secrets.mp3 -> ~/Music/iphone/F36/DGOH.mp3
│       └── [...etc...]
├── Ben Folds
├── Blam Blam Blam
└── [...etc...]
```

with a simple `musicdir update --input=~/Music/iphone --output=~/Music/awesome`

## Dependencies

 - Python 2.7+
 - Mutagen version 1.10.1 or above
 - argparse
 - A filesystem that supports os.symlink

Mutagen is in PyPI (pip install mutagen). Argparse, from 2.7, is in the
Python standard library.

### Ubuntu/Debian

```
# apt-get install python2.7 python-argparse python-mutagen
```

### Mac/OS X

```
# port install python27 py27-mutagen
```

## Getting Started

First, install from source using the distutils setup.py:

```
# apt-get install python2.7 python-argparse python-mutagen
$ git clone git://github.com/dominics/musicdir.git
$ cd musicdir
# python setup.py install
```

This should put musicdir in /usr/local/bin. Use `musicdir --help` to get
information about the available subcommands.

Check [example.musicdir.cfg](https://github.com/dominics/musicdir/blob/master/example.musicdir.cfg)
for an example config file. You should move this file to ~/.musicdir.cfg or
/etc/musicdir.cfg. Configuration options specified in files will be used as
defaults, but they may be overriden on the command line.

The command line interface works like this:

```
$ musicdir --help
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
      - Great, based on Mutagen, and widely available
      - Doesn't persist metadata, so it scans all music on startup
