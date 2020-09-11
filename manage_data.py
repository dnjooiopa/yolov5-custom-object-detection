import os
import random

# get all image files
path_to_data = os.getcwd().replace('\\', '/')+"/data/image"
image_list = [(path_to_data+"/"+i)
              for i in os.listdir(path_to_data) if ('.txt' not in i)]

# split data
percent_train = 0.7
percent_val = 0.2

train_len = int(len(image_list) * percent_train)
val_len = int(len(image_list) * percent_val)
test_len = len(image_list) - (train_len+val_len)
