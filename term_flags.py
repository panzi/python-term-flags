#!/usr/bin/env python3

# U+1FB47 🭇
# U+1FB44 🭄
# U+1FB3C 🬼
# U+1FB4F 🭏
# U+1FB62 🭢
# U+1FB55 🭕
# U+1FB57 🭗
# U+1FB60 🭠
# U+02588 █

# 🭢🭕   U+1FB62 U+1FB55
# ██🭏🬼 U+1FB4F U+1FB3C
# ██🭠🭗 U+1FB60 U+1FB57
# 🭇🭄   U+1FB47 U+1FB44

from typing import NamedTuple, Optional
from enum import Enum
from os import get_terminal_size

class LineCap(Enum):
    Square  = 1
    TriDown = 2
    TriUp   = 3

White     = (255, 255, 255)
Black     = (  0,   0,   0)
TransPink = (245, 168, 184) # or (244, 174, 200)
TransBlue = ( 91, 207, 249) # or (123, 204, 229)
Brown     = (149,  85,  23)
Red       = (227,  32,  32)
Orange    = (245, 136,  23)
Yellow    = (240, 229,  37)
Green     = (121, 184,  43)
Blue      = ( 45,  89, 163)
Purple    = (109,  35, 128)

Color = tuple[int, int, int]

class LineSegment(NamedTuple):
    color: Color
    length: int
    cap: LineCap

Flag = list[list[LineSegment]]

SQ = LineCap.Square
TD = LineCap.TriDown
TU = LineCap.TriUp

LS = LineSegment

# See: https://www.hrc.org/resources/lgbtq-pride-flags
# See: https://www.volvogroup.com/en/news-and-media/news/2021/jun/lgbtq-pride-flags-and-what-they-stand-for.html
ProgressPrideFlag: Flag = [
    [LS(TransPink, 3, TD), LS(TransBlue, 4, TD), LS(Brown, 4, TD), LS(Black, 4, TD), LS(Red, 21, SQ)],
    [LS(White, 2, TD), LS(TransPink, 4, TD), LS(TransBlue, 4, TD), LS(Brown, 4, TD), LS(Black, 4, TD), LS(Orange, 18, SQ)],
    [LS(White, 5, TD), LS(TransPink, 4, TD), LS(TransBlue, 4, TD), LS(Brown, 4, TD), LS(Black, 4, TD), LS(Yellow, 15, SQ)],
    [LS(White, 5, TU), LS(TransPink, 4, TU), LS(TransBlue, 4, TU), LS(Brown, 4, TU), LS(Black, 4, TU), LS(Green, 15, SQ)],
    [LS(White, 2, TU), LS(TransPink, 4, TU), LS(TransBlue, 4, TU), LS(Brown, 4, TU), LS(Black, 4, TU), LS(Blue, 18, SQ)],
    [LS(TransPink, 3, TU), LS(TransBlue, 4, TU), LS(Brown, 4, TU), LS(Black, 4, TU), LS(Purple, 21, SQ)],
]

AllyFlag: Flag = [
    [LS(Black, 18, TU), LS(Red,     3, TD), LS(Black, 15, SQ)],
    [LS(White, 15, TU), LS(Orange,  9, TD), LS(White, 12, SQ)],
    [LS(Black, 12, TU), LS(Yellow, 15, TD), LS(Black,  9, SQ)],
    [LS(White,  9, TU), LS(Green,  21, TD), LS(White,  6, SQ)],
    [LS(Black,  6, TU), LS(Blue,   12, TU), LS(Black,  3, TD), LS(Blue,   12, TD), LS(Black, 3, SQ)],
    [LS(White,  3, TU), LS(Purple, 12, TU), LS(White,  9, TD), LS(Purple, 12, TD), LS(White, 0, SQ)],
]

TransFlag: Flag = [
    [LS(TransBlue, 30, SQ)],
    [LS(TransPink, 30, SQ)],
    [LS(White,     30, SQ)],
    [LS(TransPink, 30, SQ)],
    [LS(TransBlue, 30, SQ)],
]

