import json
import pyperclip

values = pyperclip.paste()
arr = values.split('\n')
di = {}

for it in arr:
    a = it.split(':')
    di.update({a[0].strip(): a[1].strip()})

js = json.loads(json.dumps(di))

pyperclip.copy(str(js))
