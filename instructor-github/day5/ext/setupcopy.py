"""Install the sample extension."""

from distutils.core import setup, Extension

setup(
    name = "hp",
    ext_modules = [ Extension("ext3", sources=["ext3.c"]),

        ]
    )


