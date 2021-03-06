import r2pipe
import sys
import math
import os

retfile = []
filetype = ""

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

    #Store results from different tests
    print(os.path.getsize(filename2))
    print(os.path.getsize(filename1))
    sizediff = os.path.getsize(filename2) - os.path.getsize(filename1)
    reta = testAlloc(f1main, f2main)
    retnl = testNop(f1main, f2main)
    retnd = testNoopDistance(f1main, f2main)
    retjs = testJaccardSim(f1main, f2main)

    r2f1.quit()
    r2f2.quit()

    return "," + str(sizediff) + "," + str(reta) + "," + str(retnl) + "," + str(retnd) + "," + str(retjs)

#Test difference in alloca instruction count
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

    total = len(r2) - len(r1)

    print ("Alloc/Store Check: ")
    print ("File1: ", r1, len(r1))
    print ("File2: ", r2, len(r2))
    print ("File2 - File1: ", total)

    if(total > 0):
        return total
    else:
        return 0

#Test difference in Noop instruction count
def testNop(fileJson1, fileJson2):
    remain1 = []
    remain2 = []
    for op in fileJson1["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain1.append(op["disasm"])

    for op in fileJson2["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain2.append(op["disasm"])

    print ("Nop Check (Difference in Line): ")
    print ("File1: ", remain1, len(remain1))
    print ("File2: ", remain2, len(remain2))
    print ("File2 - File1: ", len(remain2) - len(remain1))

    return len(remain2) - len(remain1)

#Check the additional Noops in file2, and check to see if they are somewhat spread out
def testNoopDistance(fileJson1, fileJson2):
    remain1 = [] #list of addresses of Noop Instructions in list 1
    remain2 = [] #list of addresses of Noop Instructions in list 2

    for op in fileJson1["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain1.append(op["offset"])

    for op in fileJson2["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain2.append(op["offset"])

    print ("Check only addional noops")
    print ("File1: ", remain1, len(remain1))
    print ("File2: ", remain2, len(remain2))

    noopsOnlyIn2 = [elem for elem in remain2 if elem not in remain1]
    print (noopsOnlyIn2)
    if(len(noopsOnlyIn2) > 3):
        dist1 = noopsOnlyIn2[math.floor(len(noopsOnlyIn2)/2)] - noopsOnlyIn2[0]
        dist2 = noopsOnlyIn2[len(noopsOnlyIn2) - 1] - noopsOnlyIn2[math.floor(len(noopsOnlyIn2)/2)]
        print ("Noop distance test score: ", (dist1+dist2)/2)
        return (dist1+dist2)/2
    else:
        print ("Noop distance test score: 0")
        return 0


#Check the similarity (0 = different, 1 = similar) in Noop location/distribution between the two files.  If one file has no noops, expect 0 as the score
def testJaccardSim(fileJson1, fileJson2):
    remain1 = set() #set of addresses of Noop Instructions in list 1
    remain2 = set() #set of addresses of Noop Instructions in list 2

    for op in fileJson1["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain1.add(op["offset"])

    for op in fileJson2["ops"]:
        if op["disasm"].find("nop") >= 0:
            remain2.add(op["offset"])

    print ("Check Jaccard Similarity score for noops")
    print ("File1: ", remain1, len(remain1))
    print ("File2: ", remain2, len(remain2))

    if len(remain1 | remain2):
        jaccard = len(remain1 & remain2) / len(remain1 | remain2)
    else: #both are empty sets
        jaccard = 0

    print ("Jaccard similarity test score: ", jaccard)
    return jaccard

#Creates list of results from tests
def testList(listFile):
    if filetype == "csv":
        retfile.append("File1,File2,Size Diff,Alloc Diff, Noop Line Diff, Noop Diff based on Offsets, Noop Jaccard Score Index\n")
    temp = ""
    f = open(listFile, "r")
    fl =f.readlines()
    for x in fl:
        files = x.strip('\n').split(',')
        r = test(files[0], files[1])
        if filetype == "csv" and r:
            temp += ','.join(files) + r
            temp += "\n"
            retfile.append(temp)
            temp = ""
    f.close()
    if filetype == "csv":
        rf = open("result.csv", "w+")
        for l in retfile:
            rf.write(l)
        rf.close()


if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        if len(sys.argv) == 3:
            if(sys.argv[1] == "--list" or sys.argv[1] == "-l" and sys.argv[2] != ""):
                print ("Runnin Scoring Test on List: " + sys.argv[2])
                testList(sys.argv[2])
            else:
                print ("Runnin Scoring Test on ", sys.argv[1], ",", sys.argv[2])
                test(sys.argv[1], sys.argv[2])
        elif len(sys.argv) == 4 and (sys.argv[1] == "--list" or sys.argv[1] == "-l") and sys.argv[2] != "" and sys.argv[3] == "-csv":
            print ("Creating a CSV for the Testlist: ", sys.argv[2])
            filetype = "csv"
            testList(sys.argv[2])
        else:
            print ("Arguments Incorrect")
    else:
        print ("Arguments Incorrect")
