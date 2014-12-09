#include        <iostream>

template <int n>
struct  Solver
{
  static const int val = n * (!(n % 3) || !(n % 5)) + Solver<n - 1>::val;
};

template <>
struct  Solver<0>
{
  static const int val = 0;
};

// Compile with g++ -ftemplate-depth=1000 solve.cpp
int             main()
{
  std::cout << Solver<999>::val << std::endl;
  return (0);
}
