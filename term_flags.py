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

from typing import NamedTuple, Optional, Any
from enum import Enum
from os import get_terminal_size
from argparse import ArgumentParser, ArgumentTypeError

import json

class LineCap(Enum):
    Square  = 1
    TriDown = 2
    TriUp   = 3

White     = (255, 255, 255)
Black     = (  0,   0,   0)
TransPink = (245, 168, 184) # or (244, 174, 200)
TransBlue = ( 91, 207, 249) # or (123, 204, 229)
PBrown    = (149,  85,  23)
PRed      = (227,  32,  32)
POrange   = (245, 136,  23)
PYellow   = (240, 229,  37)
PGreen    = (121, 184,  43)
PBlue     = ( 45,  89, 163)
PPurple   = (109,  35, 128)

Color = tuple[int, int, int]

class LineSegment(NamedTuple):
    color: Color
    length: int
    cap: LineCap

Flag = list[list[LineSegment]]

SQ = LineCap.Square
TD = LineCap.TriDown
TU = LineCap.TriUp

LineCapMap = {
    'sq': SQ, 'square': SQ,
    'td': TD, 'tridown': TD,
    'tu': TU, 'triup': TU,
}

LS = LineSegment

# See: https://www.hrc.org/resources/lgbtq-pride-flags
# See: https://www.volvogroup.com/en/news-and-media/news/2021/jun/lgbtq-pride-flags-and-what-they-stand-for.html

ZARed    = (224,  60,  50)
ZAGreen  = (  0, 119,  73)
ZAYellow = (254, 184,  28)
ZABlue   = (  0,  19, 137)

ATRed = (200,  16,  46)
CHRed = (255,   0,   0)

ISBlue = (  2,  82, 156)
ISRed  = (220,  30,  53)

UABlue   = (  0,  87, 183)
UAYellow = (255, 215,   0)

PSRed   = (237,  46,  56)
PSGreen = (  0, 150,  57)

