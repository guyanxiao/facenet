# -*- coding: UTF-8 -*- 
import numpy as np
from numpy import linalg as la  
import os



def cosin(embeddings1, embeddings2):
    num = np.sum(embeddings1*embeddings2,axis=0)
    denom=la.norm(embeddings1,axis=0)*la.norm(embeddings2,axis=0)
    cos = (num/denom)*100
    return cos
    
    
embeddings1 = np.loadtxt ("E:\\Study\\facenet-master\\facenet-master\\data\\lfw_embeddings1.txt", dtype=float)
embeddings2 = np.loadtxt ("E:\\Study\\facenet-master\\facenet-master\\data\\lfw_embeddings2.txt", dtype=float)

out = open("E:\\Study\\facenet-master\\facenet-master\\data\\lfw_search_result_v1c_529000.txt" ,"w")
#print (embeddings1[0])
emb1_cnt = 1

for emb1 in embeddings1[:,::1]:
    #print (emb1)
    emb2_cnt = 1
    max_score = 0
    max_emb1_cnt = 0
    max_emb2_cnt = 0
    for emb2 in embeddings2[:,::1]:
        #print (emb2)
        cos = cosin(emb1 , emb2)
        if cos > max_score and cos < 100:
            max_score = cos
            max_emb1_cnt = emb1_cnt
            max_emb2_cnt = emb2_cnt
        emb2_cnt = emb2_cnt + 1
    out.write(str(max_emb1_cnt) + "," + str(max_emb2_cnt) + "," + str("%.2f"%max_score) + "\n")
    emb1_cnt = emb1_cnt + 1
    print(emb1_cnt)
    out.flush() 
out.close()
