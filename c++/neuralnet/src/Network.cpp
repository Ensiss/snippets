#include        "Network.hh"

NN::Network::Network(const std::vector<uint8_t> nb)
{
  if (nb.size() < 2)
    throw "A neural network must have at least two layers\n";
  for (uint8_t i = 0; i < nb.size(); i++)
    {
      Layer     *layer = new Layer(nb[i]);

      if (i)
        _layers[i - 1]->linkTo(layer);
      _layers.push_back(layer);
    }
}

NN::Network::Network(const State &state)
{
  load(state);
}

NN::Network::~Network()
{
  for (Layer *l: _layers)
    delete l;
}

void            NN::Network::save(State &state)
{
  state.layers.clear();
  state.weights.clear();
  for (Layer *layer: _layers)
    layer->save(state);
}

NN::State       NN::Network::save()
{
  State         state;

  save(state);
  return (state);
}

void            NN::Network::load(const State &state)
{
  while (_layers.size())
    {
      delete _layers.back();
      _layers.pop_back();
    }

  uint32_t      i = 0;
  for (uint8_t nb: state.layers)
    {
      Layer     *layer = new Layer(nb);

      if (_layers.size())
        _layers.back()->linkTo(layer);
      _layers.push_back(layer);
      layer->load(state, i);
    }
}

// void            NN::Network::import(const State &state);

void            NN::Network::_updateOutput(const std::vector<double> &input)
{
  _layers[0]->updateOutput(input);
  for (uint8_t i = 1; i < _layers.size(); i++)
    _layers[i]->updateOutput();
}

std::vector<double>     NN::Network::getOutput(const std::vector<double> &input)
{
  _updateOutput(input);
  return (_layers[_layers.size() - 1]->getOutput());
}

void                    NN::Network::learn(const std::vector<double> &input, const std::vector<double> &output, double rate)
{
  // Update outputs forward
  _updateOutput(input);

  // Compute error delta backwards
  _layers[_layers.size() - 1]->updateDelta(output);
  for (uint8_t i = _layers.size() - 2; i > 0; i--)
    _layers[i]->updateDelta();

  // Update weights forward
  _layers[1]->updateWeights(input, rate);
  for (uint8_t i = 2; i < _layers.size(); i++)
    _layers[i]->updateWeights(rate);
}
