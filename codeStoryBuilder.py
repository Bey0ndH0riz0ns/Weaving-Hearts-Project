from logging import exception
import re
rpyFile = open('script.rpy', 'r')
scpFile = open('TestScript3.md', 'r')
lintedFile = open('linted.rpy','w')

#Script = []

SceneMap = {}

sceneBeginning = re.compile("[A-Za-z]+, [A-Za-z]+ [0-9]+")
sceneEnd = re.compile("-Scene End")

Scene = False
Index = 0
sceneLines = []
row = 1
for data in scpFile.readlines():
    line = data.rstrip()
    if sceneBeginning.match(line):
        #print(line)
        Index = re.findall('\d', line)[0]
        Scene = True
        continue
    if sceneEnd.match(line):
        #print(line)
        SceneMap[str(Index)] = sceneLines
        Scene = False
        sceneLines = []
        row = 1
        continue
    if (Scene) and (len(line) > 1):
        #print(line)
        sceneLines.append({'row': row, 'line':line})
        row = row + 1
        #print('')
        #print(line)
        #if not str(Index) in SceneMap:
        #    SceneMap[str(Index)] = [line]
        #    continue
        
#print('')
#print(SceneMap['1'])

#print(len(SceneMap['1']))

#for data in SceneMap['1']:
#    print(data)
#    print('')

#for data in SceneMap['2']:
#    print(data)
#    print('')

#for data in SceneMap['3']:
#    print(data)
#    print('')

#print(Script)

beginningPattern = re.compile("    \"{i}([A-Za-z]+, [A-Za-z]+ [0-9]\*){\/i}\"")
endPattern = re.compile("    \"{i}Scene End{\/i}\"")
dialogPattern = re.compile("(    ([a-z])+ +\".+\")|(    \"[A-Za-z ]+\" \".+\")|(    \"\.\.\.\")")
commentPattern = re.compile("    #.+")
settingPattern = re.compile("    \"{i}[A-Za-z? ]+{\/i}\"")


sceneNumber = '0'
Scene = False
row = 0
for line in rpyFile.readlines():
    if beginningPattern.match(line):
        #print(line)
        #print('')
        sceneNumber = re.findall('\d', line)[0]
        #print(sceneNumber)
        Scene = True 
    if endPattern.match(line):
        #print(line)
        #print('')
        row = 0
        Scene = False
    if (dialogPattern.match(line) or commentPattern.match(line) or settingPattern.match(line)) and Scene and sceneNumber in SceneMap:
        print(row+1)
        print(line)
        #print(sceneNumber)
        print(SceneMap[sceneNumber][row])
        print('')
        
        
        #for data in SceneMap[sceneNumber]:
            #if data['row'] == row:
                #print(row)
                #print(line)
                #print(data)
            
            #print(data)
            #print('')
        
        #for sceneLine in SceneMap[sceneNumber]:
        #    if sceneLine['row'] == row:
        #        print(line)
        #        print(sceneLine['line'])
        #        print('')
        row = row + 1
       #for sceneLine in SceneMap[sceneNumber]:
            #lintedFile.write(sceneLine)
            #temp1 = line.split()
            #temp2 = sceneLine.split()
            #if temp1 in temp2:
            #    print(temp1)
            #    print(temp2)
            #    print('')
            #if line in sceneLine:
            #    print(sceneLine)
            #    print('')
        #    print(sceneLine) 
        #    print('')    
       #print(line)
    lintedFile.write(line)