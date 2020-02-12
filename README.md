# larcv3-pybind11-example

This is a barebones example of a pybind11 build with CMake, broken up source libraries and binding libraries.

To use this, you need:
- cmake
- scikit-build (`pip install scikit-build`)
- python

To build, checkout this repository, and then run `git submodule update` to pull down the pybind11 source code. Then, run:

```bash
python setup.py build [-j 8]
python setup.py install [--user]
```

To compile and install.

To test the software, start python and run 

```python
from larcv import pylarcv
a = pylarcv.larcv_base()
```

Which should work without complaint.
