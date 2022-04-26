#include "larcv3/core/base/base.h"
#include <iostream>


PYBIND11_MODULE(pylarcv, m) {
  std::cout << "Here" << std::endl;
  // init_base(m);
}
