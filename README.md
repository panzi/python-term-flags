Term Flags
==========

A primitive sytem to render simple scalable flags on the terminal. A better
system could enable drawing of more details.

This makes use of [Symbols for Legacy
Computing](https://en.wikipedia.org/wiki/Symbols_for_Legacy_Computing). Not all
terminals or fonts used in terminals work well with this. In my tests konsole
with it's default font 'Hack' worked well. gnome-terminal was ok, but a bit
wobbly. When changing the font to 'Hack' for that too it worked just as well as
konsole. xterm, alacritty, and kitty (or their default fonts) where compeltely
broken.

There are a few flags built-in for demo/testing purposes, but you could also
define more as files JSON and render those.

This is what it looks like in konsole:

![screenshot of all included flags](https://assets.chaos.social/media_attachments/files/113/863/898/834/844/862/original/d130f25cd0ff6473.png)

And here when scaling up just the ally flag 8 times:

![screenshot of the ally flag](https://assets.chaos.social/media_attachments/files/113/863/891/346/971/743/original/bc30a3f5271f727a.png)

## Related Projects

I've mentioned other things that I did with Unicode on the terminal lately.
In case you're interested, here is a list of those things:

- [Color Cycling](https://github.com/panzi/rust-color-cycle) (Rust): This is a
  method to give otherwise static pixel art images some kind of animation using
  its color palette.
- [Bad Apple!! but its the Unix Terminal](https://github.com/panzi/bad-apple-terminal)
  (C): A program that displays the Bad Apple!! animation on the terminal.
- [ANSI IMG](https://github.com/panzi/ansi-img) (Rust): Display images (including
  animated GIFs) on the terminal.
- [Unicode Bar Charts](https://github.com/panzi/js-unicode-bar-chart)
  (JavaScript): Draw bar charts on the terminal. With 8 steps per character and
  with colors.
- [Unicode Progress Bars](https://github.com/panzi/js-unicode-progress-bar)
  (JavaScript): Draw bar charts on the terminal. With 8 steps per character,
  border styles, and colors.
- [Unicode Unicode Plots](https://github.com/panzi/js-unicode-plot) (JavaScript):
  Very simple plotting on the terminal. No colors.
