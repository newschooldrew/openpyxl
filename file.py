import os

path = os.getcwd()

content = ['this','is','a','test']

with open('testfile.txt','w') as f:
    for word in content:
        f.write(word+"\n")

with open('testfile.txt','r') as f:
    for line in f:
        line = line.strip()
        print(line)
        try:
            os.mkdir(path+"/"+line)
        except OSError:
            print("cant create folder",path+"\\"+line)
