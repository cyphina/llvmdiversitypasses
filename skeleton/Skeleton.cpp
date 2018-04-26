#include "llvm/IR/Function.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/InstrTypes.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Type.h"
#include "llvm/Pass.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/Transforms/IPO/PassManagerBuilder.h"
#include "llvm/Transforms/Utils/BasicBlockUtils.h"
#include <cstring>

using namespace llvm;

static LLVMContext TheContext;

namespace {
struct SkeletonPass : public FunctionPass {
  static char ID;
  SkeletonPass() : FunctionPass(ID) {}

  virtual bool runOnFunction(Function &F) {
    int i = 0;
    for (auto &B : F) {
      for (auto &I : B) {
        // http://llvm.org/docs/ProgrammersManual.html#creating-and-inserting-new-instructions
        IRBuilder<> builder(&I);
        // if this instruction is an an assignment instruction
        if (strcmp(I.getOpcodeName(), "alloca") == 0) {
          auto *ai = builder.CreateAlloca(Type::getDoubleTy(TheContext), 0, "asdfasdf" + ++i);
          //ai->insertAfter(&I);
          // We modified the code.
        }

      }
    }
    return true;
  }
};
} // namespace

char SkeletonPass::ID = 0;
static RegisterPass<SkeletonPass> X("skeleton", "Skeleton Pass",
                             false /* Only looks at CFG */,
                             false /* Analysis Pass */);

// Automatically enable the pass.
// http://adriansampson.net/blog/clangpass.html
static void registerSkeletonPass(const PassManagerBuilder &,
                                 legacy::PassManagerBase &PM) {
  PM.add(new SkeletonPass());
}
static RegisterStandardPasses
    RegisterMyPass(PassManagerBuilder::EP_EarlyAsPossible,
                   registerSkeletonPass);
