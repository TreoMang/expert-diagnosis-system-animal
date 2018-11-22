import  re

# read file
file_data = open("simple.txt",mode='r')
data = file_data.readlines()
animal = []
#tach tung dong du lieu thanh cac gia tri cach nhau boi dau ","
for line in data:
    animal.append(line.split(','))

#cac truong du lieu cua tung dong
key = ['name','hair','toothed','backbone','tail','eggs',
                'feathers','airborne','domestic','fins','legs','predator']

# dictionary luu dac diem cua tung animal
diction = dict()
dic = dict()
for ani in animal:
    line2 = ani[-1]
    # bo dau \n cuoi dong
    ani[-1] = re.sub('\n', '', line2)
    dic2 = dict()
    k = 0
    for a in ani:
        dic2[key[k]] = a
        k +=1

    diction[ani[0]] = dic2
    dic[ani[0]] = diction[ani[0]].copy()
    del dic[ani[0]]['name']

file_data.close()


