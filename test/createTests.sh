#!/bin/bash
for ((number=1;number < 4;number++))
{
clang++ -emit-llvm -c test$number.cpp -o test$number.bc
opt -S test$number.bc > test$number.ll
}
