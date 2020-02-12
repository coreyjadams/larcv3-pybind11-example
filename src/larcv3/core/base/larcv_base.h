/**
 * \file larcv_base.h
 *
 * \ingroup core_Base
 * 
 * \brief Class definition file of larcv3::larcv_base
 *
 * @author Kazu - Nevis 2015
 */

/** \addtogroup core_Base

    @{*/

#ifndef __LARCV3BASE_LARCV_BASE_H__
#define __LARCV3BASE_LARCV_BASE_H__

#include <vector>
#include <pybind11/pybind11.h>

namespace larcv3 {
    
  /**
    \class larcv_base
    Framework base class equipped with a logger class
  */
  class larcv_base {
    
  public:
    
    /// Default constructor
    larcv_base(const std::string name="larcv_base")
     :  _name(name)
    {  }
    
    /// Default copy constructor
    larcv_base(const larcv_base &original) {}
    
    /// Default destructor
    virtual ~larcv_base(){};
    
    /// Name getter, defined in a logger instance attribute
    const std::string& name() const
    { return _name; }
    
  private:
    std::string _name;
  };
}

void init_larcv_base(pybind11::module m);

#endif

/** @} */ // end of doxygen group
