import pyperclip

values = pyperclip.paste()
arr = values.split('\n')
tup = ()

for it in arr:
    a = it.split(':'
    # (0, 0) is for being able to update the tuple properly
    tup += ((a[0].strip(), a[1].strip()), (0, 0))

pyperclip.copy(str(tup[::2]))
