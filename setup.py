from distutils.core import setup
from Cython.Build import cythonize

setup(
  name='My 2048 Operation',
  ext_modules=cythonize("my_2048_operation.pyx"),
)
