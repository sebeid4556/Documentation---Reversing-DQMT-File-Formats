import os
import sys

EXIT_ERROR = 1

def loadFile(path):
    try: 
        f = open(path, "rb")
    except:
        print("[!]Error: could not open %s" % path)
        sys.exit(EXIT_ERROR)
    buffer = f.read()
    f.close()
    return buffer

def frequencyAnalysisByte(buffer):
    size = len(buffer)
    freq = {}
    for i in range(0x00, 0x100):
        counter = 0
        for byte in buffer:
            if byte == i:
                counter += 1
        freq[i] = counter
    return freq

#returns element
def getMax(array):
    max = 0
    for i in range(0, len(array)):
        if array[i] > max:
            max = array[i]
    return last

#returns index of max element
def getMaxDict(dict):
    max = 0
    for key in dict:
        new = dict[key]
        if new > max:
            max = new
    return list(dict.values()).index(max)

def displayTopNResults(freq, n):
    ranked = {}
    for i in range(0, n):
        max_index = getMaxDict(freq)        
        max_key = list(freq.keys())[max_index]
        ranked[max_key] = list(freq.values())[max_index]
        freq.pop(max_key)
        if len(freq) == 0:
            break
    print("\n[+]Frequencies (Top %d):" % (n))
    for j in ranked:
        print("   0x%02X: %d" % (j, ranked[j]))

def findLengthOccurences(buffer):
    offsets = []
    size = len(buffer)
    for i in range(0, size):
        if buffer[i] == size:
            offsets.append(i)
    return offsets

def displayFLOResults(offsets, buffer):
    print("\n[+]File Size Occurences (1 Byte):")
    for entry in offsets:
        print("   0x%08X: %02X" % (entry, buffer[entry]))

def parseArguments():    
    argc = len(sys.argv)
    
    if argc < 2:
        if argc == 1:
            print("[+]scan.py [.bin path] [Top N results]\n\t-Perform frequency analysis on file")
        else: print("[!]Error: Path to file not provided.")
        sys.exit(1)
    elif argc > 3:
        print("[!]Error: Too many arguments.")
        sys.exit(1)    
    if not os.path.exists(sys.argv[1]):
        print("[!]Error: specified file/path does not exist.")
        sys.exit(1)
    return sys.argv

def main():
    args = parseArguments()
    print("[+]Scanning %s..." % (args[1]))
    buffer = loadFile(args[1])
    displayTopNResults(frequencyAnalysisByte(buffer), int(args[2]))
    displayFLOResults(findLengthOccurences(buffer), buffer)

if __name__ == "__main__":
    main()
