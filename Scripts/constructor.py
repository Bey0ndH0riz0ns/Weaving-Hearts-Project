from logging import exception
import re
scp_file = open('Documents\Script.md', 'r')
rpy_file = open('script.rpy', 'r')

i = 1
start = 0
end = 0
#titles = []
#characters = []
#comment_lines = []
#dialog_lines = []
codes = []
code_id = 1
title_id = 1
comment_id = 1
dialog_id = 1

title_pattern = re.compile("    \"{i}([A-Za-z]+, [A-Za-z]+ [0-9]){\/i}\"")
comment_pattern = re.compile("(    #+[A-Za-z0-9,.-]+ [A-Za-z0-9, .-]*)")
character_dialog_pattern = re.compile("(    ([a-z])+ \".+\"{1})")
general_dialog_pattern = re.compile("(    \"[A-Za-z ]+\" \".+\"{1})")
misc_dialog_pattern = re.compile("(    \"[A-Za-z0-9 ,'.’…!?-]+\"(?!.))")
for line in rpy_file.readlines():
    if 'label start:' in line:
        codes.append({'id':code_id, 'type': 'start', 'row':i, 'text':line})
        start = i
        code_id = code_id + 1
        continue
    
    if 'return' in line:
        end = i
        codes.append({'id':code_id, 'type': 'end', 'row':i, 'text':line})
        break
    
    if start > 0:
        if title_pattern.match(line):
            #print(line)
            codes.append({'id':title_id, 'type': 'title', 'row':i, 'text':line})
            title_id = title_id + 1
            i = i + 1
            continue
        if comment_pattern.match(line):
            codes.append({'id':comment_id, 'type': 'comment', 'row':i, 'text':line})
            comment_id = comment_id + 1
            i = i + 1
            continue
        if character_dialog_pattern.match(line) or general_dialog_pattern.match(line) or misc_dialog_pattern.match(line):
            codes.append({'id':dialog_id, 'type': 'dialog', 'row':i, 'text':line})
            dialog_id = dialog_id + 1
            i = i + 1
            continue
        #if general_dialog_pattern.match(line):
        #    codes.append({'id':dialog_id, 'type': 'dialog', 'row':i, 'text':line})
        #    dialog_id = dialog_id + 1
        #    i = i + 1
        #    continue
        #if misc_dialog_pattern.match(line):
        #    codes.append({'id':id, 'type': 'dialog', 'row':i, 'text':line})
        #    id = id + 1
        #    i = i + 1
        #    continue
        codes.append({'id':code_id, 'type': 'code', 'row':i, 'text':line})
        code_id = code_id + 1
        i = i + 1
        continue

    codes.append({'id':code_id, 'type': 'code', 'row':i, 'text':line})
    code_id = code_id + 1  
    i = i + 1


#script_titles = []
#script_dialog = []
#script_comments = []
script = []
i = 1
title_id = 1
dialog_id = 1
comment_id = 1
script_title_pattern = re.compile("([A-Za-z]+, [A-Za-z]+ [0-9])")
script_dialog_pattern = re.compile("[a-z]+: \".+\"(?!.)")
script_comment_pattern = re.compile("#+[a-z ,-]+")
for line in scp_file.readlines():
    if script_title_pattern.match(line):
        script.append({'id':title_id, 'type': 'title', 'row': i, 'text': line})
        title_id = title_id + 1
    if script_dialog_pattern.match(line):
        script.append({'id':dialog_id, 'type': 'dialog', 'row': i, 'text': line})
        dialog_id = dialog_id + 1 # Regex is quite sensitive for trailing spaces
    if script_comment_pattern.match(line):
        script.append({'id':comment_id, 'type':'comment', 'row': i, 'text': line})
        comment_id = comment_id + 1
    i = i + 1

#for line in script:
#    print(line)

