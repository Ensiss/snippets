#include        <iostream>
#include        "Factorial.hpp"
#include        "Pow.hpp"

int             main()
{
  std::cout << "Factorial(5) = " << Factorial<5>::val << std::endl;
  std::cout << "Pow(3, 5) = " << Pow<3, 5>::val << std::endl;
  return (0);
}
