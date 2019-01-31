import os
from math import pi as π

def sin(x):
    return x

if os.environ.get('USE_REFERENCE_IMPLEMENTATION'):
    from math import sin


def cos(x):
    return sin(x + (π / 2))
