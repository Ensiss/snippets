#include        "Layer.hh"

NN::Layer::Layer(uint8_t size)
  : _prev(NULL), _next(NULL), _size(size)
{
  for (uint8_t i = 0; i < _size; i++)
    _neurons.push_back(new Neuron());
}

void            NN::Layer::linkTo(Layer *l)
{
  _next = l;
  l->_prev = this;
  for (Neuron *n: _neurons)
    {
      for (Neuron *ln: l->_neurons)
        n->linkTo(ln);
    }
}

std::vector<double>     NN::Layer::getOutput()
{
  std::vector<double>   out;

  for (Neuron *n: _neurons)
    out.push_back(n->getOutput());
  return (out);
}

void            NN::Layer::updateOutput()
{
  for (Neuron *n: _neurons)
    n->updateOutput();
}

void            NN::Layer::updateOutput(const std::vector<double> &input)
{
  for (uint8_t i = 0; i < _neurons.size(); i++)
    _neurons[i]->updateOutput(input[i]);
}

void            NN::Layer::updateDelta(const std::vector<double> &expected)
{
  for (uint8_t i = 0; i < _neurons.size(); i++)
    _neurons[i]->updateDelta(expected[i]);
}

void            NN::Layer::updateDelta()
{
  for (Neuron *n: _neurons)
    n->updateDelta();
}

void            NN::Layer::updateWeights(const std::vector<double> &inputs, double rate)
{
  for (Neuron *n: _neurons)
    n->updateWeights(inputs, rate);
}

void            NN::Layer::updateWeights(double rate)
{
  for (Neuron *n: _neurons)
    n->updateWeights(rate);
}