built_file = open('test.rpy','w')
# Possible problems: Things not found in the script and overly sensitive regex
breakLine = False
for line in codes:
    #print(line)
    #print(line)
    id = line['id']
    type = line['type']
    code = line['text']
    #print(code)
    #print(repr(code))
    #print(len(code))
    accepted_code = code
    if breakLine:
        if len(code) > 1:
            #print(type)
            #accepted_code = code
            if type == 'title' or type == 'comment' or type == 'dialog':
                for row in script:
                    if row['id'] == id and row['type'] == type:
                        stripped_line = code.strip()
                        checked_line = stripped_line[4:len(stripped_line)-5]
                        #print(checked_line)
                        #print(row['text'])
                        #print('C: ' + str(line))
                        #print('S: ' + str(row))
                        if checked_line not in row['text']:
                            #print(checked_line)
                            #print(row['text'])
                            accepted_code = '    "' + '{i}' + str(row['text'].strip()) + '{/i}"\n'
                            #print(test_code)

                        break

            #if 'title' in type:
            #    print(line)
            #if 'dialog' in type:
            #    print(code)
            built_file.write(accepted_code)
            breakLine = False
            continue
        continue

    if len(code) == 1:
        #print(repr(code))
        breakLine = True
    
    #if 'title' in type:
    #    print(code)
    #if 'dialog' in type:
    #    print(code)
    #if 'dialog' in type:
    #print(type)

    if type == 'title' or type == 'comment' or type == 'dialog':
        for row in script:
            if row['id'] == id and row['type'] == type:
                if type == 'dialog':
                    #stripped_line = code.strip()
                    code_words = re.findall("[\w'.]+",code.strip())    
                    script_words = re.findall("[\w'.]+",row['text'])
                    
                    #code_placement = []
                    #found_words = []
                    #for word in script_words[1:len(script_words)]:
                        #try:
                    #    if word in code_words:
                            
                    #        found_words.append(True)
                    #        continue
                        #except:
                    #    found_words.append(False)

                    print(code_words)
                    print(script_words)
                    #print(found_words)
                    #print(word_array)
                    #print(fix_array)
                    print('')
                    

                        #if word in code_words:



                    #code_index = 1
                    #script_index = 1
                    #word_array = []
                    #fix_array = []
                    #for word in code_words[1:len(code_words)]:
                        #if re.match("[cps0-9.]+", word):
                        #    code_index = code_index + 1
                        #    continue
                    #    if word in script_words[script_index]:
                    #        word_array.append(code_index)
                    #        code_index = code_index + 1
                    #        script_index = script_index + 1
                    #        continue
                    #    fix_array.append(code_index)
                    #    code_index = code_index + 1


                    #fix = False
                    #cases = []
                    #for word in script_words[1:len(script_words)]:
                    #    if not word in code_words:
                    #        fix = True
                    #        cases.append(False)
                    #    cases.append(True)
                    
                    #for word in code_words[1:len(code_words)]:
                    #    print(word)
                    
                    #print(code_words)
                    #print(script_words)
                    #print(word_array)
                    #print(fix_array)
                    #print('')

                    #print(code_words)
                    #print(script_words)
                    #print('')
                    #checked_line = stripped_line 
                    #print(stripped_line)
                    #print(row['text'])
                    #print('')
                    #if checked_line not in row['text']:
                    #    print('C: '+ stripped_line)
                    #    print('S: '+ row['text'])
                        #print('C: ' + str(line))
                        #print('S: ' + str(row))
                
                #stripped_line = code.strip()
                #print(stripped_line)
                #print(row['text'])
                #print('C: ' + str(line))
                #print('S: ' + str(row))
                break

    built_file.write(accepted_code)


#row = 1
#index = 0
#breakLine = False
#while True:
#    line = codes[index]['text']
    #print(codes[index])

    #if '\n' not in line:
        #built_file.write(line)
    #    breakLine = False
        #index = index + 1
        #row = row + 1
        #continue

    #if '\n' in line:
    #    built_file.write(line)
    #    breakLine = True
    #    index = index + 1
    #    row = row + 1
    #    continue
    
    
#    built_file.write(line)
    #if '\n' not in lastLine: 
    #    built_file.write(line)
    #else:
    #    if '\n' not in line:
    #        built_file.write(line)

#    if row == 100:
#        break

#    index = index + 1
#    row = row + 1
    #lastLine = line
    


#for thing in script_dialog:
#    print(thing)

#for thing in script_comments:
#    print(thing)

#for thing in lines:
#    print(thing)

#for thing in codes:
#    print(thing)

#for line in scp_file.readlines():
#    print(line)

#if character_dialog_pattern.match(line):
        #    lines.append({'row':i, 'text':line})
        #    continue
        #if general_dialog_pattern.match(line):
        #    lines.append({'row':i, 'text':line})
        #    continue
        #if misc_pattern.match(line):
        #    lines.append({'row':i, 'text':line})
        #    continue

