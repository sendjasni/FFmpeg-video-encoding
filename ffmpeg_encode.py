import os
import subprocess

# path to ffmpeg bin
FFMPEG_BIN = 'ffmpeg'

# params for video encoding
WIDTH_X_HEIGHT = '1024x720'
FRAME_RATE = '30'


def get_video_input():
    cwd = os.getcwd()

    # get a list of files that have the extension y4m
    filelist = filter(lambda f: f.split('.')[-1] == 'y4m', os.listdir(cwd))
    filelist = sorted(filelist)

    # encode each file using FFmpeg + x265
    for file in filelist:
        encode_video(file)


def encode_video(file):
    name = ''.join(file.split('.')[:-1])
    output_name = '{}_encoded.h265'.format(name)

    try:
        
        encode_command = [FFMPEG_BIN,'-i',file, '-s',WIDTH_X_HEIGHT,'-r', FRAME_RATE,'-c:v','libx265', '-c:a','copy', output_name ]
        subprocess.call(encode_command)  # encode the video!
    
    except  subprocess.CalledProcessError as err:
        ret =   err.returncode
        if ret in (1, 2):
            print('the command failed')
        elif ret in (3, 4, 5):
            print('the command failed very much')

    decode_video(output_name)

def decode_video(encoded_file):
    input_file = ''.join(encoded_file.split('.')[:-1])
    decoded_file = '{}_decoded.y4m'.format(input_file)

    try:
        
        decode_command = [FFMPEG_BIN,'-i' ,encoded_file,'-f','yuv4mpegpipe', decoded_file]
        subprocess.call(decode_command)  # decode the video!

    except subprocess.CalledProcessError as err:
        ret =   err.returncode
        if ret in (1, 2):
            print('the command failed')
        elif ret in (3, 4, 5):
            print('the command failed very much')


if __name__ == "__main__":
    get_video_input()
