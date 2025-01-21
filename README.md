Term Flags
==========

A primitive sytem to render simple scalable flags on the terminal. A better
system could enable drawing of more details.

Not all terminals or fonts used in terminals work well with this. In my tests
konsole with it's default font 'Hack' worked well. gnome-terminal was ok, but
a bit wobbly. When changing the font to 'Hack' for that too it worked just as
well as konsole. xterm, alacritty, and kitty (or their default fonts) where
compeltely broken.

There are a few flags built-in for demo/testing purposes, but you could also
define more as files JSON and render those.

This is what it looks like in konsole:

![screenshot of all included flags](https://assets.chaos.social/media_attachments/files/113/863/898/834/844/862/original/d130f25cd0ff6473.png)

And here when scaling up just the ally flag 8 times:

![screenshot of the ally flag](https://assets.chaos.social/media_attachments/files/113/863/891/346/971/743/original/bc30a3f5271f727a.png)
