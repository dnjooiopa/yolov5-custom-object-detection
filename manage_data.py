import os

# get all image files
path_to_data = (os.getcwd()+"\\data\\image").replace('\\', '\\\\')
image_list = [i for i in os.listdir(path_to_data) if '.jpeg' in i]


percent_train = 0.7
percent_val = 0.2
percent_test = 1-(percent_train+percent_val)