FlagOfAustria: Flag = [
    [LS(Red, 30, SQ)],
    [LS(Red, 30, SQ)],
    [LS(White, 30, SQ)],
    [LS(White, 30, SQ)],
    [LS(Red, 30, SQ)],
    [LS(Red, 30, SQ)],
]

SARed    = (224,  60,  50)
SAGreen  = (  0, 119,  73)
SAYellow = (254, 184,  28)
SABlue   = (  0,  19, 137)

FLagOfSouthAfrica: Flag = [
    [LS(SAYellow, 1, TD), LS(SAGreen,  7, TD), LS(White,    4, TD), LS(SARed,   28, SQ)],
    [LS(SAYellow, 4, TD), LS(SAGreen,  7, TD), LS(White,    4, TD), LS(SARed,   25, SQ)],
    [LS(Black,    3, TD), LS(SAYellow, 4, TD), LS(SAGreen,  7, TD), LS(White,   26, SQ)],
    [LS(Black,    6, TD), LS(SAYellow, 4, TD), LS(SAGreen, 30, SQ)],
    [LS(Black,    6, TU), LS(SAYellow, 4, TU), LS(SAGreen, 30, SQ)],
    [LS(Black,    3, TU), LS(SAYellow, 4, TU), LS(SAGreen,  7, TU), LS(White,   26, SQ)],
    [LS(SAYellow, 4, TU), LS(SAGreen,  7, TU), LS(White,    4, TU), LS(SABlue,  25, SQ)],
    [LS(SAYellow, 1, TU), LS(SAGreen,  7, TU), LS(White,    4, TU), LS(SABlue,  28, SQ)],
]

def scale_flag(flag: Flag, scale: int) -> Flag:
    if scale < 1:
        raise ValueError(f'illegal scale: {scale}')

    new_flag: Flag = []
    is_odd_line = True
    for flag_line in flag:

        for scale_index in range(scale):
            offset = scale - scale_index - 1

            new_line: list[LineSegment] = []
            new_flag.append(new_line)

            length_diff = 0
            for segment in flag_line:
                length = segment.length * scale + length_diff
                cap = segment.cap
                col = segment.color

                if cap == LineCap.Square:
                    length_diff = 0
                elif cap == LineCap.TriDown:
                    length_diff = offset * 2
                elif cap == LineCap.TriUp:
                    length_diff = scale_index * 2
                length -= length_diff

                new_line.append(LineSegment(col, max(length, 0), cap))
            is_odd_line = not is_odd_line

    return new_flag

