import pandas as pd
import numpy as np
import math

df = pd.read_csv('sentence.csv', delimiter=';',header=None)
# print(df[0][101])
f_ids = open("commandreminder_test.fileids", "r")
f_trans = open("commandreminder_test.transcription", "w")
for ids in f_ids :
    dir_name = ids.split(".")[0]
    file_name = dir_name.split("/")[1]
    num = int(file_name.split("_")[1])
    sentence = df[0][num-1].upper()
    f_trans.write("<s> " + sentence + " </s> " + "(" + file_name.split("\n")[0]+")\n")

f_ids.close()
f_trans.close()
