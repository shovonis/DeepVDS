import pandas as pd
from os import walk
import re
import datetime



def read_file(file_name):
    data = pd.read_csv(file_name)
    data['Time'] = pd.to_datetime(data['Time'], format='%Y.%m.%d %H:%M:%S:%f')
    return data


def get_image_file_names(image_dir):
    _, _, filenames = next(walk(image_dir))
    return filenames


def search_a_frame(frames, frame_number):
    matching = [match for match in frames if "Frame-" + str(frame_number) in match]
    return matching[0]


def get_frames_in_window(frames, frame_number, window_size=15):
    time_of_frame = matched_frame.replace("Frame-" + str(frame_number) + "-", '')
    time_of_frame = time_of_frame.replace(".png", '')
    time_of_frame = datetime.datetime.strptime(time_of_frame, '%H-%M-%S-%f').strftime('%H-%M-%S')
    print(time_of_frame)







### Main ###
file_name = '../../data/BeachWithTelePortation/verbal_feedback.csv'
image_directory = '../../data/BeachWithTelePortation/Frames'

# Read Sickness File and all Frames
df = read_file(file_name)
frame_list = get_image_file_names(image_directory)

for index, row in df.iterrows():
    current_frame = row['Frame']
    matched_frame = search_a_frame(frame_list, current_frame)
    print(matched_frame)
    get_frames_in_window(frame_list, current_frame, window_size=15)

