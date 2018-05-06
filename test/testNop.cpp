#include <stdio.h>
#define XXX __asm__("nop");

int main(int argc, char** argv) {
  XXX;
  XXX;
  int a = 3;
  XXX;
  XXX;
  XXX;
  XXX;
  return 0;
}
