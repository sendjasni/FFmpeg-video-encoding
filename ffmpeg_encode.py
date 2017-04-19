import os, subprocess

# path to ffmpeg bin
FFMPEG_PATH = '/usr/local/bin/ffmpeg'
# params for video encoding
WIDTH = 1080
HEIGHT = 720
FRAME_RATE = 30


def get_video_input():
    cwd = os.getcwd()

    # get a list of files that have the extension y4m
    filelist = filter(lambda f: f.split('.')[-1] == 'y4m', os.listdir(cwd))
    filelist = sorted(filelist)

    # encode each file
    for file in filelist:
        encode_video(file)


def encode_video(file):
    name = ''.join(file.split('.')[:-1])
    output = '{}.h265'.format(name)

    #try:
    command = [FFMPEG_PATH, '-i', file, '-s', WIDTH, 'x', HEIGHT, '-r', FRAME_RATE, '-c:v libx265e -c:a copy',
                   '-threads', '8', output]
    subprocess.call(command)  # encode the video!
    # except  subprocess.CalledProcessError as err:
    #     et =   err.returncode
    #     if ret in (1, 2):
    #         print("the command failed")
    #     elif ret in (3, 4, 5):
    #         print("the command failed very much")


if __name__ == "__main__":
    get_video_input()

