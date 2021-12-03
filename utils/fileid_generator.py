# import os

# wavdir = '..\\wav'
# speaker_ids = [i for i in range(1, 21) if i%5 == 0]
# f_ids = open("data_test.fileids", "w")
# f_transcriptions = open("data_test.transcription", "w")
# file_count = 0

# for subdir, dirs, files in os.walk(wavdir) :
#   for dir in dirs :
#     if int(dir) in speaker_ids :
#       f_script = open(os.path.join(wavdir, dir, "script~"), "r")
#       i_wav = 1
#       for line in f_script :
#         if i_wav < 172 :
#           if line != '\n' :
#             f_ids.write("{}{}\n".format(dir, line[1:8]))
#             f_transcriptions.write("<s>{} </s> ({})\n".format(line[8:].rstrip().upper(), line[2:8]))
#             file_count += 1
#         else :
#           break
#         i_wav += 1
#       f_script.close()

# f_ids.close()
# f_transcriptions.close()
# print(file_count)
import os
wavdir = '../wav'
f_ids = open("commandreminder_train.fileids", "w")
for subdir, dirs, files in os.walk(wavdir):
    for dir in dirs : 
        if(dir != "nilam" and dir !="surya"):
            print(dir)
            speaker_dir = os.path.join(wavdir, dir)
            for sp_subdir, sp_dirs, sp_files in os.walk(speaker_dir):
                print(sp_files)
                sp_files.sort()
                for files in sp_files :
                    file_dir = dir+'/'+files.split(".")[0]
                    f_ids.write(file_dir+"\n")
f_ids.close()