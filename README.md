# llvmdiversitypasses
Beginnings of learning to use LLVM to diversify code mainly for the focus of obfuscating it to make reverse engineering more difficult.  

Progress possible thanks to these tutorials:
* https://www.cs.cornell.edu/~asampson/blog/llvm.html
* http://www.gabriel.urdhr.fr/2014/09/26/adding-a-llvm-pass/
* https://reviews.llvm.org/D3392#change-P8klzVX6q0t6

Commands:
Get llvm bitcode from C/C++ program so we can run passes on it
```
clang -O3 -emit-llvm <program-name> -c -o <output-name>
```
Get native assembly from llvm bytecode
```
llc <bitcode-file-name> -o <output-name>
```
