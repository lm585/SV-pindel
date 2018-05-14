import sys


def main():

    if len(sys.argv) != 4:
        print "pindelToFormat.py exampleFile pindelFile DeletionSize"
        sys.exit()

    exampleFile = sys.argv[1]
    appendEnd = open( exampleFile, 'r')
    
    for line in appendEnd:
        tempList = line.split('\t')

    appendEnd.close()    

    x = 7
    append = ""
    while x < len(tempList)-1:
        if x < len(tempList)-1:
            append = append + tempList[x] + "\t"
            x = x + 1
        elif x == len(tempList)-1:
            append = append + tempList[x]

    pindelFile = sys.argv[2]
    pindel = open ( pindelFile, 'r')
    
    delete = int(sys.argv[3])

    for line in pindel:
        indexList = line.split()
        
        
        listLen = len(indexList)
    
        if listLen >= 16:
            
            if (int(indexList[9]) > int(indexList[10])):
               temp9 = indexList[9]
               temp10 = indexList[10]
               indexList[9] = temp10
               indexList[10] = temp9
            
            if (int(indexList[2]) >= delete):
                newFormat = []
                newFormat.append(indexList[7])
                newFormat.append(indexList[9])
                newFormat.append(indexList[9])  
                newFormat.append(indexList[7])
                newFormat.append(indexList[10]) 
                newFormat.append(indexList[10])
                newFormat.append(indexList[16])
                    
                inputString = ""
                for i in range(len(newFormat)):
                    
                    inputString = inputString + newFormat[i] + "\t"
    
                inputString = inputString + append
                inputString = inputString.strip('\n')
                print inputString

        else:
            pass
    pindel.close()
    
main()
