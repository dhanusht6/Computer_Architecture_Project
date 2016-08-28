'''

Coder: Dhanush Thimmappa.

Module: single cycle Micro-architecture with multi-core implementation with Load-Store ISA.

Date and Time: 02-20-2016 and 3:51 pm.

File Name: Finalcode.py

Related Files :
1. code.txt -> contains the assembly code in the hexadecimal format
2. data_64.txt -> contains the data to be encrypted , the 1024 data are arranged first followed be the 52 subkeys
3. output.txt -> contain the encrypted data fo the input file.
4. assembly_code.txt -> contains the assembly code of IDEA algorithm.

Functionality:
The python fuction simulator accepts the data and keys in the code.txt and data_64.txt and encrypts the data
and dumps the encrypted data to the output.txt file

File sources : All the related files has to be in the same directory of the Finalcode.py

Tools used :pycharm

python version : 2.7
'''
# Re-directing the output from console to the trace file
import sys
sys.stdout = open('trace.txt', 'w') # The output is directed to the trace.txt file

# setting the initial values for the variables
clock = 0
n=0
z= 0
R0 = 0
R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0
R6 = 0
R7 = 0
R8 = 0
R9 = 0
R10 = 0
R11 = 0
R12 = 0
R13 = 0
R14 = 0
R15 =0                # Is always reserved for zero
A1 = 0
A2 = 0
A3 = 0
RD1 = 0
RD2 = 0
WD3 = 0
SRCA = 0
SRCB = 0
IMM = 0
PC = 0
PC_BRANCH = 0
INST = 0  #
ALU_RESULT = 0
WRITE_DATA = 0
MEM_TO_REG =0
MEM_TO_WRITE=0
BRANCH = 0
ALU_CONTROL=0
ALU_SRC = 0
REG_DST = 0
REG_WRITE =0
PC_SRC = 0
ZERO =0
RESULT = 0
RS=0
RT=0
RD= 0
ADDRESS = 0
OPCODE = 0
A  = 0
READ_DATA = 0
NEXT_PC = 0
WD = 0

# setting the initial values for the variables

R_0 = 0
R_1 = 0
R_2 = 0
R_3 = 0
R_4 = 0
R_5 = 0
R_6 = 0
R_7 = 0
R_8 = 0
R_9 = 0
R_10 = 0
R_11 = 0
R_12 = 0
R_13 = 0
R_14 = 0
R_15 =0                # Is always reserved for zero
A_1 = 0
A_2 = 0
A_3 = 0
RD_1 = 0
RD_2 = 0
WD_3 = 0
SRCA1 = 0
SRCB1 = 0
IMM1 = 0
PC1 = 0
PC_BRANCH1 = 0
INST1 = 0  #
ALU_RESULT1 = 0
WRITE_DATA1 = 0
MEM_TO_REG1=0
MEM_TO_WRITE1=0
BRANCH1 = 0
ALU_CONTROL1= 0
ALU_SRC1 = 0
REG_DST1= 0
REG_WRITE1 =0
PC_SRC1 = 0
ZERO1 =0
RESULT1 = 0
RS1=0
RT1 =0
RD1= 0
ADDRESS1 = 0
OPCODE1 = 0
A1  = 0
READ_DATA1 = 0
NEXT_PC1 = 0
WD1 = 0

# open the file to read the data
with open("data_64.txt") as pointer:
    cache = map(str.strip,pointer)
m = 1024#raw_input("Enter the size of the data in bits for the encryption :")  # to read the data as 64 or the 1024 bits
m = int(m)  # converts the string to the int
n = m / 16  # to distinguish between the data in the first and rest as the keys
R_1 = R1 = n / 2
DATA_MEMORY = list( i for  i in range(n))
R_14 = R14 = n/8 -1

# setting the separate data cache for the cores.
cache1 = cache[0:n/2]+cache[n:n+52]
cache2 = cache[n/2:n]+cache[n:n+52]

with open('code.txt') as pointer1:  # The code in the hex 32 bit format is read and this is put into the data string
    code = map(str.rstrip, pointer1)
    code1  = code #setting the separate instruction cache for the cores.
    code2  = code

