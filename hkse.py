import hashlib
import sys

def xorBytes(a, b):
    return bytes([_a ^ _b for _a, _b in zip(a, b)])

def firstHash(seed):
    return hashlib.sha256(seed.encode()).digest()

def nextHash(prevHash):
    return hashlib.sha256(prevHash).digest()

# Encryption function is also used to decrypt. It IS symmetrical after all!
def encryptFile(seed, inFile, outFile):
    currentHash = firstHash(seed)
    while True:
        # 32 bytes == 256 bits
        inBlock = inFile.read(32)
        if len(inBlock) == 0:
            break
        slicedHash = currentHash[0:len(inBlock)]
        outBlock = xorBytes(inBlock, slicedHash)
        outFile.write(outBlock)
        if len(inBlock) < 32:
            break
        currentHash = nextHash(currentHash)
    inFile.close()
    outFile.close()

if len(sys.argv) < 3:
    print("2 command line arguments are required. The first is the input file name, the second is the output file name.");
    exit()

inFileName = sys.argv[1]
outFileName = sys.argv[2]
try:
    inFile = open(inFileName, "rb");
except:
    print("Failed to open file '" + inFileName + "'")
    exit()

try:
    outFile = open(outFileName, "wb");
except:
    print("Failed to open or create file '" + outFileName + "'")

seed = input("Password: ")

encryptFile(seed, inFile, outFile)
