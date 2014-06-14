# Cleanse the "../" directory of the following:
#     - all files with a .pyc extension.
#     - all "trash files" listed below:
#         . parsetab.py - generated by the PLY module.

import os


extensions = ('.pyc',)
trashFiles = ('parsetab.py',)

print 'Changing to root directory...'
os.chdir('../')

print 'Scanning for garbage files...'


def delete(filepath):
    print "Removing '{0}'...".format(filepath)
    os.unlink(filepath)


for root, folders, files in os.walk('.'):
    for filename in files:
        filepath = os.path.join(root, filename)
        if os.path.splitext(filename)[1] in extensions:
            delete(filepath)
        elif filename in trashFiles:
            delete(filepath)

print 'Done.'
os.system('pause')
