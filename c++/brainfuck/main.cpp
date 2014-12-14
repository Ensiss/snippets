#include        <sys/types.h>
#include        <sys/stat.h>
#include        <fcntl.h>
#include        <cstdio>
#include        <iostream>
#include        <unistd.h>
#include        <cstring>

class           BrainFuck
{
public:
  BrainFuck(const char *src = NULL, unsigned int mem = 4096)
    : _pc(src), _memsz(mem), _mem(new char[mem]), _ptr(_mem) {}
  ~BrainFuck() { delete[] _mem; }

public:
  void          step()
  {
    if (!_pc)
      return;
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
  void          run(const char *src)
  {
    memset(_mem, 0, _memsz);
    _ptr = _mem;
    _pc = src;
    run();
  }

private:
  const char    *_pc;
  unsigned int  _memsz;
  char          *_mem;
  char          *_ptr;
};

int             main(int ac, char **av)
{
  BrainFuck     bf;
  char          buff[4016];
  int           fd, ret;

  if (ac < 2)
    {
      ret = read(0, buff, 4016);
      if (ret && buff[ret - 1])
        buff[ret - 1] = '\0';
      bf.run(buff);
    }
  else
    {
      for (int i = 1; i < ac; i++)
        {
          if ((fd = open(av[i], O_RDONLY)) == -1)
            {
              perror(av[i]);
              continue;
            }
          if ((ret = read(fd, buff, 4096)) > 0)
            bf.run(buff);
          close(fd);
        }
    }
  return (0);
}
