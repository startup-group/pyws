import os
import pickle

if os.path.exists("testfile//sketch.txt"):
    the_file = open("testfile//sketch.txt")
    print(the_file.readline(),end="")
    the_file.seek(0)
    for each_line in the_file:
        if not each_line.find(":") == -1:
            (role,said)=each_line.split(":",1)
            print(role,end="")
            print(" said: ",end="")
            print(said,end="")
        else:
            print(each_line,end="")
    the_file.close()
else:
    print("the file is missing...")

print("============================")

try:
    the_file = open("testfile//sketch.txt")
    print(the_file.readline(),end="")
    the_file.seek(0)
    for each_line in the_file:
        try:
            (role,said)=each_line.split(":",1)
            print(role,end="")
            print(" said: ",end="")
            print(said,end="")
        except ValueError:
            print(each_line,end="")
except IOError as err:
    print("the file is missing..." + str(err))
finally:
    if "the_file" in locals():
        the_file.close()

data = open("testfile//test.txt","w")
print("this is a test text...",file=data)
data.close()

try:
    with open("testfile//testwith.txt","w") as withdata:
        print("this is a text for with test...",file=withdata)
except IOError as err:
    print("Error msg is : " + str(err))

try:
    with open("testfile//pickle.txt","wb") as pdata:
        pickle.dump("this is a test pickle",pdata)
except pickle.PickleError as perr:
    print("error msg is : " + str(perr))
except IOError as err:
    print("IO error msg is " + str(err))

try:
    with open("testfile//pickle.txt","rb") as pfile:
        newdata = pickle.load(pfile)
        print(newdata)
except pickle.PickleError as perr:
    print("error msg is : " + str(perr))
except IOError as err:
    print("IO error msg is " + str(err))
