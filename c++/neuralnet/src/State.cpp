#include        "State.hh"

std::ostream    &operator<<(std::ostream &os, const NN::State &st)
{
  uint16_t      sz;

  sz = st.layers.size();
  os.write((char *) &sz, sizeof(sz));
  for (uint8_t l: st.layers)
    os.write((char *) &l, sizeof(l));

  sz = st.weights.size();
  os.write((char *) &sz, sizeof(sz));
  for (double w: st.weights)
    os.write((char *) &w, sizeof(w));
  return (os);
}

std::istream    &operator>>(std::istream &is, NN::State &st)
{
  uint16_t      sz;

  is.read((char *) &sz, sizeof(sz));
  for (uint16_t i = 0; i < sz; i++)
    {
      uint8_t   val;
      is.read((char *) &val, sizeof(val));
      st.layers.push_back(val);
    }

  is.read((char *) &sz, sizeof(sz));
  for (uint16_t i = 0; i < sz; i++)
    {
      double    val;
      is.read((char *) &val, sizeof(val));
      st.layers.push_back(val);
    }
  return (is);
}
