A simple tool that helps me renaming video files of anime and tv series to an easy to work with and universal format.

## How to use

`main.py [folder]`

I made myself a symlink to main.py for easier access across my linux system

`alias format=PATH/TO/FOLDER/main.py` =>
`format [folder]`

Don't be scared if you use it in the wrong folder, before renaming the tool gives you a hint which files exactly get renamed to what and you have to confirm (UX; wooooo!)

## How it works
Ehm. A shitton of regex basically. That makes it kinda unreadable but it was easy to code. Thats not what this segment is about tho :D

### Example
 `Awesome Series with LONG name S3E01 GerEngSub AAC 1080p WebDL x264-SubGroup.mkv`
 => `awesome-series-with-long-name-S03E01.mkv`

The above has lots of Uppercase, spaces and general bloat such as the format, codec used and subgroup in it. I want to get rid of this so that trees look cleaner and more readable.
Also, season and episode numbers become 2 digit which also makes them more readable.
