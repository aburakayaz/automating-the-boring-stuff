#! python3
# mcb save <keyword> - Saves the current clipboard.
# mcb <keyboard> - Loads the corresponding save to the clipboard.
# mcb list - Loads all keywords to the clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
	
if len(sys.argv) == 3:
	command = sys.argv[1].lower()
	if command == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	elif command == 'remove':
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	else:
		pyperclip.copy('Keyword not found')

mcbShelf.close()
