#ifndef         __LAYER_HH__
#define         __LAYER_HH__

#include        "Neuron.hh"
#include        "State.hh"

namespace       NN
{
  class         Layer
  {
  public:
    Layer(uint8_t size);

  public:
    void        linkTo(Layer *l);
    uint8_t     getSize() const { return (_neurons.size()); }
    Layer       *getPrev() { return (_prev); }
    Layer       *getNext() { return (_next); }

  public:
    void        save(State &state);
    void        load(const State &state, uint32_t &i);

  public:
    std::vector<double> getOutput();
    void        updateOutput();
    void        updateOutput(const std::vector<double> &input);
    void        updateDelta(const std::vector<double> &expected);
    void        updateDelta();
    void        updateWeights(const std::vector<double> &inputs, double rate = 0.4);
    void        updateWeights(double rate = 0.4);

  protected:
    Layer                       *_prev;
    Layer                       *_next;
    std::vector<Neuron *>       _neurons;
  };
}

#endif
