# this is a learning session from head first
friuts = ["Apple","Pear","Peach","Grape","Watermelon"]
print(len(friuts))
print(friuts)
friuts.append("Pine")
print(friuts)
friuts.extend(["Orange","Cucumber"])
print(friuts)
friuts.pop()
print(friuts)
friuts.pop(0)
print(friuts)
friuts.remove("Orange")
print(friuts)
friuts.insert(1,"Cucumber")
print(friuts)

for i in friuts:
    print(i)

count = 0
while count<len(friuts):
    print(friuts[count])
    count+=1

#dir(__builtins__)查看python标准库函数
bif = ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes',
       'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
       'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
       'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash',
       'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
       'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord',
       'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
       'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
print(len(bif))

complicatedList = ["a","b","c",["a1","b1","c1",["c2","c3"]]]
print(complicatedList)

for item in complicatedList:
    if isinstance(item,list):
        for it in item:
            print(it)
    else:
        print(item)

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

def print_lol2(the_list,level):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol2(each_item,level+1)
        else:
            for tabstop in range(level):
                print("\t",end="")
            print(each_item)

print_lol(complicatedList)
print_lol2(complicatedList,0)