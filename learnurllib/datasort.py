import os

def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + "." + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(","))
    except IOError as err:
        print("File Error : + " + str(err))
        return (None)

with open("testfile//james.txt") as jaf:
    data = jaf.readline()
james = data.strip().split(",")

with open("testfile//julie.txt") as juf:
    data = juf.readline()
julie = data.strip().split(",")

with open("testfile//sarah.txt") as saf:
    data = saf.readline()
sarah = data.strip().split(",")
"""
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
"""
sarah = get_coach_data("testfile//sarah.txt")
sarah_data={}
sarah_data["name"] = sarah.pop(0)
sarah_data["birth"] = sarah.pop(0)
sarah_data["time"] = sarah
print(sarah_data["name"] + "'s fatest time is " + str(sorted(set([sanitize(t) for t in sarah_data["time"]]))[0:3]))