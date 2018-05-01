#include <iostream>

template <int T> struct fact {
  static const int result = T * fact<T - 1>::result;
};

template <> struct fact<1> { static const int result = 1; };

int main(int agrc, char **agrv) {
  std::cout << fact<5>::result;
  return 0;
}
