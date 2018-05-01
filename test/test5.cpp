#include <iostream>

int bar(int N) { return 5 + N; }

int main(int agrc, char **agrv) {
  std::cout << bar(5);
  return 0;
}
