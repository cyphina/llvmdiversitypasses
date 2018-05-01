#!/bin/bash
for ((number=1;number < 4;number++))
{
gcc test$number.cpp -O0 -o test$number
clang++ -emit-llvm -c test$number.cpp -o test$number.bc
./build/bin/opt -S test$number.bc > test$number.ll
./build/bin/opt -load build/lib/libSkeletonPass.so -skeleton test$number.bc -o testAlloc$number.bc
./build/bin/opt -S testAlloc$number.bc > testAlloc$number.ll
./build/bin/llc -filetype=obj testAlloc$number.bc
gcc testAlloc$number.o -O0 -o testAlloc$number
}
