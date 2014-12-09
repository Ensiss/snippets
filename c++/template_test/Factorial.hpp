#ifndef         __FACTORIAL_HPP__
#define         __FACTORIAL_HPP__

template <int n>
struct          Factorial
{
  static const int val = n * Factorial<n - 1>::val;
};

template<>
struct          Factorial<1>
{
  static const int val = 1;
};

#endif
