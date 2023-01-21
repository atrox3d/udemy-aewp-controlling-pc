from mss import mss

with mss() as screen:
    screen.shot()
"""
Grab a screen shot and save it to a file.

:param int mon: The monitor to screen shot (default=0).
                -1: grab one screen shot of all monitors
                 0: grab one screen shot by monitor
                 N: grab the screen shot of the monitor N

:param str output: The output filename.

    It can take several keywords to customize the filename:
    - `{mon}`: the monitor number
    - `{top}`: the screen shot y-coordinate of the upper-left corner
    - `{left}`: the screen shot x-coordinate of the upper-left corner
    - `{width}`: the screen shot's width
    - `{height}`: the screen shot's height
    - `{date}`: the current date using the default formatter

    As it is using the `format()` function, you can specify
    formatting options like `{date:%Y-%m-%s}`.

:param callable callback: Callback called before saving the
    screen shot to a file.  Take the `output` argument as parameter.

:return generator: Created file(s).
"""

