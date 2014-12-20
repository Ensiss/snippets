#include        "Utils.hh"

void            Utils::init()
{
  srand(time(NULL) * getpid());
}

double          Utils::drand()
{
  return ((double) rand() / RAND_MAX);
}

double          Utils::drand(double max)
{
  return (max * drand());
}

double          Utils::drand(double min, double max)
{
  return (min + drand(max - min));
}

