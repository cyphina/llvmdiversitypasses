#include <llvm/PassRegistry.h>
#include <llvm/CodeGen/MachineFunctionPass.h>
#include <memory>

#ifndef LLVM_CODEGEN_NOOPINSERTION
#define LLVM_CODEGEN_NOOPINSERTION

namespace llvm {

class RandomNumberGenerator;

class NoopInserter : public llvm::MachineFunctionPass {
public:
  static char ID;
  NoopInserter();
private:
    virtual bool runOnMachineFunction(llvm::MachineFunction &Fn) override;
    std::unique_ptr<RandomNumberGenerator> RNG;
  };
}

#endif