FLAGS: dict[str, Flag] = {
    'progress-pride': [
        [LS(TransPink, 3, TD), LS(TransBlue, 4, TD), LS(PBrown, 4, TD), LS(Black, 4, TD), LS(PRed, 21, SQ)],
        [LS(White, 2, TD), LS(TransPink, 4, TD), LS(TransBlue, 4, TD), LS(PBrown, 4, TD), LS(Black, 4, TD), LS(POrange, 18, SQ)],
        [LS(White, 5, TD), LS(TransPink, 4, TD), LS(TransBlue, 4, TD), LS(PBrown, 4, TD), LS(Black, 4, TD), LS(PYellow, 15, SQ)],
        [LS(White, 5, TU), LS(TransPink, 4, TU), LS(TransBlue, 4, TU), LS(PBrown, 4, TU), LS(Black, 4, TU), LS(PGreen, 15, SQ)],
        [LS(White, 2, TU), LS(TransPink, 4, TU), LS(TransBlue, 4, TU), LS(PBrown, 4, TU), LS(Black, 4, TU), LS(PBlue, 18, SQ)],
        [LS(TransPink, 3, TU), LS(TransBlue, 4, TU), LS(PBrown, 4, TU), LS(Black, 4, TU), LS(PPurple, 21, SQ)],
    ],
    'ally': [
        [LS(Black, 18, TU), LS(PRed,     3, TD), LS(Black, 15, SQ)],
        [LS(White, 15, TU), LS(POrange,  9, TD), LS(White, 12, SQ)],
        [LS(Black, 12, TU), LS(PYellow, 15, TD), LS(Black,  9, SQ)],
        [LS(White,  9, TU), LS(PGreen,  21, TD), LS(White,  6, SQ)],
        [LS(Black,  6, TU), LS(PBlue,   12, TU), LS(Black,  3, TD), LS(PBlue,   12, TD), LS(Black, 3, SQ)],
        [LS(White,  3, TU), LS(PPurple, 12, TU), LS(White,  9, TD), LS(PPurple, 12, TD), LS(White, 0, SQ)],
    ],
    'trans': [
        [LS(TransBlue, 30, SQ)],
        [LS(TransPink, 30, SQ)],
        [LS(White,     30, SQ)],
        [LS(TransPink, 30, SQ)],
        [LS(TransBlue, 30, SQ)],
    ],
    'austria': [
        [LS(ATRed, 30, SQ)],
        [LS(ATRed, 30, SQ)],
        [LS(White, 30, SQ)],
        [LS(White, 30, SQ)],
        [LS(ATRed, 30, SQ)],
        [LS(ATRed, 30, SQ)],
    ],
    'south-africa': [
        [LS(ZAYellow, 1, TD), LS(ZAGreen,  7, TD), LS(White,    4, TD), LS(ZARed,   28, SQ)],
        [LS(ZAYellow, 4, TD), LS(ZAGreen,  7, TD), LS(White,    4, TD), LS(ZARed,   25, SQ)],
        [LS(Black,    3, TD), LS(ZAYellow, 4, TD), LS(ZAGreen,  7, TD), LS(White,   26, SQ)],
        [LS(Black,    6, TD), LS(ZAYellow, 4, TD), LS(ZAGreen, 30, SQ)],
        [LS(Black,    6, TU), LS(ZAYellow, 4, TU), LS(ZAGreen, 30, SQ)],
        [LS(Black,    3, TU), LS(ZAYellow, 4, TU), LS(ZAGreen,  7, TU), LS(White,   26, SQ)],
        [LS(ZAYellow, 4, TU), LS(ZAGreen,  7, TU), LS(White,    4, TU), LS(ZABlue,  25, SQ)],
        [LS(ZAYellow, 1, TU), LS(ZAGreen,  7, TU), LS(White,    4, TU), LS(ZABlue,  28, SQ)],
    ],
    'swizerland': [
        [LS(CHRed, 20, SQ)],
        [LS(CHRed,  8, SQ), LS(White,  4, SQ), LS(CHRed,  8, SQ)],
        [LS(CHRed,  4, SQ), LS(White, 12, SQ), LS(CHRed,  4, SQ)],
        [LS(CHRed,  8, SQ), LS(White,  4, SQ), LS(CHRed,  8, SQ)],
        [LS(CHRed, 20, SQ)],
    ],
    'iceland': [
        [LS(ISBlue, 8, SQ), LS(White, 2, SQ), LS(ISRed,  2, SQ), LS(White, 2, SQ), LS(ISBlue, 16, SQ)],
        [LS(ISBlue, 8, SQ), LS(White, 2, SQ), LS(ISRed,  2, SQ), LS(White, 2, SQ), LS(ISBlue, 16, SQ)],
        [LS(White, 10, SQ), LS(ISRed, 2, SQ), LS(White, 18, SQ)],
        [LS(ISRed, 30, SQ)],
        [LS(White, 10, SQ), LS(ISRed, 2, SQ), LS(White, 18, SQ)],
        [LS(ISBlue, 8, SQ), LS(White, 2, SQ), LS(ISRed, 2, SQ), LS(White, 2, SQ), LS(ISBlue, 16, SQ)],
        [LS(ISBlue, 8, SQ), LS(White, 2, SQ), LS(ISRed, 2, SQ), LS(White, 2, SQ), LS(ISBlue, 16, SQ)],
    ],
    'ukraine': [
        [LS(UABlue,   30, SQ)],
        [LS(UABlue,   30, SQ)],
        [LS(UABlue,   30, SQ)],
        [LS(UAYellow, 30, SQ)],
        [LS(UAYellow, 30, SQ)],
        [LS(UAYellow, 30, SQ)],
    ],
    'palestine': [
        [LS(PSRed, 3, TD), LS(Black,   27, SQ)],
        [LS(PSRed, 6, TD), LS(Black,   24, SQ)],
        [LS(PSRed, 9, TD), LS(White,   21, SQ)],
        [LS(PSRed, 9, TU), LS(White,   21, SQ)],
        [LS(PSRed, 6, TU), LS(PSGreen, 24, SQ)],
        [LS(PSRed, 3, TU), LS(PSGreen, 27, SQ)],
    ]
}

