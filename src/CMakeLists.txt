cmake_minimum_required(VERSION 3.1 FATAL_ERROR)


# general configuration for compilation:
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -O3 -g")




# set(CMAKE_SKIP_RPATH TRUE)
project(larcv3)

set(CMAKE_PACKAGE_DIR "larcv")

set(PROJECT_SOURCE_DIR "./")


include_directories("./")


# Many packages need python:
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

if(OPENMP)
  find_package(OpenMP)
  if(OpenMP_CXX_FOUND)
      add_definitions(-DLARCV_OPENMP)
  endif()
endif()


# # Define a function that handles generating python bindings for a library:
# macro(generate_python_bindings name)



# endmacro(generate_python_bindings)
if(CMAKE_PYTHON_BINDINGS)
  message("Adding pybind11")
  add_subdirectory(pybind11)
  include_directories(${PYBIND11_INCLUDE_DIR})
  message(${PYBIND11_INCLUDE_DIR})
else()
  add_definitions(-DLARCV_NO_PYBIND)
endif(CMAKE_PYTHON_BINDINGS)

add_subdirectory(larcv3)
