#include "noop.h"

#include <llvm/CodeGen/MachineInstrBuilder.h>
#include <llvm/Target/TargetMachine.h>
#include <llvm/CodeGen/TargetInstrInfo.h>
#include <llvm/IR/PassManager.h>
#include <llvm/Transforms/IPO/PassManagerBuilder.h>
#include <llvm/CodeGen/Passes.h>
#include <llvm/CodeGen/TargetSubtargetInfo.h>
#include "llvm/Pass.h"

#define GET_INSTRINFO_ENUM
#include "../lib/Target/X86/X86GenInstrInfo.inc"

#define GET_REGINFO_ENUM
#include "../lib/Target/X86/X86GenRegisterInfo.inc.tmp"

namespace llvm {
  char NoopInserter::ID = 0;

  NoopInserter::NoopInserter() : llvm::MachineFunctionPass(ID) {
  }

  bool NoopInserter::runOnMachineFunction(llvm::MachineFunction &fn) {
    const llvm::TargetInstrInfo &TII = *fn.getSubtarget().getInstrInfo();
    MachineBasicBlock& bb = *fn.begin();
    llvm::BuildMI(bb, bb.begin(), llvm::DebugLoc(), TII.get(llvm::X86::NOOP));
    return true;
  }

  char& NoopInserterID = NoopInserter::ID;
}

using namespace llvm;

INITIALIZE_PASS_BEGIN(NoopInserter, "noop-inserter",
  "Insert a NOOP", false, false)
INITIALIZE_PASS_DEPENDENCY(PEI)
INITIALIZE_PASS_END(NoopInserter, "noop-inserter",
  "Insert a NOOP", false, false)
