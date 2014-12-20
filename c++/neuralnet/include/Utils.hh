#ifndef         __UTILS_HH__
#define         __UTILS_HH__

#include        <sys/types.h>
#include        <unistd.h>
#include        <iostream>
#include        <cstdlib>
#include        <string>
#include        <ctime>

namespace       Utils
{
  void          init();
  double        drand();
  double        drand(double max);
  double        drand(double min, double max);
};

#endif
