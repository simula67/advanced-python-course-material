"""Install the sample extension."""

from distutils.core import setup, Extension

setup(
    name = "hp",
    ext_modules = [ Extension("ext1", sources=["ext1.c"]),
])


