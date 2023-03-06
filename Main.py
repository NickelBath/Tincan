import sys

class Interpreter():
    pointer = 0
    pointertable = []
    programdata = ""
    
    iscompiled = input("TII-Shell >>> (C)ompiled or (I)nterpreted: ")
    if iscompiled  == "C" or "c":
        file = open('generated.py', 'w')
        file.write("import sys \n")
        file.write("# Program Compiled by the Tincan Compiler \n")
        file.write("pointertable = [] \n")
        file.write("pointer = 0; \n")
    # stack = []
    # if pointer > 255 or pointer < 0: pointer = 0

        
    while True:
        obj = input("TII-Shell >>>")
        for instruction in obj:
            # mathematical instructions
            if instruction == "+": 
                pointer += 1; pointertable.append(pointer)
                if iscompiled == "C" or "c":
                    file.write("pointer += 1; pointertable.append(pointer) \n")
            if instruction == "-": 
                pointer -= 1; pointertable.append(pointer)
                if iscompiled == "C" or "c":
                    file.write("pointer -= 1; pointertable.append(pointer) \n")
            if instruction == "$": 
                pointer *= 2; pointertable.append(pointer)
                if iscompiled == "C" or "c":
                    file.write("pointer *= 2; pointertable.append(pointer) \n")
            if instruction == "/":
                pointer /= 2; pointertable.append(pointer)
                if iscompiled == "C" or "c":
                    file.write("pointer /= 2; pointertable.append(pointer) \n")
                 

            if instruction == ":":
                print(pointer)
                if iscompiled == "C" or "c":
                    file.write("print(pointer) \n")
            if instruction == "§": 
                sys.exit()
            if instruction == "^": 
                pointer = 0; pointertable.append(pointer)
                if iscompiled == "C" or "c":
                    file.write("pointer = 0; pointertable.append(pointer) \n")
            # disabled if instruction == "%": string = ''.join(chr(i) for i in pointertable); print(string)
