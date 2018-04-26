#include <llvm/PassRegistry.h>
#include <llvm/CodeGen/MachineFunctionPass.h>

namespace llvm {
  class NoopInserter : public llvm::MachineFunctionPass {
  public:
    static char ID;
    NoopInserter();
    virtual bool runOnMachineFunction(llvm::MachineFunction &Fn);
  };
}
