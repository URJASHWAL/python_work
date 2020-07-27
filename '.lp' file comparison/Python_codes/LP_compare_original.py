import re
pathSpark = r'spark_lp.lp'
pathPy = r'py_lp.lp'

def getHashes(paths):
    pythonLp = {}
    block = ""
    with open(paths,'r') as f:
        lines = f.readlines()
        for line in lines:
            if ("Min" in line or "Max" in line or "Par" in line or "Equal" in line) and block != "" :
                #print block
                block=re.split('<=|>=|=|<|>',block)[0]
                #print block[0]
                keyValues = block.split(':')
                key = keyValues[0]
                val = sorted(keyValues[1].replace(" ", "").replace("\n", ""))
                hashVal = hash("".join(val[:]))
                pythonLp[key] = [keyValues[1],hashVal]
                print key ,hashVal,"**********************"
                block = line
            else:
                block += line
    return pythonLp

keysPython = getHashes(pathPy)
keysSpark =  getHashes(pathSpark)
count_py = len(keysPython)
count_sp = len(keysSpark)

S_No = 1
for k in keysPython.keys():
    if keysSpark.has_key(k):
        if keysPython[k][1] != keysSpark[k][1]:
            print "------------------------------------------------", "S.NO",":", S_No, "---------------------------------------------------------------------------"
            print k+"\n","Python Value:\n",keysPython[k][0],"\n","Spark Value:\n",keysSpark[k][0]
            sparkset = set(keysSpark[k][0].replace("\n", "").split('+'))
            pythonset = set(keysPython[k][0].replace("\n", "").split('+'))
            print "\n","Differ values:\n",'Spark\'s values :', sparkset.difference(pythonset)
            print 'python\'s values :', pythonset.difference(sparkset)
            print "\n"
            S_No = S_No + 1
print "Number of python constraint:",count_py,"\n","Number of Spark constraint:",count_sp
