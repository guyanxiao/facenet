import os
import numpy as np


def read_pairs(pairs_filename):
    pairs = []
    with open(pairs_filename, 'r') as f:
        for line in f.readlines()[1:]:
            pair = line.strip().split()
            pairs.append(pair)
    return np.array(pairs)


def get_names( pairs):
    name_list = []
    for pair in pairs:
        if len(pair) == 3:
            name0 = pair[0]
            name1 = pair[0]
        elif len(pair) == 4:
            name0 = pair[0]
            name1 = pair[2]
        name_list += (name0 , name1)

    return name_list

out = open("E:\\Study\\facenet-master\\facenet-master\\data\\lfw_pairs_ext_id.txt" ,"w")

pairs = read_pairs("E:\\Study\\facenet-master\\chengdu_6000_crop_160\\chengdu_6000_crop_160\\pairs_cd.txt")
names = get_names(pairs)

for i in range(6000):
    print(i)
    out.write(str(i+1) + "," + names[2*i] + "," + names[2*i+1] + "\n")

out.close()
