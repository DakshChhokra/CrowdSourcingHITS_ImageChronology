import random
import csv


image_access_dict = {
    "a-1":"https://nets213replicate.s3.us-east-2.amazonaws.com/a-1.png",
    "a-2":"https://nets213replicate.s3.us-east-2.amazonaws.com/a-2.png",
    "a-3":"https://nets213replicate.s3.us-east-2.amazonaws.com/a-3.png",
    "a-4":"https://nets213replicate.s3.us-east-2.amazonaws.com/a-4.png",
    "b-1":"https://nets213replicate.s3.us-east-2.amazonaws.com/b-1.png",
    "b-2":"https://nets213replicate.s3.us-east-2.amazonaws.com/b-2.png",
    "b-3":"https://nets213replicate.s3.us-east-2.amazonaws.com/b-3.png",
    "b-4":"https://nets213replicate.s3.us-east-2.amazonaws.com/b-4.png",
    "c-1":"https://nets213replicate.s3.us-east-2.amazonaws.com/c-1.png",
    "c-2":"https://nets213replicate.s3.us-east-2.amazonaws.com/c-2.png",
    "c-3":"https://nets213replicate.s3.us-east-2.amazonaws.com/c-3.png",
    "c-4":"https://nets213replicate.s3.us-east-2.amazonaws.com/c-4.png",
    "d-1":"https://nets213replicate.s3.us-east-2.amazonaws.com/d-1.png",
    "d-2":"https://nets213replicate.s3.us-east-2.amazonaws.com/d-2.png",
    "d-3":"https://nets213replicate.s3.us-east-2.amazonaws.com/d-3.png",
    "d-4":"https://nets213replicate.s3.us-east-2.amazonaws.com/d-4.png",
    "e-1":"https://nets213replicate.s3.us-east-2.amazonaws.com/e-1.png",
    "e-2":"https://nets213replicate.s3.us-east-2.amazonaws.com/e-2.png",
    "e-3":"https://nets213replicate.s3.us-east-2.amazonaws.com/e-3.png",
    "e-4":"https://nets213replicate.s3.us-east-2.amazonaws.com/e-4.png",
    "f-1":"https://nets213replicate.s3.us-east-2.amazonaws.com/f-1.png",
    "f-2":"https://nets213replicate.s3.us-east-2.amazonaws.com/f-2.png",
    "f-3":"https://nets213replicate.s3.us-east-2.amazonaws.com/f-3.png",
    "f-4":"https://nets213replicate.s3.us-east-2.amazonaws.com/f-4.png"
    }

def return_random_array_hard(letter):
    arr = [1, 2, 3, 4]
    random.shuffle(arr)
    ret_arr = [letter + "-" + str(x) for x in arr]
    return ret_arr

def return_random_array_medium(letter):
    arr = [1, 2, 3]
    random.shuffle(arr)
    ret_arr = [letter + "-" + str(x) for x in arr]
    return ret_arr

def return_random_array_easy(letter):
    arr = [1, 2]
    random.shuffle(arr)
    ret_arr = [letter + "-" + str(x) for x in arr]
    return ret_arr



# for x in 'abcdef':
#     print(return_random_array_hard(x))

# for x in 'abcdef':
#     print(return_random_array_medium(x))

# for x in 'abcdef':
#     print(return_random_array_easy(x))

easy_array = []
with open('easy.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "image_url_1", "image_url_2"])
    for letter in 'abcdef':
        row = []
        row.append(letter)
        keys = return_random_array_easy(letter)
        easy_array.append(keys)
        print(keys)
        for key in keys:
            row.append(image_access_dict[key])
        writer.writerow(row)

medium_array = []
with open('medium.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "image_url_1", "image_url_2", "image_url_3"])
    for letter in 'abcdef':
        row = []
        row.append(letter)
        keys = return_random_array_medium(letter)
        medium_array.append(keys)
        print(keys)
        for key in keys:
            row.append(image_access_dict[key])
        writer.writerow(row)

hard_array = []
with open('hard.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "image_url_1", "image_url_2", "image_url_3", "image_url_4"])
    for letter in 'abcdef':
        row = []
        row.append(letter)
        keys = return_random_array_hard(letter)
        hard_array.append(keys)
        print(keys)
        for key in keys:
            row.append(image_access_dict[key])
        writer.writerow(row)

with open('legend.txt', 'w+') as leg:
    leg.write("Easy\n")
    for x in easy_array:
        leg.write(str(x) + '\n')
    leg.write("\n\n\n")
    leg.write("Medium\n")
    for x in medium_array:
        leg.write(str(x) + '\n')
    leg.write("\n\n\n")
    leg.write("Hard\n")
    for x in hard_array:
        leg.write(str(x) + '\n')