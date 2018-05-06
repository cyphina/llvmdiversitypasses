#include <stdio.h>
#define XXX __asm__("nop");

int main(int argc, char** argv) {
  XXX;
  XXX;
  int a = 3;
  XXX;
  XXX;
  XXX;
  int c = 9;
  XXX;
  XXX;
  int b = 2;
  XXX;
  XXX;
  return 0;
}
