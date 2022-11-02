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
Index = 0
sceneLines = []
row = 1
for data in scpFile.readlines():
    line = data.rstrip()
    if sceneBeginning.match(line):
        Index = re.findall('\d', line)[0]
        Scene = True
        continue
    if sceneEnd.match(line):
        SceneMap[str(Index)] = sceneLines
        Scene = False
        sceneLines = []
        row = 1
        continue
    if (Scene) and (len(line) > 1):
        sceneLines.append({'row': row, 'line':line})
        row = row + 1
        
beginningPattern = re.compile("    \"{i}([A-Za-z]+, [A-Za-z]+ [0-9]\*){\/i}\"")
endPattern = re.compile("    \"{i}Scene End{\/i}\"")
dialogPattern = re.compile("(    ([a-z])+ +\".+\")|(    \"[A-Za-z ]+\" \".+\")|(    \"\.\.\.\")|(    \"\(.+\)\")") # Problems here
commentPattern = re.compile("    #.+")
settingPattern = re.compile("    \"{i}[A-Za-z? ]+{\/i}\"")

sceneNumber = '0'
Scene = False
row = 0
for data in rpyFile.readlines():
    line = data.rstrip()
    
    if beginningPattern.match(line):
        sceneNumber = re.findall('\d', line)[0]
        Scene = True 
    
    if endPattern.match(line):
        row = 0
        Scene = False
    
    if (dialogPattern.match(line) or commentPattern.match(line) or settingPattern.match(line)) and Scene and sceneNumber in SceneMap:
        #temp = re.sub('({[a-z]=[0-9.]+})|({i})|({\/i})', '',line.strip())
        temp = re.sub('({[a-z]+=[*0-9.]+})|({[a-z]+})|({\/[a-z]+})', '',line.strip())
        lineWords = re.findall('\w+',temp)
        sceneWords = re.findall('\w+',SceneMap[sceneNumber][row]['line'])
        
        if len(lineWords) == len(sceneWords):
            print(lineWords)
            print(sceneWords)
            print('')
        
        #print(re.findall('\w+',temp))
        #print(re.findall('\w+',SceneMap[sceneNumber][row]['line']))
        #print('')
        row = row + 1
        
    lintedFile.write(line)