#include        <iostream>

template <int out, int in>
struct  SubReverse
{
  static const int val = SubReverse<out * 10 + in % 10, in / 10>::val;
};

template <int out>
struct  SubReverse<out, 0>
{
  static const int val = out;
};

template <int n>
struct  Reverse
{
  static const int val = SubReverse<0, n>::val;
};

template <int a, int b>
struct  Checker
{
  static const int val = a * b * (a * b == Reverse<a * b>::val);
};

template <int a, int b>
struct  Max
{
  static const int val = a > b ? a : b;
};

template <int a, int b>
struct  Solver
{
  static const int val = Max<Checker<a, b>::val, Solver<a, b - 1>::val>::val;
};

template <int a>
struct  Solver<a, 1>
{
  static const int val = Solver<a - 1, a - 1>::val;
};

template <>
struct  Solver<1, 1>
{
  static const int val = 1;
};

int             main()
{
  // g++ segfaults when trying 999x999 :(
  std::cout << Solver<99, 99>::val << std::endl;
  return (0);
}
