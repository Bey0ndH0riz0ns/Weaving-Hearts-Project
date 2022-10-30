from logging import exception
import re
rpyFile = open('script.rpy', 'r')
scpFile = open('Script.md', 'r')
lintedFile = open('linted.rpy','w')

Script = []

for line in scpFile.readlines():
    Script.append(line)

print(Script)

beginningPattern = re.compile("    \"{i}([A-Za-z]+, [A-Za-z]+ [0-9]\*){\/i}\"")
endPattern = re.compile("    \"{i}Scene End{\/i}\"")
dialogPattern = re.compile("(    ([a-z])+ +\".+\")|(    \"[A-Za-z ]+\" \".+\")|(    \"\(.+\)\"(?!.))")

Scene = False
for line in rpyFile.readlines():
    if beginningPattern.match(line):
        Scene = True 
    if dialogPattern.match(line) and Scene:
       print(line)
    if endPattern.match(line):
        Scene = False
    lintedFile.write(line)