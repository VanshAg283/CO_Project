# GIGAssembler and simulator
The project involves creating an assembler that translates assembly code into machine code (binary) for a specific architecture. The assembler parses the assembly instructions, converts them into their corresponding binary representations, and generates a binary executable file.

Once the binary file is generated, a simulator is implemented to emulate the behavior of the target architecture. The simulator reads and interprets the binary instructions, simulating the execution of the program. It emulates the processor's state, including registers, memory, and flags, to execute the binary instructions sequentially.
##  Instruction Set Architecture (ISA)
| Instruction  | Description                                | Mnemonic | Type|
|--------------|--------------------------------------------|----------|-----|
| 00000        | Addition: Performs reg1 = reg2 + reg3. If the computation overflows, set overflow flag and write 0 to reg1. | add reg1 reg2 reg3 | A |
| 00001        | Subtraction: Performs reg1 = reg2 - reg3. If reg3 > reg2, write 0 to reg1 and set overflow flag. | sub reg1 reg2 reg3 | A |
| 00010        | Move Immediate: Performs reg1 = $Imm, where Imm is a 7-bit value. | mov reg1 $Imm | B |
| 00011        | Move Register: Move content of reg2 into reg1. | mov reg1 reg2 | C |
| 00100        | Load: Loads data from mem_addr into reg1. | ld reg1 mem_addr | D |
| 00101        | Store: Stores data from reg1 to mem_addr. | st reg1 mem_addr | D |
| 00110        | Multiply: Performs reg1 = reg2 x reg3. If the computation overflows, set overflow flag and write 0 to reg1. | mul reg1 reg2 reg3 | A |
| 00111        | Divide: Divide reg3 by reg4, store quotient in R0, remainder in R1. If reg4 is 0, set overflow flag and reset R0 and R1 to 0. | div reg3 reg4 | C |
| 01000        | Right Shift: Right shift reg1 by $Imm (7-bit value). | rs reg1 $Imm | B |
| 01001        | Left Shift: Left shift reg1 by $Imm (7-bit value).  | ls reg1 $Imm | B |
| 01010        | Exclusive OR: Bitwise XOR of reg2 and reg3, store result in reg1. | xor reg1 reg2 reg3 | A |
| 01011        | OR: Bitwise OR of reg2 and reg3, store result in reg1. | or reg1 reg2 reg3 | A |
| 01100        | AND: Bitwise AND of reg2 and reg3, store result in reg1. | and reg1 reg2 reg3 | A |
| 01101        | Invert: Bitwise NOT of reg2, store result in reg1. | not reg1 reg2 | C |
| 01110        | Compare: Compare reg1 and reg2, set up FLAGS register. | cmp reg1 reg2 | C |
| 01111        | Unconditional Jump: Jumps to mem_addr, where mem_addr is a memory address. | jmp mem_addr | E |
| 11100        | Jump If Less Than: Jump to mem_addr if the less than flag is set (less than flag = 1), where mem_addr is a memory address. | jlt mem_addr | E |
| 11101        | Jump If Greater Than: Jump to mem_addr if the greater than flag is set (greater than flag = 1), where mem_addr is a memory address. | jgt mem_addr | E |
| 11111        | Jump If Equal: Jump to mem_addr if the equal flag is set (equal flag = 1), where mem_addr is a memory address. | je mem_addr | E |
| 11010        | Halt: Stops the machine from executing until reset. | hlt | F |



## P-1 Assembly-to-Binary Assembler

This is an Assembly-to-Binary Assembler written in Python 3. It takes an input file code.txt containing assembly code and generates the corresponding binary code in the output file output.txt. If there are any errors in the assembly code, the assembler will print the errors and write them to output.txt as well.


This project is part of a college group project and is designed to fulfill the requirements specified in the instruction.pdf file, which provides the correct format and guidelines for writing assembly code.
## Prerequisites

To run the assembler, you need to have Python 3 installed on your system. You can check if Python is installed by running the following command in your terminal:

    python3 --version

If Python is not installed, you can download and install it from the official Python website: https://www.python.org/downloads/
## Usage

Place your assembly code in a file named code.txt. Make sure the assembly code follows the appropriate syntax and conventions.

Run the assembler by executing the following command in your terminal:

    python3 assembler.py

The assembler will read the code.txt file, process the assembly code, and generate the corresponding binary code in the output.txt file.

After execution, check the output.txt file for the generated binary code. If any errors were encountered during assembly, they will be printed and written to output.txt as well.

## Example
Here's an example of how the assembly code and output files would look like:

### "code.txt" (Input - Assembly Code)

    var var1
    var var2
    var var3
    ld R1 var1
    ld R2 var2
    st R3 var3
    jmp hlt_label
    add R1 R2 R3
    hlt_label: hlt
### "output.txt" (Output - Binary Code)
    0010000010000001
    0010000100000010
    0010100110000011
    0111100000000101
    0000000001010011
    1101000000000000
## P2 Simulator
The simulator should load a binary file into system memory and execute the code starting from address 0 until it encounters a "hlt" instruction.

Here's an overview of the distinct components mentioned in the question:

1) Memory (MEM): The memory component stores 256 bytes, initialized to 0s. It has read and write operations to access the data stored at a specific address.

2) Program Counter (PC): The program counter is a 7-bit register that keeps track of the current instruction's address. It is used to fetch the instruction from memory and update its value to point to the next instruction.

3) Register File (RF): The register file component is responsible for storing and accessing the values of different registers. It has 7 general-purpose registers (R0, R1, ..., R6) and a FLAGS register. The RF component provides read and write operations for these registers.

4) Execution Engine (EE): The execution engine fetches instructions from memory using the program counter, decodes the instruction, and executes it accordingly. It interacts with the memory and register file to perform operations specified by each instruction.

To solve this task, we can implement these components as separate classes: Memory, ProgramCounter, RegisterFile, and ExecutionEngine. The simulator will read the binary file, load it into memory, and start executing the instructions. After each instruction, it will output the program counter value and the values of the registers. Finally, it will print the memory dump of the entire memory.

have provided the Python code that implements these components and performs the simulation. You can run the code by providing a binary file as input, and it will execute the instructions, printing the program counter and register values, and displaying the memory dump.

Please make sure to adapt the code to match the specific instruction set and binary file format of your ISA, as the code provided is a general structure based on the given requirements.
