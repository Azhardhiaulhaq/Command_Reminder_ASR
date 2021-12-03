import pandas as pd
import numpy as np
import math

df = pd.read_csv('sentence.csv', delimiter=';',header=None)
# print(df[0][101])
f_ids = open("sentence_train.txt", "r")
f_trans = open("lm_train.txt", "w")
for ids in f_ids :
    sent = ids.split(" </s>")[0]
    f_trans.write(sent+"\n")

f_ids.close()
f_trans.close()