# Reading the code from the code.txt
# Instruction memory
def cycle(PC):

    global R0
    global R1
    global R2
    global R3
    global R4
    global R5
    global R6
    global R7
    global R8
    global R9
    global R10
    global R11
    global R12
    global R13
    global R14
    global R15             # Is always reserved for zero
    global A1
    global A2
    global A3
    global RD1
    global RD2
    global WD3
    global SRCA
    global SRCB
    global IMM
    global PC_BRANCH
    global INST
    global ALU_RESULT
    global WRITE_DATA
    global MEM_TO_REG
    global MEM_TO_WRITE
    global BRANCH
    global ALU_CONTROL
    global ALU_SRC
    global REG_DST
    global REG_WRITE
    global PC_SRC
    global ZERO
    global RESULT
    global RS
    global RT
    global RD
    global ADDRESS
    global OPCODE
    global A
    global READ_DATA
    global NEXT_PC
    global WD
    global clock
    global z
    global DATA_MEMORY
    #----------------------------------------------------------------------------
    # Instruction fetch stage
    #----------------------------------------------------------------------------

    INST = code1[PC]
    print "INST:",INST
    INST = int(INST,base=16)  # converting the instruction to the decimal format
    INST = '{:032b}'.format(INST)  # padding zeros to make the 16 bit instruction
    print "the PC :",PC
    #----------------------------------------------------------------------------
    # End of the  Instruction fetch stage
    #----------------------------------------------------------------------------


    #----------------------------------------------------------------------------
    #  Decode stage
    #----------------------------------------------------------------------------


    # Decode the instruction
    OPCODE = INST[0:6]
    RS     = INST[6:10]
    RT     = INST[10:14]
    RD     = INST[14:18]
    IMM     =  INST[18:32]
    ADDRESS  = INST[6:32]
    IMM = int(IMM, 2)

    #----------------------------------------------------------------------------
    #  End of the Decode stage
    #----------------------------------------------------------------------------
    # clock cycle calculation logic
    if OPCODE == '010001':
        clock  =  clock + 4
    else :
        clock = clock + 1

    print "clock:",clock
    if OPCODE == '001101': # if it is halt command , terminate the program
        z = 1 # settin z= 1 indicated the one core has completed the completion

    print "OPCODE:",OPCODE,"||","RS:",RS,"||","RT:",RT,"||","RD:",RD,"||","IMM:",IMM ,"||", "ADDRESS:",ADDRESS


    # Conrol Unit : Generation of the control signals from the OPOCDE which is decode from the INST
    #----------------------------------------------------------------------------
    #  Assigning the control signal depending on the OPCODE
    #----------------------------------------------------------------------------

    if OPCODE == '000000':
         #def Add():
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address;
        ZERO = 0
    elif OPCODE == '000001':
    #def Sub():
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '001'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0
    elif OPCODE == '000010':
    #def Mul():
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '010'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '000011':
    #def And():
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '011'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '000100':
    #def Or():
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '100'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0


    elif OPCODE == '000101':
    #def Xor():
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '101'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '000110':
    #def Load():
        MEM_TO_REG = 1  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 1  # Which source has to be selected between the immediate or the another source
        REG_DST = 0  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '000111':
    #def Store():
        MEM_TO_REG = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 1  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 1  # Which source has to be selected between the immediate or the another source
        REG_DST = 2  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 0  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '001000':
    #def Bz():
        MEM_TO_REG = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 2  # Required during the store operation in the memory cyle
        BRANCH = 1  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 2  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 2  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '001001':
    #def Beq():
        MEM_TO_REG = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 2  # Required during the store operation in the memory cyle
        BRANCH = 1  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 2  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 0  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '001010':
    #def Bp():
        MEM_TO_REG = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 2  # Required during the store operation in the memory cyle
        BRANCH = 1  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 2  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 0  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '001011':
    #def Bn():
        MEM_TO_REG = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 2  # Required during the store operation in the memory cyle
        BRANCH = 1  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 2  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 0  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '001100':          # JR
        MEM_TO_REG = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 2  # Required during the store operation in the memory cyle
        BRANCH = 1  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 2  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 2  # To enable the reg file during the write back to the register
        PC_SRC = 1  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '001101':
    #def Halt():
        MEM_TO_REG = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 2  # Required during the store operation in the memory cyle
        BRANCH = 2  # Required during the equal to zero AND branch operation
        ALU_CONTROL = 2  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 2  # Which source has to be selected between the immediate or the another source
        REG_DST = 2  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 2  # To enable the reg file during the write back to the register
        PC_SRC = 2  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0



    elif OPCODE == '001110':    #Load immediate
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 1  # Which source has to be selected between the immediate or the another source
        REG_DST = 0  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address\
        ZERO = 0

    elif OPCODE == '001111':    # Add  immediate
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 1  # Which source has to be selected between the immediate or the another source
        REG_DST = 0  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0


    elif OPCODE == '010000':    # Sub immediate
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '001'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 1  # Which source has to be selected between the immediate or the another source
        REG_DST = 0  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '010001':    #  MulMOD
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '010'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    elif OPCODE == '010010':    #  AddMod
        MEM_TO_REG = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE = 0  # Required during the store operation in the memory cyle
        BRANCH = 0  # Required during the equal to zero AND branch operation
        ALU_CONTROL = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC = 0  # Which source has to be selected between the immediate or the another source
        REG_DST = 1  # Which is the destination for the operation, in which register the result has to be stored
        REG_WRITE = 1  # To enable the reg file during the write back to the register
        PC_SRC = 0  # Control signal to select between the PC+4 and PC+4+address
        ZERO = 0

    # Register file

    # Register file and the decode operation

    A1 = RS
    A2 = RT
    # MUX for choosing the  destination
    if REG_DST == 0:
     A3 = RT
    elif REG_DST == 1:
     A3 = RD


    print "A1:",A1 ,"||","A2:" ,A2,"||" ,"A3:",A3,"||"
    # For choosing the RD1 based on the  A1
    if A1 == '0000':
        RD1 = R0
    elif A1 == '0001':
        RD1 = R1
    elif A1 == '0010':
        RD1 = R2
    elif A1 == '0011':
        RD1 = R3
    elif A1 == '0100':
        RD1 = R4
    elif A1 == '0101':
        RD1 = R5
    elif A1 == '0110':
        RD1 = R6
    elif A1 == '0111':
        RD1 = R7
    elif A1 == '1000':
        RD1 = R8
    elif A1 == '1001':
        RD1 = R9
    elif A1 == '1010':
        RD1 = R10
    elif A1 == '1011' :
        RD1 = R11
    elif A1 == '1100' :
        RD1 = R12
    elif A1 == '1101':
        RD1 = R13
    elif A1 == '1110' :
        RD1 = R14
    elif A1 ==  '1111':
        RD1 = R15

    # For choosing the RD2 based on the  A2
    if A2 == '0000' :
        RD2 = R0
    elif A2 == '0001':
        RD2 = R1
    elif A2 == '0010':
        RD2 = R2
    elif A2 == '0011':
        RD2 = R3
    elif A2 == '0100':
        RD2 = R4
    elif A2 == '0101':
        RD2 = R5
    elif A2 == '0110':
        RD2 = R6
    elif A2 == '0111':
        RD2 = R7
    elif A2 == '1000':
        RD2 = R8
    elif A2 == '1001':
        RD2 = R9
    elif A2 == '1010':
        RD2 = R10
    elif A2 == '1011' :
        RD2 = R11
    elif A2 == '1100' :
        RD2 = R12
    elif A2 == '1101':
        RD2 = R13
    elif A2 == '1110' :
        RD2 = R14
    elif A2 ==  '1111':
        RD2 = R15

    print "RD1: ",RD1 ,"||", "RD2:",RD2,"||"


    WRITE_DATA = RD2
    print "ALU_SRC:",ALU_SRC,"||","IMM:",IMM,"||"
    # -----------------------------------------------------------------------
    # ALU Operation and Execution of the Single Cycle
    #------------------------------------------------------------------------

    SRCA = RD1       #SRCA is choosen from the RD1
    # MUX implementation , ALU_SRC is the control signal
    # Based on the control signal the SCRB is selected from the RD2 and IMM
    if ALU_SRC == 0:
        SRCB = RD2
    elif ALU_SRC == 1:
        SRCB = IMM

    # Now we have selected what are the inputs SRCA and SRCB
    # we shall define the operation to be performend by the ALU based on the ALU_CONTROL
    print "SRCA: " ,SRCA ,"||", "SRCB:" , SRCB,"||"
    print "ALU_CONTROL:" ,ALU_CONTROL
    global a                       # for the type matching for the int
    a = 1234
    global b                       # for the type matching for the str
    b = 'abcd'

    if (type(b)==type(SRCA)):
        SRCA = int(SRCA,16)
    if (type(b)==type(SRCB)):
        SRCB  = int(SRCB,16)
    # Now the SRCA and SRCB are in the interger format
    if ALU_CONTROL == '000':        #ADD
       ALU_RESULT = SRCA + SRCB
       if SRCA == SRCB:             # for the branch SRCA will be zero and if they are equal the zero is set
            ZERO = 1
       print " ZERO:",ZERO

    elif ALU_CONTROL == '001' :      #SUB
      ALU_RESULT = SRCA - SRCB
      if SRCA == SRCB:
            ZERO = 1


    elif ALU_CONTROL == '010' :     # MUL
         if OPCODE == '010001':     # for the MULMOD
           if (SRCA == 0):
             SRCA = 65536
           elif (SRCB == 0):
             SRCB = 65536
         ALU_RESULT = SRCA * SRCB
         if SRCA == SRCB:
            ZERO = 1

    elif ALU_CONTROL == '011' :     # AND
        ALU_RESULT = SRCA & SRCB
        if SRCA == SRCB:
            ZERO = 1


    elif ALU_CONTROL == '100' :     # OR
        ALU_RESULT = SRCA | SRCB
        if SRCA == SRCB:
            ZERO = 1


    elif ALU_CONTROL == '101' :       # XOR
        ALU_RESULT = SRCA ^ SRCB
        if SRCA == SRCB:
            ZERO = 1


    global temp1,temp2
    if OPCODE =='010001': # MUL MOD
        if (type(b)==type(ALU_RESULT)):            # if str
         ALU_RESULT = int(ALU_RESULT,16)           # convert to int
        print "ALU_RESULT before the MULMOD:",ALU_RESULT
        ALU_RESULT = '{:032b}'.format(ALU_RESULT)
        temp1 = ALU_RESULT[0:16]
        temp2 = ALU_RESULT[16:32]
        temp1 = int(temp1,2)
        temp2 = int(temp2,2)
        print "temp1:",temp1 ,"||","temp2:",temp2
        if (temp2 - temp1) > 0:
            ALU_RESULT = temp2 - temp1
        elif(temp2 - temp1 ) < 0:
            ALU_RESULT  = temp2 - temp1 + 65537
        if (ALU_RESULT == 65536):
            ALU_RESULT = 0000
        print "ALU_RESULT after the MULMOD:", ALU_RESULT


    if OPCODE == '010010': # ADD MOD
        if (type(b)==type(ALU_RESULT)):            # if str
         ALU_RESULT = int(ALU_RESULT,16)           # convert to int
        ALU_RESULT = '{:032b}'.format(ALU_RESULT)  # convert the ALU_RESULT to the 32 bit binary
        temp2 = ALU_RESULT[16:32]                  # take only the last 16 bits that will be the result
        temp2 = int(temp2,2)                       # converting to the integer format
        ALU_RESULT = temp2

    #----------------------------------------------------------------------------
    #End of the ALU Operation
    #----------------------------------------------------------------------------



    #----------------------------------------------------------------------------
    # Memory stage for the load and the Store operation
    #----------------------------------------------------------------------------

    A = ALU_RESULT
    WD = WRITE_DATA
    READ_DATA = RD
    #----------------------------------------------------------------------------
    #End of the Memory operation
    #----------------------------------------------------------------------------



    #----------------------------------------------------------------------------
    #  Write Back stage
    #----------------------------------------------------------------------------

    if OPCODE == '000110':                   # if it is load instruction
         if (type(b)==type(ALU_RESULT)):     # if it is of type str
             ALU_RESULT = int(ALU_RESULT,16)
         READ_DATA = cache1[A]                # cache is the data memory


    if OPCODE == '000111':                 # for the storing of the data
        if (type(b)==type(A)):
            print "A",A ,"type A", type (A)
            A = int(A,16)
        cache1[A] = WD

    # MUX implementation for the select of the RESULT form the ALU_RESLUT and the READ_DATA
    if MEM_TO_REG == 0:
        RESULT = ALU_RESULT
    elif MEM_TO_REG == 1:
        RESULT = READ_DATA
    print "RESULT:",RESULT
    WD3 = RESULT
    if type(a) == type (WD3):
        WD3 = hex(WD3)
    # Selecting the register based on the A3
    if REG_WRITE == 1:
        if A3 == '0000':
            R0 = WD3
        elif A3 == '0001':
            R1 = WD3
        elif A3 == '0010':
            R2  = WD3
        elif A3 == '0011':
            R3  = WD3
        elif A3 == '0100':
            R4  = WD3
        elif A3 == '0101':
            R5  = WD3
        elif A3 == '0110':
            R6  = WD3
        elif A3 == '0111':
            R7  = WD3
        elif A3 == '1000':
            R8  = WD3
        elif A3 == '1001':
            R9  = WD3
        elif A3 == '1010':
            R10  = WD3
        elif A3 == '1011':
            R11  = WD3
        elif A3 == '1100':
            R12  = WD3
        elif A3 == '1101':
            R13  = WD3
        elif A3 == '1110':
            R14  = WD3
        elif A3 == '1111':
            R15  = WD3


    #----------------------------------------------------------------------------
    #End of the Write back stage
    #----------------------------------------------------------------------------



    #----------------------------------------------------------------------------
    #Desiding the next PC with the help of the PC_SRC signal from the PC+1 and imm+PC+1
    #----------------------------------------------------------------------------
    # for the branching calculation the PC_SRC
    PC_SRC = BRANCH * ZERO
    print "PC_SRC", PC_SRC,"||","BRANCH:",BRANCH,"||", "ZERO:",ZERO


    if OPCODE == '001010': #Bp
     if ALU_RESULT > 0 :
      PC_BRANCH = IMM - 1
      PC_SRC = 1

    elif OPCODE == '001011': #Bn
      if ALU_RESULT < 0 :
          PC_BRANCH = IMM -1
          PC_SRC = 1

    if OPCODE == '001100':                # JR
        if type(b)== type(ALU_RESULT):
          ALU_RESULT = int(ALU_RESULT)
        PC_BRANCH = ALU_RESULT - 1
        PC_SRC = 1

    # PC_BRANCH = IMM + PC +1
    else:
        PC_BRANCH = IMM - 1


    if PC_SRC == 0:
        NEXT_PC  = PC + 1
    elif PC_SRC == 1:
        NEXT_PC = PC_BRANCH
    print "The value of the PC After the PC calculation :",PC

    PC = NEXT_PC


    #print "PC:",PC , "PC_BRANCH:",PC_BRANCH , "NEXT_PC:",NEXT_PC
    #----------------------------------------------------------------------------
    # End of the NEXT PC decision
    #----------------------------------------------------------------------------

    #----------------------------------------------------------------------------
    # The status of the Register of the processor after the execution
    #----------------------------------------------------------------------------
    print "The values stored in the Registers are :"
    print "R0:",R0,"||","R1:",R1,"||","R2:",R2,"||","R3:",R3,"||"
    print "R4:",R4,"||","R5:",R5,"||","R6:",R6,"||","R7:",R7,"||"
    print "R8:",R8,"||","R9:",R9,"||","R10:",R10,"||","R11:",R11,"||"
    print "R12:",R12,"||","R13:",R13,"||","R14:",R14,"||","R15:",R15,"||"
    return PC