FLAG_ALIASES = {
    'at': FLAGS['austria'],
    'za': FLAGS['south-africa'],
    'ch': FLAGS['swizerland'],
    'is': FLAGS['iceland'],
    'ua': FLAGS['ukraine'],
    'ps': FLAGS['palestine'],

    'iceland-highres': [
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(White,  36, SQ), LS(ISRed, 8, SQ), LS(White, 68, SQ)],

        [LS(ISRed, 112, SQ)],
        [LS(ISRed, 112, SQ)],

        [LS(White,  36, SQ), LS(ISRed, 8, SQ), LS(White, 68, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
        [LS(ISBlue, 32, SQ), LS(White, 4, SQ), LS(ISRed,  8, SQ), LS(White, 4, SQ), LS(ISBlue, 64, SQ)],
    ],
}

FLAG_ALIASES['is-highres'] = FLAG_ALIASES['iceland-highres']

def scale_flag(flag: Flag, scale: int) -> Flag:
    if scale < 1:
        raise ValueError(f'illegal scale: {scale}')

    new_flag: Flag = []
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
                    length_diff = offset * 3
                elif cap == LineCap.TriUp:
                    length_diff = scale_index * 3
                length -= length_diff

                if length < 0:
                    length_diff += length
                else:
                    new_line.append(LineSegment(col, length, cap))

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

def draw_flag_list(buf: list[str], flags: list[Flag], column: int = 0) -> None:
    if not flags:
        return

    max_size = max(len(flag) for flag in flags)
    newlines = max_size - 1

    buf.append('\n' * newlines)
    buf.append(f'\x1B[{newlines}A')

    if column > 1:
        buf.append(f'\x1B[{column}C')
    elif column == 1:
        buf.append(f'\x1B[C')

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
            indent = (term_width - current_width) // 2
            draw_flag_list(buf, bucket, indent)
            #buf.append(f'\x1B[{current_width}D\x1B[3B')
            #buf.append(f'\x1B[3B')
            buf.append(f'\n\n')

            bucket.clear()
            current_width = width
        else:
            current_width = next_width
        bucket.append(flag)

    if bucket:
        indent = (term_width - current_width) // 2
        draw_flag_list(buf, bucket, indent)

def load_flag_from_path(path: str) -> Flag:
    with open(path, 'r') as fp:
        data = json.load(fp)
    return load_flag_from_json(data)

def load_flag_from_json(data: Any) -> Flag:
    if not isinstance(data, dict):
        raise TypeError(f'expected mapping at root: {type(data).__name__}')

    flag_data = data.get('flag')
    if not isinstance(flag_data, list):
        raise TypeError(f'expected sequence at .flag: {type(flag_data).__name__}')

    flag: Flag = []
    for line_index, line_data in enumerate(flag_data):
        if not isinstance(line_data, list):
            raise TypeError(f'expected sequence at .flag[{line_index}]: {type(line_data).__name__}')
        
        line: list[LineSegment] = []
        for segment_index, segment_data in enumerate(line_data):
            if isinstance(segment_data, (tuple, list)):
                if len(segment_data) != 3:
                    raise ValueError(f'expected sequence of length 3 at .flag[{line_index}][{segment_index}]: {len(segment_data)}')

                color_data, length, cap_data = segment_data

                if not isinstance(color_data, (tuple, list)):
                    raise TypeError(f'expected sequence at .flag[{line_index}][{segment_index}]: {type(color_data).__name__}')

                if len(color_data) != 3:
                    raise ValueError(f'expected sequence of length 3 at .flag[{line_index}][{segment_index}][0]: {len(color_data)}')

                for color_index, val in enumerate(color_data):
                    if isinstance(val, float):
                        if float(int(val)) != val:
                            raise TypeError(f'expected integer at .flag[{line_index}][{segment_index}][0][{color_index}]: {val}')
                    elif not isinstance(val, int):
                        raise TypeError(f'expected integer at .flag[{line_index}][{segment_index}][0][{color_index}]: {val}')

                    if val < 0 or val > 255:
                        raise TypeError(f'value out of range at .flag[{line_index}][{segment_index}][0][{color_index}]: {val}')

                color = tuple(map(int, color_data))

                if isinstance(length, float):
                    ilength = int(length)
                    if float(ilength) != length:
                        raise TypeError(f'expected integer at .flag[{line_index}][{segment_index}][1]: {length}')
                    length = ilength
                elif not isinstance(length, int):
                    raise TypeError(f'expected integer at .flag[{line_index}][{segment_index}][1]: {length}')

                if length < 0:
                    raise TypeError(f'value out of range at .flag[{line_index}][{segment_index}][1]: {length}')

                if isinstance(cap_data, float):
                    icap = int(cap_data)
                    if float(icap) != cap_data:
                        raise TypeError(f'expected integer at .flag[{line_index}][{segment_index}][2]: {cap_data}')
                    try:
                        cap = LineCap(icap)
                    except ValueError as exc:
                        raise ValueError(f'value out of range at .flag[{line_index}][{segment_index}][2]: {cap_data}') from exc
                elif isinstance(cap_data, int):
                    try:
                        cap = LineCap(cap_data)
                    except ValueError as exc:
                        raise ValueError(f'value out of range at .flag[{line_index}][{segment_index}][2]: {cap_data}') from exc
                elif isinstance(cap_data, str):
                    lower_cap = cap_data.lower()
                    try:
                        cap = LineCapMap[lower_cap]
                    except KeyError as exc:
                        raise ValueError(f'illegal value of range at .flag[{line_index}][{segment_index}][2]: {cap_data}') from exc
                else:
                    raise TypeError(f'expected integer or string at .flag[{line_index}][{segment_index}][2]: {cap_data}')

                line.append(LineSegment(color, length, cap))
            elif isinstance(segment_data, LineSegment):
                line.append(segment_data)
            else:
                raise TypeError(f'expected sequence or LineSegment at .flag[{line_index}][{segment_index}]: {type(segment_data).__name__}')

    return flag

def parse_scale(value: str) -> int:
    try:
        scale = int(value, 10)
    except ValueError as exc:
        raise ArgumentTypeError(f"expected integer: {value!r}") from exc

    if scale < 1:
        raise ArgumentTypeError(f"must be >= 1: {scale}")

    return scale

def main() -> None:
    ap = ArgumentParser()
    ap.add_argument('-s', '--scale', type=parse_scale, default=1)
    ap.add_argument('flags', nargs='+')
    args = ap.parse_args()
    scale: int = args.scale
    flag_names: list[str] = args.flags

    flags: list[Flag] = []
    for flag_name in flag_names:
        if flag_name == 'all':
            flags.extend(FLAGS.values())
        elif '/' in flag_name or '\\' in flag_name or '.' in flag_name:
            flags.append(load_flag_from_path(flag_name))
        else:
            norm_flag_name = flag_name.lower().replace('_', '-')
            try:
                flags.append(FLAGS.get(norm_flag_name) or FLAG_ALIASES[norm_flag_name])
            except KeyError as exc:
                raise ValueError(f'unknown flag name: {flag_name}') from exc

    buf: list[str] = []

    # CSI ?  7 l     No Auto-Wrap Mode (DECAWM), VT100.
    buf.append("\x1B[?25l")

    draw_wrapped_flag_list(buf, flags, scale)

    # CSI ?  7 h     Auto-Wrap Mode (DECAWM), VT100
    buf.append("\x1B[?25h\n")

    print(''.join(buf))

if __name__ == '__main__':
    main()
