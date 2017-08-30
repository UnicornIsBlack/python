



with open('james.txt') as james_file:
    data=james_file.readline()
    james=data.strip().split(',')

with open('julie.txt') as julie_file:
    data=julie_file.readline()
    julie=data.strip().split(',')


with open('mikey.txt') as mikey_file:
    data=mikey_file.readline()
    mikey=data.strip().split(',')

with open('sarah.txt') as sarah_file:
    data=sarah_file.readline()
    sarah=data.strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)
