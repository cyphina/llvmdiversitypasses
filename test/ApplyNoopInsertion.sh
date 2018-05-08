#!/bin/bash
for ((number=1; number < 6; number++))
{
echo "Running Pass"
opt -noop-inserter -rng-seed=$number ./testOutput/test$number.bc -o ./testOutput/testNoop$number.bc
opt -noop-inserter -rng-seed=$number ./testOutput/testAlloc$number.bc -o ./testOutput/testNoopAlloc$number.bc
echo "Outputting transformed code assembly (llc must be used for machinefunctionpass to activate)"
llc ./testOutput/testNoop$number.bc -o ./testOutput/testNoop$number.s
llc ./testOutput/testNoopAlloc$number.bc -o ./testOutput/testNoopAlloc$number.s
echo "Compiling executeable with no optimization"
clang++ -o ./testOutput/testNoop$number ./testOutput/testNoop$number.s
clang++ -o ./testOutput/testNoopAlloc$number ./testOutput/testNoopAlloc$number.s
}