def draw_flag(buf: list[str], flag: Flag) -> None:
    bg_col: Optional[Color] = None
    fg_col: Optional[Color] = None

    def set_cols(new_bg: Optional[Color], new_fg: Optional[Color]) -> None:
        nonlocal buf, bg_col, fg_col
        if bg_col != new_bg:
            if new_bg is None:
                buf.append(f'\x1B[49m')
            else:
                buf.append(f'\x1B[48;2;{new_bg[0]};{new_bg[1]};{new_bg[2]}m')
            bg_col = new_bg

        if fg_col != new_fg:
            if new_fg is None:
                buf.append(f'\x1B[38;2;0;0;0m')
            else:
                buf.append(f'\x1B[38;2;{new_fg[0]};{new_fg[1]};{new_fg[2]}m')
            fg_col = new_fg

    def set_bg(new_bg: Optional[Color]) -> None:
        nonlocal bg_col, buf
        if bg_col != new_bg:
            if new_bg is None:
                buf.append(f'\x1B[49m')
            else:
                buf.append(f'\x1B[48;2;{new_bg[0]};{new_bg[1]};{new_bg[2]}m')
            bg_col = new_bg

    x = 0
    max_x = 0
    prev_carry_x = 0
    is_first = True
    for flag_line in flag:
        if x > 0:
            move = (x + 1) // 2
            if move > 1:
                buf.append(f'\x1B[{move}D')
            else:
                buf.append('\x1B[D')

            if not is_first:
                buf.append('\x1B[B')

            if max_x < x:
                max_x = x

            x = 0
            prev_carry_x = 0
        is_first = False

        for segment_index, segment in enumerate(flag_line):
            col = segment.color
            cap = segment.cap
            length = segment.length

            if prev_carry_x:
                length -= 1

            x += length
            carry_x = x & 1
            x += carry_x

            next_index = segment_index + 1
            next_col: Optional[Color]
            if next_index < len(flag_line):
                next_col = flag_line[next_index].color
            else:
                next_col = None

            if cap != LineCap.Square:
                block_length = max(length - 3, 0)

                if block_length > 0:
                    set_bg(col)
                    buf.append(' ' * (block_length >> 1))

                cap_length = length - block_length
                if cap_length > 0:
                    if cap == LineCap.TriDown:
                        if carry_x:
                            set_cols(next_col, col)
                            if cap_length > 1:
                                buf.append('🭏')
                            buf.append('🬼')
                        else:
                            set_cols(col, next_col)
                            if cap_length > 2:
                                buf.append('🭢')
                            buf.append('🭕')

                    elif cap == LineCap.TriUp:
                        if carry_x:
                            set_cols(next_col, col)
                            if cap_length > 1:
                                buf.append('🭠')
                            buf.append('🭗')
                        else:
                            set_cols(col, next_col)
                            if cap_length > 2:
                                buf.append('🭇')
                            buf.append('🭄')

            else:
                if length > 0:
                    set_bg(col)
                    buf.append(' ' * (length >> 1))

                    if carry_x:
                        set_cols(next_col, col)
                        buf.append('▌')

            prev_carry_x = carry_x

    diff = max_x - x
    move = diff // 2
    if move > 1:
        buf.append(f'\x1B[{move}C')
    elif move > 0:
        buf.append('\x1B[C')

    buf.append('\x1B[0m')

def get_flag_width(flag: Flag) -> int:
    return max(
        (sum(segment.length for segment in flag_line)
         for flag_line in flag),
        default=0)

def draw_flag_list(buf: list[str], flags: list[Flag]) -> None:
    if not flags:
        return

    max_size = max(len(flag) for flag in flags)
    newlines = max_size - 1

    buf.append('\n' * newlines)
    buf.append(f'\x1B[{newlines}A')

    for flag in flags[:-1]:
        draw_flag(buf, flag)
        buf.append(f'\x1B[{len(flag) - 1}A\x1B[2C')

    flag = flags[-1]
    draw_flag(buf, flag)
    diff_lines = max_size - len(flag)
    if diff_lines > 0:
        buf.append(f'\x1B[{diff_lines}B')

def draw_wrapped_flag_list(buf: list[str], flags: list[Flag], scale: int = 1) -> None:
    if not flags:
        return

    try:
        term_width = get_terminal_size().columns
    except:
        draw_flag_list(buf, flags)

    if scale != 1:
        flags = [scale_flag(flag, scale) for flag in flags]

    bucket: list[Flag] = []
    current_width = 0
    for flag in flags:
        width = get_flag_width(flag)
        width = (width + 1) // 2
        next_width = current_width + width
        if current_width:
            next_width += 2

        if bucket and next_width > term_width:
            draw_flag_list(buf, bucket)
            #buf.append(f'\x1B[{current_width}D\x1B[3B')
            #buf.append(f'\x1B[3B')

            bucket.clear()
            current_width = width
        else:
            current_width = next_width
        bucket.append(flag)

    if bucket:
        draw_flag_list(buf, bucket)

def main() -> None:
    buf: list[str] = []
    #print('                               🭇🭒')
    #newlines = len(ProgressPrideFlag) - 1
    #buf.append('\n' * newlines)
    #buf.append(f'\x1B[{newlines}A')
    #draw_flag(buf, ProgressPrideFlag)
    draw_wrapped_flag_list(buf, [ProgressPrideFlag, AllyFlag, TransFlag, FlagOfAustria, FLagOfSouthAfrica], 1)
    print(''.join(buf))

if __name__ == '__main__':
    main()
