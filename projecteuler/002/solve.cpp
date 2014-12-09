#include        <iostream>

template <bool cond, int a, int b, int max>
struct  If;

template <int a, int b, int max>
struct  Solver
{
  static const int val = If<(a < max), a, b, max>::val;
};

template <int a, int b, int max>
struct  If<true, a, b, max>
{
  static const int val = (a * !(a & 1)) + Solver<b, a + b, max>::val;
};

template <int a, int b, int max>
struct  If<false, a, b, max>
{
  static const int val = 0;
};

int             main()
{
  std::cout << Solver<1, 2, 4000000>::val << std::endl;
  return (0);
}
