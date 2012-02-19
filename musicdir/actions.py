def cleanup():
    """ Cleans up the output directory by removing symlinks not output on this
    run. Real files are skipped. """
    print "Cleaning up: ", root
#    for r, dirs, files in os.walk(root):
#        print dirs
#        print files
#        print r

def index_audio(filename):
    substitute = {};

    audio = EasyID3(filename)
    substitute.update(audio)

    for i in substitute:
        if isinstance(substitute[i], list):
            substitute[i] = substitute[i][0]

     substitute.update({
        'extension': os.path.splitext(filename)[1],
        'track': (
                    substitute['tracknumber'].split('/')[0]
                    if 'tracknumber' in substitute
                    else 0
                 )
    })

    result = template.format(**substitute)
    result = os.path.normcase(os.path.normpath(os.path.join(root, result)))

    # Create directories
    directory = os.path.dirname(result)
    if not os.path.lexists(directory):
        print "Creating: ", directory
        os.makedirs(directory)

    # Create link
    if os.path.lexists(result):
        if os.path.islink(result):
            os.remove(result)
        else
            Pass
            # FIXME

    os.symlink(filename, result)

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

index()
cleanup()
