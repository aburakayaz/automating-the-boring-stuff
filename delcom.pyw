# USAGE delcom <command name>
import sys, os, send2trash

if len(sys.argv) > 1:
    # Get command name from command line.
    command = sys.argv[1]
else:
    # Stop the program if there is no command line argument.
    sys.exit()

os.chdir('W:\\PyBatches')

batfile_name = command + '.bat'
batfile = open(batfile_name)
line = batfile.read()
py_file_path = line.split(' ')[1]
batfile.close()

send2trash.send2trash(batfile_name)
send2trash.send2trash(py_file_path)
