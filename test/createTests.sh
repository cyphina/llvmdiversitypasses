#!/bin/bash
for ((number=1;number < 4;number++))
{
clang++ test$number.cpp -o test$number
clang++ -emit-llvm -c test$number.cpp -o test$number.bc
./build/bin/opt -S test$number.bc > test$number.ll
./build/bin/opt -time-passes -load build/lib/libSkeletonPass.so -skeleton test$number.bc -o testAlloc$number.bc
./build/bin/llc -filetype=obj testAlloc$number.bc
gcc testAlloc$number.o -o testAlloc$number
}