def cycle1(PC1):

    global R_0
    global R_1
    global R_2
    global R_3
    global R_4
    global R_5
    global R_6
    global R_7
    global R_8
    global R_9
    global R_10
    global R_11
    global R_12
    global R_13
    global R_14
    global R_15             # Is always reserved for ZERO1
    global A_1
    global A_2
    global A_3
    global RD_1
    global RD_2
    global WD_3
    global SRCA1
    global SRCB1
    global IMM1
    global PC_BRANCH1
    global INST1
    global ALU_RESULT1
    global WRITE_DATA1
    global MEM_TO_REG1
    global MEM_TO_WRITE1
    global BRANCH1
    global ALU_CONTROL1
    global ALU_SRC1
    global REG_DST1
    global REG_WRITE1
    global PC_SRC1
    global ZERO1
    global RESULT1
    global RS1
    global RT1
    global RD1
    global ADDRESS1
    global OPCODE1
    global A1
    global READ_DATA1
    global NEXT_PC1
    global WD1
    global z
    global DATA_MEMORY
    INST1 = code2[PC1]
    INST1 = int(INST1,base=16)  # converting the INST1ruction to the decimal format
    INST1 = '{:032b}'.format(INST1)  # padding ZERO1s to make the 16 bit INST1ruction



    # Decode the INST1ruction
    OPCODE1 = INST1[0:6]
    RS1     = INST1[6:10]
    RT1     = INST1[10:14]
    RD1     = INST1[14:18]
    IMM1     =  INST1[18:32]
    ADDRESS1  = INST1[6:32]
    IMM1 = int(IMM1, 2)

    print "clock:",
    print "OPCODE1:",OPCODE1,"||","RS1:",RS1,"||","RT1:",RT1,"||","RD1:",RD1,"||","IMM1:",IMM1 ,"||", "ADDRESS1:",ADDRESS1


    # Conrol Unit : Generation of the control signals from the OPOCDE which is decode from the INST1

    if OPCODE1 == '000000':
         #def ADD():
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1;
        ZERO1 = 0
    elif OPCODE1 == '000001':
    #def Sub():
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '001'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0
    elif OPCODE1 == '000010':
    #def Mul():
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '010'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '000011':
    #def And():
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '011'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '000100':
    #def Or():
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '100'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0


    elif OPCODE1 == '000101':
    #def Xor():
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '101'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '000110':
    #def Load():
        MEM_TO_REG1 = 1  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 1  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 0  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '000111':
    #def Store():
        MEM_TO_REG1 = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 1  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 1  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 2  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 0  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '001000':
    #def Bz():
        MEM_TO_REG1 = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 2  # Required during the store operation in the memory cyle
        BRANCH1 = 1  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 2  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 2  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '001001':
    #def Beq():
        MEM_TO_REG1 = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 2  # Required during the store operation in the memory cyle
        BRANCH1 = 1  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 2  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 0  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '001010':
    #def Bp():
        MEM_TO_REG1 = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 2  # Required during the store operation in the memory cyle
        BRANCH1 = 1  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 2  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 0  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '001011':
    #def Bn():
        MEM_TO_REG1 = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 2  # Required during the store operation in the memory cyle
        BRANCH1 = 1  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 2  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 0  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '001100':          # JR
        MEM_TO_REG1 = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 2  # Required during the store operation in the memory cyle
        BRANCH1 = 1  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 2  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 2  # To enable the reg file during the write back to the register
        PC_SRC1 = 1  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '001101':
    #def Halt():
        MEM_TO_REG1 = 2  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 2  # Required during the store operation in the memory cyle
        BRANCH1 = 2  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = 2  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 2  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 2  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 2  # To enable the reg file during the write back to the register
        PC_SRC1 = 2  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '001110':    #Load IMM1ediate
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 1  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 0  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1\
        ZERO1 = 0

    elif OPCODE1 == '001111':    # ADD2  IMM1ediate
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 1  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 0  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0


    elif OPCODE1 == '010000':    # Sub IMM1ediate
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '001'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 1  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 0  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '010001':    #  MulMOD
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '010'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    elif OPCODE1 == '010010':    #  AddMod
        MEM_TO_REG1 = 0  # Required for the selection of data from the ALU out or the data from the data memory to register file
        MEM_TO_WRITE1 = 0  # Required during the store operation in the memory cyle
        BRANCH1 = 0  # Required during the equal to ZERO1 AND BRANCH1 operation
        ALU_CONTROL1 = '000'  # Indicates which operation to be performed by the alu during the execution stage
        ALU_SRC1 = 0  # Which source has to be selected between the IMM1ediate or the another source
        REG_DST1 = 1  # Which is the destination for the operation, in which register the RESULT1 has to be stored
        REG_WRITE1 = 1  # To enable the reg file during the write back to the register
        PC_SRC1 = 0  # Control signal to select between the PC1+4 and PC1+4+ADDRESS1
        ZERO1 = 0

    # Register file

    # Register file and the decode operation

    A_1 = RS1
    A_2 = RT1
    # MUX for choosing the  destination
    if REG_DST1 == 0:
     A_3 = RT1
    elif REG_DST1 == 1:
     A_3 = RD1


    print "A_1:",A_1 ,"||","A_2:" ,A_2,"||" ,"A_3:",A_3,"||"
    # For choosing the RD_1 based on the  A_1
    if A_1 == '0000':
        RD_1 = R_0
    elif A_1 == '0001':
        RD_1 = R_1
    elif A_1 == '0010':
        RD_1 = R_2
    elif A_1 == '0011':
        RD_1 = R_3
    elif A_1 == '0100':
        RD_1 = R_4
    elif A_1 == '0101':
        RD_1 = R_5
    elif A_1 == '0110':
        RD_1 = R_6
    elif A_1 == '0111':
        RD_1 = R_7
    elif A_1 == '1000':
        RD_1 = R_8
    elif A_1 == '1001':
        RD_1 = R_9
    elif A_1 == '1010':
        RD_1 = R_10
    elif A_1 == '1011' :
        RD_1 = R_11
    elif A_1 == '1100' :
        RD_1 = R_12
    elif A_1 == '1101':
        RD_1 = R_13
    elif A_1 == '1110' :
        RD_1 = R_14
    elif A_1 ==  '1111':
        RD_1 = R_15

    # For choosing the RD_2 based on the  A_2
    if A_2 == '0000' :
        RD_2 = R_0
    elif A_2 == '0001':
        RD_2 = R_1
    elif A_2 == '0010':
        RD_2 = R_2
    elif A_2 == '0011':
        RD_2 = R_3
    elif A_2 == '0100':
        RD_2 = R_4
    elif A_2 == '0101':
        RD_2 = R_5
    elif A_2 == '0110':
        RD_2 = R_6
    elif A_2 == '0111':
        RD_2 = R_7
    elif A_2 == '1000':
        RD_2 = R_8
    elif A_2 == '1001':
        RD_2 = R_9
    elif A_2 == '1010':
        RD_2 = R_10
    elif A_2 == '1011' :
        RD_2 = R_11
    elif A_2 == '1100' :
        RD_2 = R_12
    elif A_2 == '1101':
        RD_2 = R_13
    elif A_2 == '1110' :
        RD_2 = R_14
    elif A_2 ==  '1111':
        RD_2 = R_15

    print "RD_1: ",RD_1 ,"||", "RD_2:",RD_2,"||"


    WRITE_DATA1 = RD_2
    print "ALU_SRC1:",ALU_SRC1,"||","IMM1:",IMM1,"||"
    # -----------------------------------------------------------------------
    # ALU Operation and Execution of the Single Cycle
    #------------------------------------------------------------------------

    SRCA1 = RD_1       #SRCA1 is choosen from the RD_1
    # MUX implementation , ALU_SRC1 is the control signal
    # Based on the control signal the SCRB is selected from the RD_2 and IMM1
    if ALU_SRC1 == 0:
        SRCB1 = RD_2
    elif ALU_SRC1 == 1:
        SRCB1 = IMM1

    # Now we have selected what are the inputs SRCA1 and SRCB1
    # we shall define the operation to be performend by the ALU based on the ALU_CONTROL1
    print "SRCA1: " ,SRCA1 ,"||", "SRCB1:" , SRCB1,"||"
    print "ALU_CONTROL1:" ,ALU_CONTROL1
    global A1                       # for the type matching for the int
    A1 = 1234
    global b                       # for the type matching for the str
    b = 'abcd'

    if (type(b)==type(SRCA1)):
        SRCA1 = int(SRCA1,16)
    if (type(b)==type(SRCB1)):
        SRCB1  = int(SRCB1,16)
    # Now the SRCA1 and SRCB1 are in the interger format
    if ALU_CONTROL1 == '000':        #ADD2
       ALU_RESULT1 = SRCA1 + SRCB1
       if SRCA1 == SRCB1:             # for the BRANCH1 SRCA1 will be ZERO1 and if they are equal the ZERO1 is set
            ZERO1 = 1
       print " ZERO1:",ZERO1

    elif ALU_CONTROL1 == '001' :      #SUB
      ALU_RESULT1 = SRCA1 - SRCB1
      if SRCA1 == SRCB1:
            ZERO1 = 1


    elif ALU_CONTROL1 == '010' :     # MUL
         if OPCODE1 == '010001':     # for the MULMOD
           if (SRCA1 == 0):
             SRCA1 = 65536
           elif (SRCB1 == 0):
             SRCB1 = 65536
         ALU_RESULT1 = SRCA1 * SRCB1
         if SRCA1 == SRCB1:
            ZERO1 = 1

    elif ALU_CONTROL1 == '011' :     # AND
        ALU_RESULT1 = SRCA1 & SRCB1
        if SRCA1 == SRCB1:
            ZERO1 = 1


    elif ALU_CONTROL1 == '100' :     # OR
        ALU_RESULT1 = SRCA1 | SRCB1
        if SRCA1 == SRCB1:
            ZERO1 = 1


    elif ALU_CONTROL1 == '101' :       # XOR
        ALU_RESULT1 = SRCA1 ^ SRCB1
        if SRCA1 == SRCB1:
            ZERO1 = 1


    global temp1,temp2
    if OPCODE1 =='010001': # MUL MOD
        if (type(b)==type(ALU_RESULT1)):            # if str
         ALU_RESULT1 = int(ALU_RESULT1,16)           # convert to int
        print "ALU_RESULT1 before the MULMOD:",ALU_RESULT1
        ALU_RESULT1 = '{:032b}'.format(ALU_RESULT1)
        temp1 = ALU_RESULT1[0:16]
        temp2 = ALU_RESULT1[16:32]
        temp1 = int(temp1,2)
        temp2 = int(temp2,2)
        print "temp1:",temp1 ,"||","temp2:",temp2
        if (temp2 - temp1) > 0:
            ALU_RESULT1 = temp2 - temp1
        elif(temp2 - temp1 ) < 0:
            ALU_RESULT1  = temp2 - temp1 + 65537
        if (ALU_RESULT1 == 65536):
            ALU_RESULT1 = 0000
        print "ALU_RESULT1 after the MULMOD:", ALU_RESULT1


    if OPCODE1 == '010010': # ADD2 MOD
        if (type(b)==type(ALU_RESULT1)):            # if str
         ALU_RESULT1 = int(ALU_RESULT1,16)           # convert to int
        ALU_RESULT1 = '{:032b}'.format(ALU_RESULT1)  # convert the ALU_RESULT1 to the 32 bit binary
        temp2 = ALU_RESULT1[16:32]                  # take only the last 16 bits that will be the RESULT1
        temp2 = int(temp2,2)                       # converting to the integer format
        ALU_RESULT1 = temp2

    #----------------------------------------------------------------------------
    #End of the ALU Operation
    #----------------------------------------------------------------------------



    #----------------------------------------------------------------------------
    # Memory stage for the load and the Store operation
    #----------------------------------------------------------------------------

    A1 = ALU_RESULT1
    WD1 = WRITE_DATA1
    READ_DATA1 = RD1

    #----------------------------------------------------------------------------
    #End of the Memory operation
    #----------------------------------------------------------------------------



    #----------------------------------------------------------------------------
    #  Write Back stage
    #----------------------------------------------------------------------------

    if OPCODE1 == '000110':                   # if it is load INST1ruction
         if (type(b)==type(ALU_RESULT1)):     # if it is of type str
             ALU_RESULT1 = int(ALU_RESULT1,16)
         READ_DATA1 = cache2[ALU_RESULT1]                # cache is the data memory
         print "alu RESULT1 :",ALU_RESULT1
         print "The value of the READ_DATA1:",READ_DATA1
    if OPCODE1 == '000111':                 # for the storing of the data
        if (type(b)==type(A1)):
            print "A1",A1 ,"type A1", type (A1)
            A1 = int(A1,16)
        cache2[A1] = WD1

    print " the value of the READ_DATA1:",READ_DATA1
    # MUX implementation for the select of the RESULT1 form the ALU_RESLUT and the READ_DATA1
    if MEM_TO_REG1 == 0:
        RESULT1 = ALU_RESULT1
    elif MEM_TO_REG1 == 1:
        RESULT1 = READ_DATA1

    WD3 = RESULT1
    if type(A1) == type (WD3):
        WD3 = hex(WD3)
    # Selecting the register based on the A_3
    if REG_WRITE1 == 1:
        if A_3 == '0000':
            R_0 = WD3
        elif A_3 == '0001':
            R_1 = WD3
        elif A_3 == '0010':
            R_2  = WD3
        elif A_3 == '0011':
            R_3  = WD3
        elif A_3 == '0100':
            R_4  = WD3
        elif A_3 == '0101':
            R_5  = WD3
        elif A_3 == '0110':
            R_6  = WD3
        elif A_3 == '0111':
            R_7  = WD3
        elif A_3 == '1000':
            R_8  = WD3
        elif A_3 == '1001':
            R_9  = WD3
        elif A_3 == '1010':
            R_10  = WD3
        elif A_3 == '1011':
            R_11  = WD3
        elif A_3 == '1100':
            R_12  = WD3
        elif A_3 == '1101':
            R_13  = WD3
        elif A_3 == '1110':
            R_14  = WD3
        elif A_3 == '1111':
            R_15  = WD3



    #----------------------------------------------------------------------------
    #End of the Write back stage
    #----------------------------------------------------------------------------



    #----------------------------------------------------------------------------
    #Desiding the next PC1 with the help of the PC_SRC1 signal from the PC1+1 and IMM1+PC1+1
    #----------------------------------------------------------------------------
    # for the BRANCH1ing calculation the PC_SRC1
    PC_SRC1 = BRANCH1 * ZERO1
    print "PC_SRC1", PC_SRC1,"||","BRANCH1:",BRANCH1,"||", "ZERO1:",ZERO1


    if OPCODE1 == '001010': #Bp
     if ALU_RESULT1 > 0 :
      PC_BRANCH1 = IMM1 - 1
      PC_SRC1 = 1

    elif OPCODE1 == '001011': #Bn
      if ALU_RESULT1 < 0 :
          PC_BRANCH1 = IMM1 -1
          PC_SRC1 = 1

    if OPCODE1 == '001100':                # JR
        if type(b)== type(ALU_RESULT1):
          ALU_RESULT1 = int(ALU_RESULT1)
        PC_BRANCH1 = ALU_RESULT1 - 1
        PC_SRC1 = 1

    # PC_BRANCH1 = IMM1 + PC1 +1
    else:
        PC_BRANCH1 = IMM1 - 1


    if PC_SRC1 == 0:
        NEXT_PC1  = PC1 + 1
    elif PC_SRC1 == 1:
        NEXT_PC1 = PC_BRANCH1
    print "The value of the PC1 After the PC1 calculation :",PC1

    PC1 = NEXT_PC1


    #print "PC1:",PC1 , "PC_BRANCH1:",PC_BRANCH1, "NEXT_PC1:",NEXT_PC1
    #----------------------------------------------------------------------------
    # End of the NEXT PC1 decision
    #----------------------------------------------------------------------------



    #clock logic


    print "The values stored in the Registers are :"
    print "R_0:",R_0,"||","R_1:",R_1,"||","R_2:",R_2,"||","R_3:",R_3,"||"
    print "R_4:",R_4,"||","R_5:",R_5,"||","R_6:",R_6,"||","R_7:",R_7,"||"
    print "R_8:",R_8,"||","R_9:",R_9,"||","R_10:",R_10,"||","R_11:",R_11,"||"
    print "R_12:",R_12,"||","R_13:",R_13,"||","R_14:",R_14,"||","R_15:",R_15,"||"
    if OPCODE1 == '001101':
     print "------------------------------------------------------------------------------------------"
     print "clock cycle is :",clock
     DATA_MEMORY = cache1[0:n/2]+cache2[0:n/2]
     print "DATA_MEMORY:",DATA_MEMORY
     with open('output.txt', 'w') as file:   # output the encrypted data to the output.txt file
         for i in DATA_MEMORY:
          file.write("{}\n".format(i))
     print "------------------------------------------------------------------------------------------"
     if (z ==1):
        quit()
    return PC1


clock  = 0
while True:
 print "----------------------------------------------------------------------------------------------------------------"
 print "The value of the PC before execution :",PC
 PC = cycle(PC)
 print "The value of the PC after execution  :",PC
 print "----------------------------------------------------------------------------------------------------------------"
 print "----------------------------------------------------------------------------------------------------------------"
 print "The value of the PC1 before execution :",PC1
 PC1 = cycle1(PC1)
 print "The value of the PC1 after execution  :",PC1
 print "----------------------------------------------------------------------------------------------------------------"


