#!/usr/bin/env python3
"""
QUINE + MANDELBROT RENDERER
============================
This program does two things simultaneously:
  1. It is a QUINE: running it prints its own exact source code.
  2. Woven into that self-printing process, it computes and renders
     the Mandelbrot set in ASCII art using pure complex-number iteration.

No external files are read. The "s" variable below holds a template of
the entire program's source (minus itself), and %r substitution is used
to reproduce it exactly, semi-colon included, à la classic quine tricks.
"""

def mandelbrot(width=80, height=40, max_iter=60):
    chars = " ="
    xmin, xmax = -2.5, 1.0
    ymin, ymax = -1.2, 1.2
    rows = []
    for row in range(height):
        y0 = ymin + (ymax - ymin) * row / height
        line = []
        for col in range(width):
            x0 = xmin + (xmax - xmin) * col / width
            c = complex(x0, y0)
            z = 0j
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z * z + c
                n += 1
            line.append(chars[int(n / max_iter * (len(chars) - 1))])
        rows.append("".join(line))
    return "\n".join(rows)

s = '#!/usr/bin/env python3\n"""\nQUINE + MANDELBROT RENDERER\n============================\nThis program does two things simultaneously:\n  1. It is a QUINE: running it prints its own exact source code.\n  2. Woven into that self-printing process, it computes and renders\n     the Mandelbrot set in ASCII art using pure complex-number iteration.\n\nNo external files are read. The "s" variable below holds a template of\nthe entire program\'s source (minus itself), and %%r substitution is used\nto reproduce it exactly, semi-colon included, à la classic quine tricks.\n"""\n\ndef mandelbrot(width=80, height=40, max_iter=60):\n    chars = " .:-=+*#%%@"\n    xmin, xmax = -2.5, 1.0\n    ymin, ymax = -1.2, 1.2\n    rows = []\n    for row in range(height):\n        y0 = ymin + (ymax - ymin) * row / height\n        line = []\n        for col in range(width):\n            x0 = xmin + (xmax - xmin) * col / width\n            c = complex(x0, y0)\n            z = 0j\n            n = 0\n            while abs(z) <= 2 and n < max_iter:\n                z = z * z + c\n                n += 1\n            line.append(chars[int(n / max_iter * (len(chars) - 1))])\n        rows.append("".join(line))\n    return "\\n".join(rows)\n\ns = %r\n\nprint("=" * 80)\nprint("SOURCE CODE (self-printed by the quine mechanism):")\nprint("=" * 80)\nprint(s %% s)\nprint()\nprint("=" * 80)\nprint("MANDELBROT SET (computed live, not stored anywhere):")\nprint("=" * 80)\nprint(mandelbrot())\n'

print("=" * 80)
print("SOURCE CODE (self-printed by the quine mechanism):")
print("=" * 80)
print(s % s)
print()
print("=" * 80)
print("MANDELBROT SET (computed live, not stored anywhere):")
print("=" * 80)
print(mandelbrot())