import base64

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        record_data = fileObj.read()
        base64_data = base64.b64encode(record_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()

def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        origin_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(origin_data)
        fout.close()

def InputToFile(data, file):
    base64_data = str(data)
    origin_data = base64.b64decode(base64_data)
    fout = open(file, 'wb')
    fout.write(origin_data)
    fout.close()

def GetRoot(link):
    length = len(link)
    while length > 0:
        if link[length - 1] == '\\':
            return link[0:length]
        else:
            length -= 1
    raise Exception("Illegal Location")

x = 0
loc = 'defaultFileLocation'
data = 'defaultEncodedData'
name = 'defaultOutputName'
root = 'defaultRoot'

while x != 1 and x != 2 and x != 3:
    print("Press 1 to encode and 2 to decode data and 3 to decode files")
    x = int(input())
if x == 1:
    print("Please input the location of the file")
    loc = input()
    print("Please input the output file name")
    name = input()
    root = GetRoot(loc)
    name = root + name
    ToBase64(loc, name)
    print('The output is in the folder of the file')
elif x == 2:
    print("Please input the raw encoded data")
    data = input()
    print("Please input the output file name")
    name = input()
    InputToFile(data, name)
    print('The output is in the folder of this script')
elif x == 3:
    print('Please input the location of the base64 text')
    loc = input()
    print("Please input the output file name")
    name = input()
    root = GetRoot(loc)
    name = root + name
    ToFile(loc, name)
    print('The output is in the folder of the base64 txt')
else:
    print("Unknown Error Occured")