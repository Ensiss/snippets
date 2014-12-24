NAME=	neural

SRC=	main.cpp		\
	src/Neuron.cpp		\
	src/Layer.cpp		\
	src/Network.cpp		\
	src/Utils.cpp

OBJ=	$(SRC:.cpp=.o)

RM=	rm -f

CXX=	g++

CXXFLAGS=	-O3 -I include	\
		-Wall		\
		-std=c++11 -g

LDFLAGS=	-lm		\
		-lsfml-graphics	\
		-lsfml-window	\
		-lsfml-system

all: $(NAME)

$(NAME): $(OBJ)
	$(CXX) $(LDFLAGS) -o $(NAME) $(OBJ)

clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(NAME)

re: fclean all
