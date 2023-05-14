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
rest = []
for i in range(len(lines)):
    lines[i] = lines[i].strip() 
    if lines[i]:       
        lines[i] = lines[i].split()
        if lines[i][0] == "var" and var_check == 1:
            var.append(lines[i][1])
        elif lines[i][0] == "var" and var_check == 0:
            errors.append("Variables not declared at the beginning at line",i+1,"\n")
        elif lines[i][0] in A or lines[i][0] in B or lines[i][0] in C or lines[i][0] in D or lines[i][0] in E or lines[i][0] in F:
            var_check = 0
            rest.append(lines[i])
        else:
            errors.append("Typos in instruction name at line",i+1,"\n")
