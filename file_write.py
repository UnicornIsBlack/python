man = []
other = []

try:
    file_read = open('sketch.txt')
    for each_line in file_read:
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    file_read.close()
except IOError:
    print('The datafile is missing!')


try:
    man_file = open('man.txt',"w")
    other_file = open('other.txt',"w")

    print(man,file=man_file)
    print(other,file=other_file)

    man_file.close()
    other_file.close()

except IOError:
    print('File error.')
