#!/bin/bash
for ((number=1;number < 6;number++))
{
gcc test$number.cpp -O0 -o ./testOutput/test$number -lstdc++
clang++ -emit-llvm -c test$number.cpp -o ./testOutput/test$number.bc
./build/bin/opt -S ./testOutput/test$number.bc > ./testOutput/test$number.ll
./build/bin/opt -load build/lib/libSkeletonPass.so -skeleton ./testOutput/test$number.bc -o ./testOutput/testAlloc$number.bc
./build/bin/opt -S ./testOutput/testAlloc$number.bc > ./testOutput/testAlloc$number.ll
./build/bin/llc -filetype=obj ./testOutput/testAlloc$number.bc
gcc ./testOutput/testAlloc$number.o -O0 -o ./testOutput/testAlloc$number -lstdc++
./build/bin/opt -load build/lib/libSkeletonPass.so -skeleton ./testOutput/testAlloc$number.bc -o ./testOutput/testAllocx2-$number.bc
./build/bin/opt -S ./testOutput/testAllocx2-$number.bc > ./testOutput/testAllocx2-$number.ll
./build/bin/llc -filetype=obj ./testOutput/testAllocx2-$number.bc
gcc ./testOutput/testAllocx2-$number.o -O0 -o ./testOutput/testAllocx2-$number -lstdc++
}

gcc testNop.cpp -O0 -o ./testOutput/testNop3 -lstdc++
