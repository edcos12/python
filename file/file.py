list = ['football ', 'boxing ', 'tennis ', 'vollyball ', 'basketball']

file = open('D:\\Users\\edward\\codes\\Python\\lessons\\file\\teams.txt', 'w')

for item in list:
    file.write(f"{item}\n")

file.close()

file = open('D:\\Users\\edward\\codes\\Python\\lessons\\file\\teams.txt', 'r')
lines = file.readlines()
file.close()

lines[-1] = ' '
lines[0] = 'this is a new line'

file = open("D:\\Users\\edward\\codes\\Python\\lessons\\file\\teams.txt", "w")
for i in range(len(lines)):
    if i == len(lines)-1:
        file.write(lines[i])
    else:
        file.write(lines[i].strip() + "\n")

file.close()

file = open('D:\\Users\\edward\\codes\\Python\\lessons\\file\\teams.txt', 'r')
for line in file:
    print(line.strip())
file.close