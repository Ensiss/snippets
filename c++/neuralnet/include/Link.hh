#ifndef         __LINK_HH__
#define         __LINK_HH__

#include        "Utils.hh"

namespace       NN
{
  class         Neuron;

  class         Link
  {
  public:
    Link(Neuron *prev, Neuron *next)
      : _prev(prev), _next(next), _weight(Utils::drand(1))
    {}

  public:
    Neuron      *operator[](uint8_t i) { return (i ? _next : _prev); }
    Neuron      *getPrev() { return (_prev); }
    Neuron      *getNext() { return (_next); }
    double      getWeight() const { return (_weight); }
    void        setWeight(double w) { _weight = w; }
    void        addWeight(double w) { _weight += w; }

  private:
    Neuron      *_prev;
    Neuron      *_next;
    double      _weight;
  };
};

#endif
