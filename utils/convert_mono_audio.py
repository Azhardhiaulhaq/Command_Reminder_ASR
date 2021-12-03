from pydub import AudioSegment
import os
wavdir = '../wav'
for subdir, dirs, files in os.walk(wavdir):
    for dir in dirs : 
        if(dir == "lingga" or dir =="wulantika" or dir =="widya"):
            speaker_dir = os.path.join(wavdir, dir)
            for sp_subdir, sp_dirs, sp_files in os.walk(speaker_dir):
                sp_files.sort()
                for files in sp_files :
                    file_dir = wavdir + '/' + dir+'/'+files.split(".")[0]+'.wav'
                    sound = AudioSegment.from_wav(file_dir)
                    sound = sound.set_channels(1)
                    sound.export(file_dir,format="wav")