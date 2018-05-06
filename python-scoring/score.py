import r2pipe
import sys

def test(filename1, filename2):
    r2f1 = r2pipe.open(filename1)
    r2f2 = r2pipe.open(filename2)

    r2f1.cmd("aa")
    r2f2.cmd("aa")

    # Goes to the Main Function
    r2f1.cmd("s main")
    r2f2.cmd("s main")

    # Returns Json format for Main Function
    f1main = r2f1.cmdj("pdfj")
    f2main = r2f2.cmdj("pdfj")

    #Different Tests for the Files
    testAlloc(f1main, f2main)
    testNop(f1main, f2main)

    r2f1.quit()
    r2f2.quit()

def testAlloc(fileJson1, fileJson2):
    ignoreList = ["mov eax, 0"]
    remain1 = []
    remain2 = []
    for op in fileJson1["ops"]:
        if op["disasm"].find("mov ") >= 0 and ignoreList.count(op["disasm"]) == 0:
            remain1.append(op["disasm"])

    for op in fileJson2["ops"]:
        if op["disasm"].find("mov ") >= 0 and ignoreList.count(op["disasm"]) == 0:
            remain2.append(op["disasm"])


    r1 = []
    r2 = []
    contain = False
    for op in remain1:
        for op2 in remain2:
            if op == op2:
                contain = True
                break
        if not contain:
            r1.append(op)
        contain = False

    for op in remain2:
        for op2 in remain1:
            if op == op2:
                contain = True
                break
        if not contain:
            r2.append(op)
        contain = False

    print "Alloc/Store Check: "
    print "File1: ", r1, len(r1)
    print "File2: ", r2, len(r2)
    print "File2 - File1: ", len(r2) - len(r1)

def testNop(fileJson1, fileJson2):
    remain1 = []
    remain2 = []
    for op in fileJson1["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain1.append(op["disasm"])

    for op in fileJson2["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain2.append(op["disasm"])

    print "Nop Check: "
    print "File1: ", remain1, len(remain1)
    print "File2: ", remain2, len(remain2)
    print "File2 - File1: ", len(remain2) - len(remain1)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print "Runnin Scoring Test on ", sys.argv[1], ", ", sys.argv[2]
        test(sys.argv[1], sys.argv[2])
    else:
        print "Arguments Incorrect"
