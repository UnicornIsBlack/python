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
except IOError:
    print('The datafile is missing!')

finally:
    if 'file_read' in locals():
        file_read.close()


try:

    with open('man.txt',"w") as man_file:
        print(man,file=man_file)
    with open('other.txt',"w") as other_file:
        print(other,file=other_file)    
except IOError as err:
    print('File error:'+str(err))



