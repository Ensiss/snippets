#ifndef         __NETWORK_HH__
#define         __NETWORK_HH__

#include        "Layer.hh"

namespace       NN
{
  class           Network
  {
  public:
    Network(const std::vector<uint8_t> nb);

  public:
    std::vector<double> getOutput(const std::vector<double> &input);
    void                learn(const std::vector<double> &input, const std::vector<double> &output, double rate = 0.4);

  private:
    void                _updateOutput(const std::vector<double> &input);

  private:
    std::vector<Layer *>  _layers;
  };
};

#endif
