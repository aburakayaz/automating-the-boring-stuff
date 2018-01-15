# USAGE shorter <tag> <url>
# OR: shorter <tag> - (copy url)
import sys, os, pyperclip

if len(sys.argv) > 1:
    # Get shortcut tag from command line.
    tag = sys.argv[1]
else:
    # Stop the program if there is no command line argument.
    sys.exit()

if len(sys.argv) > 2:
    # Get the url from command line.
    dest = sys.arv[2]
else:
    # Get the url from clip.
    dest = pyperclip.paste()

def web_shortcut(url):
    file_name = os.path.join('W:\\PyBatches\\web_shortcuts', tag + '.pyw')
    file = open(file_name, 'w')
    file.write('import webbrowser\n')
    file.write("webbrowser.open('" + url.strip() + "')")
    file.close()

def file_shortcut(fol):
    file_name = os.path.join('W:\\PyBatches\\folder_shortcuts', tag + '.pyw')
    file = open(file_name, 'w')
    file.write('import os\n')
    file.write("os.startfile('" + fol.strip() + "')")
    file.close()

if os.path.exists(dest):
    file_shortcut(dest)
else:
    web_shortcut(dest)
