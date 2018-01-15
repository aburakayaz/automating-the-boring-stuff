# Automating The Boring Stuff
My python scripts that I use for automating the boring stuff.

## Disclaimer
I'm not a professional python developer. I created these while I'm learning python and I thought they might be useful for others as well.
I use Windows and I didn't consider other operating systems too much while creating the scripts, they are just a bunch of bodges. But I think they can be simply adapted.

## Thanks
I created these scripts while following the book ["Automating The Boring Stuff With Python"](https://automatetheboringstuff.com/). There are some scripts that are from the book and some of them are mine.

# Usage
Please refer to the [Appendix B of Automating The Boring Stuff With Python](https://automatetheboringstuff.com/appendixb/)
For Windows, use Run (`windows + R`)

# Explanation of some scripts

## Genbatch
This script automatically creates batch files in the main folder that I keep the batches.

### Usage
`delcom`

## Delcom
This script is for deleting the batch file and the script (it sends them to trash).

### Usage
`delcom <batch_file_name>`

### Example
`delcom test`

## Shorter
This script is for creating shortcuts for folders and urls.

### Usage
First, copy the folder path or the url.

Then:
`shorter <tag>`

Then, you can use the tag as a command. If you want to delete a shortcut, refer to delcom command.
