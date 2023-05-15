A = {"add":"00000","sub":"00001","mul":"00110","xor":"01001","or":"01011","and":"01100"}
B = {"mov":"00010","rs":"01000","ls":"01001"}
C = {"mov":"00011","div":"00111","not":"01101","cmp":"01110"}
D = {"ld":"00100","st":"00101"}
E = {"jmp":"01111","jlt":"11100","jgt":"11101","je":"11111"}
F = {"hlt":"11010"}
reg = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110"}
f_name = input("Enter file path:")
f = open(f_name,"r")
lines = f.readlines()
f.close()
errors = []
var_check = 1
var = []
lab = []
rest = []
ct = 0
for i in range(len(lines)):
    lines[i] = lines[i].strip() 
    if lines[i]:       
        lines[i] = lines[i].split()
        if lines[i][0] == "var" and var_check == 1:
            var.append(lines[i][1])
        elif lines[i][0] == "var" and var_check == 0:
            errors.append("Variables not declared at the beginning at line "+str(i+1)+"\n")
            ct += 1
        elif ":" in lines[i]:
            errors.append("General syntax error at line "+str(i+1)+"\n")
            ct += 1
        elif lines[i][0].endswith(":") and len(lines[i]) == 1:
            var_check = 0
            lab.append(lines[i][0][:-1])
            rest.append(lines[i][0:1])
        elif lines[i][0].endswith(":") and len(lines[i]) != 1:
            var_check = 0
            lab.append(lines[i][0][:-1])
            rest.append(lines[i][0:1])
            rest.append(lines[i][1:])
        elif lines[i][0] in A or lines[i][0] in B or lines[i][0] in C or lines[i][0] in D or lines[i][0] in E or lines[i][0] in F:
            var_check = 0
            rest.append(lines[i])
        else:
            var_check = 0
            errors.append("Typos in instruction name at line "+str(i+1)+"\n")
            ct += 1
    else:
        ct += 1
        continue

hlt_check = 0
assembly = []
inst = []
for i in range(len(rest)):
    if rest[i][0] in A:
        if len(rest[i]) != 4:
            errors.append("Syntax error at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][1] == "FLAGS" or rest[i][2] == "FLAGS" or rest[i][3] == "FLAGS":
            errors.append("Illegal use of FLAGS register at line "+str(ct+len(var)+i+1)+"\n")
        elif len(rest[i][1]) > 2 or rest[i][1] not in reg:
            errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
        elif len(rest[i][2]) > 2 or rest[i][2] not in reg:
            errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
        elif len(rest[i][3]) > 2 or rest[i][3] not in reg:
            errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
        else:
            assembly.append(A[rest[i][0]]+"00"+reg[rest[i][1]]+reg[rest[i][2]]+reg[rest[i][3]])
            inst.append(rest[i])
    elif rest[i][0] in B:
        if len(rest[i]) != 3:
                errors.append("Syntax error at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][0] == "mov" and (rest[i][2] in reg or rest[i][2] == "FLAGS"):
            if rest[i][1] == "FLAGS":
                errors.append("Illegal use of FLAGS register at line "+str(ct+len(var)+i+1)+"\n")
            elif len(rest[i][1]) > 2 or rest[i][1] not in reg:
                errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
            elif len(rest[i][2]) > 2 or rest[i][2] not in reg:
                errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
            else:
                assembly.append(C[rest[i][0]]+"00000"+reg[rest[i][1]]+reg[rest[i][2]])
                inst.append(rest[i])
        else: 
            if rest[i][1] == "FLAGS":
                errors.append("Illegal use of FLAGS register at line "+str(ct+len(var)+i+1)+"\n")
            elif len(rest[i][1]) > 2 or rest[i][1] not in reg:
                errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
            elif not(rest[i][2][1:].isdigit) or not(rest[i][2].startswith("$")):
                errors.append("Syntax error at line",ct+len(var)+i+1,"\n")
            elif int(rest[i][2][1:]) > 127 or int(rest[i][2][1:]) < 0:
                errors.append("Illegal Immediate values at line "+str(ct+len(var)+i+1)+"\n")
            else:
                assembly.append(B[rest[i][0]]+"0"+reg[rest[i][1]]+bin(int(rest[i][2][1:]))[2:].zfill(7))
                inst.append(rest[i])
    elif rest[i][0] in C:
        if len(rest[i]) != 3:
            errors.append("Syntax error at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][1] == "FLAGS" or rest[i][2] == "FLAGS":
            errors.append("Illegal use of FLAGS register at line "+str(ct+len(var)+i+1)+"\n")
        elif len(rest[i][1]) > 2 or rest[i][1] not in reg:
            errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
        elif len(rest[i][2]) > 2 or rest[i][2] not in reg:
            errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
        else:
            assembly.append(C[rest[i][0]]+"00000"+reg[rest[i][1]]+reg[rest[i][2]])
            inst.append(rest[i])
    elif rest[i][0] in D:
        if len(rest[i]) != 3:
            errors.append("Syntax error at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][1] == "FLAGS":
            errors.append("Illegal use of FLAGS register at line "+str(ct+len(var)+i+1)+"\n")
        elif len(rest[i][1]) > 2 or rest[i][1] not in reg:
            errors.append("Typo in register name at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][2] in lab:
            errors.append("Misuse of labels as variables at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][2] not in var:
            errors.append("Use of undefined variables at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[-1][0] not in F:
            errors.append("hlt not being used as the last instruction\n")
        else:
            c = 0
            for j in range(len(rest)):
                if not(rest[j][0].endswith(":")):
                    c += 1
            assembly.append(D[rest[i][0]]+"0"+reg[rest[i][1]]+bin(c+var.index(rest[i][2]))[2:].zfill(7))
            inst.append(rest[i])
    elif rest[i][0] in E:
        if len(rest[i]) != 2:
            errors.append("Syntax error at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][1] in var:
            errors.append("Misuse of variables as labels at line "+str(ct+len(var)+i+1)+"\n")
        elif rest[i][1] not in lab:
            errors.append("Use of undefined labels at line "+str(ct+len(var)+i+1)+"\n")
        else:
            cwl = 0
            for j in range(len(rest)):
                if not(rest[j][0].endswith(":")):
                    cwl += 1
                elif rest[j][0][:-1] == rest[i][1]:
                    break
            assembly.append(E[rest[i][0]]+"0000"+bin(cwl)[2:].zfill(7))
            inst.append(rest[i])
    elif rest[i][0][:-1] in lab:
        continue
    elif rest[i][0] in F:
        if len(rest[i]) != 1:
            errors.append("Syntax error at line "+str(ct+len(var)+i+1)+"\n")
        else:
            hlt_check = 1
            assembly.append(F[rest[i][0]]+"00000000000")
            inst.append(rest[i])
if hlt_check == 0:
    errors.append("Missing hlt instruction\n")
if inst[-1][0] not in F:
    errors.append("hlt not being used as the last instruction\n")

if len(errors) == 0:
    print("No errors found")
    with open ("assembly_code.txt","w") as assembly_file:
        for i in range(len(assembly)):
            assembly_file.write(assembly[i]+"\n")
else:
    print("Errors found")
    with open ("errors.txt","w") as error_file:
        error_file.writelines(errors)