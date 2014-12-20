#include        <sys/types.h>
#include        <unistd.h>
#include        <iostream>
#include        <cstdlib>
#include        <string>
#include        <ctime>

#include        <SFML/Graphics.hpp>
#include        "Network.hh"
#include        "Utils.hh"

void            testXOR()
{
  NN::Network           net({2, 3, 1});

  for (int i = 0; i < 10000; i++)
    {
      net.learn({0, 0}, {0});
      net.learn({1, 0}, {1});
      net.learn({0, 1}, {1});
      net.learn({1, 1}, {0});
    }
  for (double y = 0; y < 2; y++)
    for (double x = 0; x < 2; x++)
      std::cout << "(" << x << ", " << y << ") -> " << net.getOutput({x, y})[0] << std::endl;
}

int             main(int ac, char **av)
{
  if (ac < 2)
    {
      std::cerr << "Usage: " << av[0] << " <path_to_image>" << std::endl;
      return (1);
    }
  Utils::init();

  NN::Network           net({2, 15, 3});
  int                   it = 0;
  sf::Image             orig, out;
  if (!orig.loadFromFile(av[1]))
    return (1);
  out.create(orig.getSize().x, orig.getSize().y);
  sf::Texture           textOrig, textOut;
  if (!textOrig.loadFromImage(orig) || !textOut.loadFromImage(out))
    return (1);
  sf::Sprite            spOrig(textOrig), spOut(textOut);
  spOut.setPosition(orig.getSize().x, 0);
  sf::RenderWindow      window(sf::VideoMode(2 * orig.getSize().x, orig.getSize().y),
                               "NN Test", sf::Style::Titlebar | sf::Style::Close);

  while (window.isOpen())
    {
      sf::Event event;
      while (window.pollEvent(event))
        {
          if (event.type == sf::Event::Closed)
            window.close();
        }

      window.clear();
      window.draw(spOrig);
      window.draw(spOut);
      window.display();

      // Learn the image
      double rate = .4 / (1 + .0005 * it);
      std::cout << "Iteration " << it << " (rate = " << rate << ")" << std::endl;
      for (uint32_t y = 0; y < out.getSize().y; y++)
        {
          for (uint32_t x = 0; x < out.getSize().x; x++)
            {
              std::vector<double> vin = {(double) x / out.getSize().x, (double) y / out.getSize().x};
              sf::Color c = orig.getPixel(x, y);
              std::vector<double> vout = {c.r / 255.0, c.g / 255.0, c.b / 255.0};
              net.learn(vin, vout, rate);
            }
        }
      it++;

      // Display result
      if (it % 2 == 0)
        {
          for (uint32_t y = 0; y < out.getSize().y; y++)
            {
              for (uint32_t x = 0; x < out.getSize().x; x++)
                {
                  std::vector<double> vin = {(double) x / out.getSize().x, (double) y / out.getSize().x};
                  std::vector<double> predict = net.getOutput(vin);
                  out.setPixel(x, y, sf::Color(predict[0] * 255, predict[1] * 255, predict[2] * 255));
                }
            }
        }
      textOut.update(out);
    }
  return (0);
}
