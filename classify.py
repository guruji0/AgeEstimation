import os


image_source = r"aglined faces"
dest_source_01 = r"0-3"
dest_source_02 = r"4-7"
dest_source_03 = r"8-13"
dest_source_04 = r"14-20"
dest_source_05 = r"21-24"
dest_source_06 = r"25-32"
dest_source_07 = r"33-37"
dest_source_08 = r"38-48"
dest_source_09 = r"49-59"
dest_source_10 = r"60-100"


for file in os.listdir(image_source):
    print(file[-6:-4])
    value = int(file[-6:-4])


    if 0 <= value <= 3:
        os.rename(image_source + '/' + file, dest_source_01 + '/' + file)
    elif 4 <= value <= 7:
        os.rename(image_source + '/' + file, dest_source_02 + '/' + file)
    elif 8 <= value <= 13:
        os.rename(image_source + '/' + file, dest_source_03 + '/' + file)
    elif 14 <= value <= 20:
        os.rename(image_source + '/' + file, dest_source_04 + '/' + file)
    elif 21 <= value <= 24:
        os.rename(image_source + '/' + file, dest_source_05 + '/' + file)
    elif 25 <= value <= 32:
        os.rename(image_source + '/' + file, dest_source_06 + '/' + file)
    elif 33 <= value <= 37:
        os.rename(image_source + '/' + file, dest_source_07 + '/' + file)
    elif 38 <= value <= 48:
        os.rename(image_source + '/' + file, dest_source_08 + '/' + file)
    elif 49 <= value <= 59:
        os.rename(image_source + '/' + file, dest_source_09 + '/' + file)
    elif 60 <= value <= 100:
        os.rename(image_source + '/' + file, dest_source_10 + '/' + file)








