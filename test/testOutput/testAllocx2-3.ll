; ModuleID = './testOutput/testAllocx2-3.bc'
source_filename = "./testOutput/test3.bc"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: norecurse nounwind uwtable
define i32 @main(i32 %argc, i8** %argv) #0 {
  %sdfasdf1 = alloca double
  store double 2.000000e+00, double* %sdfasdf1
  %sdfasdf = alloca double
  store double 2.000000e+00, double* %sdfasdf
  %dfasdf2 = alloca double
  store double 2.000000e+00, double* %dfasdf2
  %1 = alloca i32, align 4
  %fasdf3 = alloca double
  store double 2.000000e+00, double* %fasdf3
  %dfasdf = alloca double
  store double 2.000000e+00, double* %dfasdf
  %asdf4 = alloca double
  store double 2.000000e+00, double* %asdf4
  %2 = alloca i32, align 4
  %sdf = alloca double
  store double 2.000000e+00, double* %sdf
  %fasdf = alloca double
  store double 2.000000e+00, double* %fasdf
  %df = alloca double
  store double 2.000000e+00, double* %df
  %3 = alloca i8**, align 8
  %f = alloca double
  store double 2.000000e+00, double* %f
  %asdf = alloca double
  store double 2.000000e+00, double* %asdf
  %4 = alloca double
  store double 2.000000e+00, double* %4
  %a = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 %argc, i32* %2, align 4
  store i8** %argv, i8*** %3, align 8
  store i32 3, i32* %a, align 4
  ret i32 0
}

attributes #0 = { norecurse nounwind uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
