import os


def sin(x):
    return x

if os.environ.get('USE_REFERENCE_IMPLEMENTATION'):
    from math import sin
