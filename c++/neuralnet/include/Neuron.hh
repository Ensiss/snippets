#ifndef         __NEURON_HH__
#define         __NEURON_HH__

#include        <iostream>
#include        <cstdint>
#include        <cstdlib>
#include        <vector>
#include        <cmath>
#include        "Utils.hh"
#include        "Link.hh"

namespace       NN
{
  class         Neuron
  {
  public:
    Neuron();

  public:
    void        linkTo(Neuron *n);

    double      updateOutput(double output);
    double      updateOutput();
    double      getOutput() const { return (_result); }

    void        updateDelta(double expected);
    void        updateDelta();
    double      getDelta() const { return (_delta); }
    void        updateWeight(Link *l, double in, double rate);
    void        updateWeights(const std::vector<double> &inputs, double rate = 0.4);
    void        updateWeights(double rate = 0.4);

  protected:
    double              _bias;
    double              _result;
    double              _delta;
    std::vector<Link *> _in;
    std::vector<Link *> _out;
  };
};

#endif
