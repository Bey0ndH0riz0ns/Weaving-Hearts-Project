from logging import exception
import re
rpyFile = open('script.rpy', 'r')
scpFile = open('Script.md', 'r')
lintedFile = open('linted.rpy','w')

#Script = []

SceneMap = {}

sceneBeginning = re.compile("[A-Za-z]+, [A-Za-z]+ [0-9]+")
sceneEnd = re.compile("-Scene End")

Scene = False
Index = 1
sceneLines = []
for data in scpFile.readlines():
    line = data.rstrip()
    if sceneBeginning.match(line):
        #print(line)
        Scene = True
        continue
    if sceneEnd.match(line):
        #print(line)
        SceneMap[str(Index)] = sceneLines
        Index = Index + 1
        Scene = False
        scene_lines = []
        continue
    if (Scene) and (len(line) > 1):
        #print(line)
        sceneLines.append(line)
        #print('')
        #print(line)
        #if not str(Index) in SceneMap:
        #    SceneMap[str(Index)] = [line]
        #    continue
        
#print('')
#print(SceneMap['3'])

#print(Script)

beginningPattern = re.compile("    \"{i}([A-Za-z]+, [A-Za-z]+ [0-9]\*){\/i}\"")
endPattern = re.compile("    \"{i}Scene End{\/i}\"")
dialogPattern = re.compile("(    ([a-z])+ +\".+\")|(    \"[A-Za-z ]+\" \".+\")|(    \"\(.+\)\"(?!.))")

sceneNumber = '0'
Scene = False
for line in rpyFile.readlines():
    if beginningPattern.match(line):
        print(line)
        print('')
        sceneNumber = re.findall('\d', line)[0]
        #print(sceneNumber)
        Scene = True 
    if dialogPattern.match(line) and Scene:
       for sceneLine in SceneMap[sceneNumber]:
            print(sceneLine) 
            print('')
       #print(line)
    if endPattern.match(line):
        print(line)
        print('')
        Scene = False
    lintedFile.write(line)