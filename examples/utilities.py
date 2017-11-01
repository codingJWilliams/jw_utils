def tryInt(inp):
    try: return int(inp)
    except: return inp
def findNameIndex(name, fileContent):
    for i, entry in list(enumerate(fileContent)):
        if name == entry and (i%2) == 0:
            return i
    return False
def getFile():
    with open("scores.txt") as f :
        return [ tryInt(x) for x in f.read().splitlines() ]
def saveFile(obj):
    with open("scores.txt", "w") as f:
        for entry in obj: print(entry, file=f)
def addPerson(name, score) :
    content = getFile()
    content += [ name, int(score) ]
    saveFile(content)
def updateScore(name, score):
    content = getFile()
    ind = findNameIndex( name, content )
    content[ ind + 1 ] = int(score)
    saveFile( content )
def getScore(name):
    content = getFile()
    return content[ findNameIndex(name, content) + 1 ]
