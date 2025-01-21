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
