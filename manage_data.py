import os
import random

# get all image files
path_to_data = os.getcwd().replace('\\', '/')+"/data/image"
image_list = [(path_to_data+"/"+i)
              for i in os.listdir(path_to_data) if ('.txt' not in i)]

# split data
percent_train = 0.7
percent_val = 0.2

image_length = len(image_list)
train_len = int(image_length * percent_train)
val_len = int(image_length * percent_val)
test_len = image_length - (train_len+val_len)

temp_image_list = image_list
random.shuffle(temp_image_list)

train_list=temp_image_list[:train_len]
val_list=temp_image_list[train_len:train_len+val_len]
test_list=temp_image_list[train_len+val_len:]
