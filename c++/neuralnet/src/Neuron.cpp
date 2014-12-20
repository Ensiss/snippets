#include        "Neuron.hh"

NN::Neuron::Neuron()
  : _bias(Utils::drand(1)), _result(0), _delta(0)
{
}

void            NN::Neuron::linkTo(Neuron *n)
{
  Link          *ln = new Link(this, n);

  _out.push_back(ln);
  n->_in.push_back(ln);
}

double          NN::Neuron::updateOutput(double output)
{
  _result = output;
  return (_result);
}

double          NN::Neuron::updateOutput()
{
  double        sum = _bias;

  for (Link *l: _in)
    sum += l->getPrev()->getOutput() * l->getWeight();
  _result = 1. / (1 + exp(-sum));
  return (_result);
}

void            NN::Neuron::updateDelta(double expected)
{
  _delta = expected - _result;
  _delta *= _result * (1 - _result);
}

void            NN::Neuron::updateDelta()
{
  _delta = 0;
  for (Link *link: _out)
    _delta += link->getWeight() * link->getNext()->getDelta();
  _delta *= _result * (1 - _result);
}

void            NN::Neuron::updateWeight(Link *l, double in, double rate)
{
  l->addWeight(rate * in * _delta);
}

void            NN::Neuron::updateWeights(const std::vector<double> &inputs, double rate)
{
  for (uint8_t i = 0; i < _in.size(); i++)
    updateWeight(_in[i], inputs[i], rate);
  _bias += rate * _delta;
}

void            NN::Neuron::updateWeights(double rate)
{
  for (uint8_t i = 0; i < _in.size(); i++)
    updateWeight(_in[i], _in[i]->getPrev()->getOutput(), rate);
  _bias += rate * _delta;
}
