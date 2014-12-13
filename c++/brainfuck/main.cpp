#include        <iostream>
#include        <unistd.h>
#include        <cstring>

class           BrainFuck
{
public:
  BrainFuck(const char *src, unsigned int mem = 4096)
    : _pc(src), _mem(new char[mem]), _ptr(_mem) {}
  BrainFuck() { delete[] _mem; }

public:
  void          step()
  {
    if (*_pc == '>' || *_pc == '<')
      _ptr += *_pc - '=';
    else if (*_pc == '+' || *_pc == '-')
      *_ptr += ',' - *_pc;
    else if (*_pc == '.')
      write(1, _ptr, 1);
    else if (*_pc == ',')
      read(0, _ptr, 1);
    else if (*_pc == ']' && *_ptr && --_pc)
      for (int c = 1; c; --_pc, c += *_pc == '[' ? -1 : *_pc == ']');
    _pc += !!(*_pc);
  }
  void          run()
  {
    while (*_pc)
      step();
  }

private:
  const char    *_pc;
  char          *_mem;
  char          *_ptr;
};

int             main(int ac, char **av)
{
  char          buff[4016];

  if (ac < 2)
    {
      int ret = read(0, buff, 4016);
      if (ret && buff[ret - 1])
        buff[ret - 1] = '\0';
    }
  else
    strcpy(buff, av[1]);

  BrainFuck     bf(buff);
  bf.run();
  return (0);
}
