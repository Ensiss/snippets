#ifndef         __STATE_HH__
#define         __STATE_HH__

#include        <vector>

namespace       NN
{
  struct        State
  {
    std::vector<uint8_t>        layers;
    std::vector<double>         weights;
  };
};

#endif
