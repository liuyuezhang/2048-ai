from distutils.core import setup
from Cython.Build import cythonize

setup(
  name='Search',
  ext_modules=cythonize("search.pyx"),
)
