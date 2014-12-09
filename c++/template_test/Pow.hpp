#ifndef         __POW_HPP__
#define         __POW_HPP__

template <int n, int p>
struct  Pow
{
  static const int val = n * Pow<n, p - 1>::val;
};

template <int n>
struct  Pow<n, 1>
{
  static const int val = n;
};

#endif
