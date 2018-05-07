#include "llvm/CodeGen/noop.h"
#include "llvm/Pass.h"
#include <llvm/CodeGen/MachineInstrBuilder.h>
#include <llvm/CodeGen/Passes.h>
#include <llvm/CodeGen/TargetInstrInfo.h>
#include <llvm/CodeGen/TargetSubtargetInfo.h>
#include <llvm/IR/PassManager.h>
#include <llvm/Support/RandomNumberGenerator.h>
#include <llvm/Target/TargetMachine.h>
#include <llvm/Transforms/IPO/PassManagerBuilder.h>

#define GET_INSTRINFO_ENUM
#include "../lib/Target/X86/X86GenInstrInfo.inc"

#define GET_REGINFO_ENUM
#include "../lib/Target/X86/X86GenRegisterInfo.inc"

#define DEBUG_TYPE "noop-inserter"

namespace llvm {

char NoopInserter::ID = 0;

NoopInserter::NoopInserter() : llvm::MachineFunctionPass(ID) {}

bool NoopInserter::runOnMachineFunction(llvm::MachineFunction &fn) {
  // if(!RNG)
  // RNG.reset(fn.getFunction().getParent()->createRNG(this));
  errs() << "Function body:\n";
  auto RNG = fn.getFunction().getParent()->createRNG(this);

  const llvm::TargetInstrInfo &TII = *(fn.getSubtarget().getInstrInfo());
  MachineBasicBlock &bb = *fn.begin();

int numNoops = (*RNG)() % 100;

for (int i = 0; i < numNoops; ++i) {
  llvm::BuildMI(bb, bb.begin(), llvm::DebugLoc(), TII.get(llvm::X86::NOOP));
  }
  return true;
}

} // namespace llvm

using namespace llvm;

char &llvm::NoopInserterID = NoopInserter::ID;

INITIALIZE_PASS(NoopInserter, "noop-inserter2",
                "Noop Insertion for fine-grained code randomization", false,
                false)
