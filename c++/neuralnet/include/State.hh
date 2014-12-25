#ifndef         __STATE_HH__
#define         __STATE_HH__

#include        <ostream>
#include        <istream>
#include        <vector>

namespace       NN
{
  struct        State
  {
    std::vector<uint8_t>        layers;
    std::vector<double>         weights;
  };
};

std::ostream    &operator<<(std::ostream &os, const NN::State &st);
std::istream    &operator>>(std::istream &is, NN::State &st);

#endif
