



#with open("test.txt", 'r+', encoding='utf-8') as file: # Открываем файл
#   file.write(str("message.text") + '\n')
#   print(file.read())


text = [
'This is 1st line\n',
'This is 2nd line\n',
'This is 3rd line\n'
]

fp = open('test.txt', 'w')
fp.writelines(text)
fp.close()
#fp = open('test.txt', 'r')
#print(fp.read())


def replace_line(file_name, line_num, text):
    #print(text)
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    print(lines)
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

replace_line('test.txt', 1, 'Mage \n')

fp = open('test.txt', 'r')
print(fp.read())