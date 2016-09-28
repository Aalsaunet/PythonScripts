from distutils.core import setup

# if this file is ran with "sudo python setup.py install",
# then the my_unit_testing module will become available for import for python scripts in any directory


module_name='my_unit_testing'

setup(name=module_name,
      version='0.1',
      py_modules=[module_name],       # modules to be installed
      scripts=[module_name + '.py'],  # programs to be installed
      )