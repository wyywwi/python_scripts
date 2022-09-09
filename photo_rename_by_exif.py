import exifread
import os
import json
import urllib.request

# please put this script in the target folder and run
# it will turn all the photos which has timestamp's name to "IMG_20XX0X0X_{the_post_name}"
# our code

# this function is for read image,the input is directory name
def read_directory(directory_name):
    imgname = []
    for filename in os.listdir(directory_name):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".JPG"):
            if not filename.startswith("IMG_20"):
                imgname.append(filename)
    return imgname

workpath = os.getcwd()

allfile = read_directory(workpath)

for eachfile in allfile:

    # 读取数据
    ourfile = open(eachfile, 'rb')
    tags = exifread.process_file(ourfile)

    # 打印所有照片信息，会以键值对的方法保存
    # print(tags)
    for tag in tags.keys():
        print("Key: {0}, value {1}".format(tag, tags[tag]))

    try:
        flag = 0
        timetag = str(tags['Image DateTime'])
    except:
        try:
            flag = 1
            timetag = str(tags['EXIF DateTimeOriginal'])
        except:
            continue

    # 格式化
    if flag == 0:
        timetag = str(tags['Image DateTime'])
    elif flag == 1:
        timetag = str(tags['EXIF DateTimeOriginal'])
    timetag = timetag.replace(':', '')
    timetag = timetag.replace(' ','_')

    # 检查是否为空
    if timetag == '':
        ourfile.close()
        continue

    #boundstr = 'IMG_' + timetag + '_' + eachfile
    # 文件名精简化
    boundstr = 'IMG_' + timetag + '_CH.JPG'
    srcname = os.path.join(workpath, eachfile)
    print('origin: ', srcname, '\r\n')
    destname = os.path.join(workpath, boundstr)
    print('after: ', destname, '\r\n')

    #解除占用
    ourfile.close()

    os.rename(srcname, destname)

    print("name ", eachfile, " has been changed to name ", boundstr)



