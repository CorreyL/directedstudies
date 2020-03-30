import random

def instructiongenerator(seeds):

  random.seed(seeds[0])

  rtypeop = "0110011"
  rtypefun3 = ["000", "000", "001", "100", "101", "101", "110", "111"]
  rtypefun7 = ["0000000", "0100000", "0000000", "0000000", "0000000", 
  "0010011", "0000000", "0000000"]
  ldtypeop = "0000011"
  ldtypefun3 = ["000", "001", "010", "011", "100", "101", "110"]
  itypeop = "0010011"
  itypefun3 = ["000", "001", "100", "101", "101", "110", "111"]
  itypefun7 = ["0000000", "0000000", "0000000", "0000000", "0100000", "0000000",
   "0000000"]
  stypeop = "0100011"
  # only testing double word, more can be added if more tests are needed
  stypefun3 = ["000"]
  sbtypeop = "1100011"
  # only testing double word, more can be added if more tests are needed
  sbtypefun3 = ["000"]
  #read and write register numbers availible for use, also used for 5 bit immediates
  addresses = [ "00101", "00110", "00111", "01000", "01001", "10010","10011",
  "10100", "10101", "10110", "10111", "11000", "11001", "11010", "11011",
  "11100", "11101", "11110", "11111"]
  rtypeinst = []
  ldtypeinst = []
  itypeinst = []
  stypeinst = []
  sbtypeinst = []

  #Build R-type instructions

  #rs combinations
  readloc = []
  for i in range(0,len(rtypefun3)):
    readloc.append(random.choice(addresses) + random.choice(addresses))

  # concatenate rtype opcode and rd with all temp register locations
  r_op_rd = []
  for i in range(0,len(rtypefun3)):
    r_op_rd.append( random.choice(addresses) + rtypeop)

  # concatenate with funct 3
  r_op_rd_fun3 = []
  for i,funct in enumerate(rtypefun3):
    r_op_rd_fun3.append(funct + r_op_rd[i])

  # concatonate with read addresses
  r_op_rd_fun3_rs = []
  for i, loc in enumerate(readloc):
    r_op_rd_fun3_rs.append(loc + r_op_rd_fun3[i])

  # concatonate with funct 7
  for i, funct7 in enumerate(rtypefun7):
    rtypeinst.append(funct7 + r_op_rd_fun3_rs[i])

  #Build ld-type instructions

  # concatenate rtype opcode and rd with all temp register locations
  ld_op_rd = []
  for i in range(0,len(ldtypefun3)):
    ld_op_rd.append( random.choice(addresses) + ldtypeop)

  # concatenate with funct 3
  ld_op_rd_fun3 = []
  for i,funct in enumerate(ldtypefun3):
    ld_op_rd_fun3.append(funct + ld_op_rd[i])

  # concatonate with read addresses
  ld_op_rd_fun3_rs = []
  for i in range(0,len(ldtypefun3)):
    ld_op_rd_fun3_rs.append(random.choice(addresses) + ld_op_rd_fun3[i])

  # concatonate with immediate
  # for ease of testing always add 2 to whatever is in the rs1
  for i in range(0,len(ldtypefun3)):
    ldtypeinst.append("000000000010" + ld_op_rd_fun3_rs[i])

  random.seed(seeds[1])

  #Build I-type instructions

  #rs combinations
  readloc = []
  for i in range(0,len(itypefun3)):
    readloc.append(random.choice(addresses) + random.choice(addresses))

  # concatenate rtype opcode and rd with all temp register locations
  i_op_rd = []
  for i in range(0,len(itypefun3)):
    i_op_rd.append( random.choice(addresses) + itypeop)

  # concatenate with funct 3
  i_op_rd_fun3 = []
  for i,funct in enumerate(itypefun3):
    i_op_rd_fun3.append(funct + i_op_rd[i])

  # concatonate with read address
  i_op_rd_fun3_rs = []
  for i, loc in enumerate(readloc):
    i_op_rd_fun3_rs.append(loc + i_op_rd_fun3[i])

  # concatonate with funct 7/immediate
  for i, funct7 in enumerate(itypefun7):
    itypeinst.append(funct7 + i_op_rd_fun3_rs[i])

  random.seed(seeds[2])

  #Build S-type instructions

  #rs combinations
  readloc = []
  for i in range(0,len(stypefun3)):
    readloc.append(random.choice(addresses) + random.choice(addresses))

  # concatenate rtype opcode and immediate
  # always have immediate at 2 for testing ease
  s_op_imm = []
  for i in range(0,len(stypefun3)):
    s_op_imm.append( "00010" + stypeop)

  # concatenate with funct 3
  s_op_imm_fun3 = []
  for i,funct in enumerate(stypefun3):
    s_op_imm_fun3.append(funct + s_op_imm[i])

  # concatonate with read addresses
  s_op_imm_fun3_rs = []
  for i, loc in enumerate(readloc):
    s_op_imm_fun3_rs.append(loc + s_op_imm_fun3[i])

  # concatonate with immediate
  # always have immediate at 2 for testing ease
  for i in range(0,len(stypefun3)):
    stypeinst.append("0000000" + s_op_imm_fun3_rs[i])

  #Build Sb-type instructions

  #rs combinations
  readloc = []
  for i in range(0,len(sbtypefun3)):
    readloc.append(random.choice(addresses) + random.choice(addresses))

  # concatenate rtype opcode and immediate
  sb_op_imm = []
  for i in range(0,len(sbtypefun3)):
    sb_op_imm.append( "00100"+ sbtypeop)

  # concatenate with funct 3
  # always have immediate at 2 for testing ease
  sb_op_imm_fun3 = []
  for i,funct in enumerate(sbtypefun3):
    sb_op_imm_fun3.append(funct + sb_op_imm[i])

  # concatonate with read addresses
  sb_op_imm_fun3_rs = []
  for i, loc in enumerate(readloc):
    sb_op_imm_fun3_rs.append(loc + sb_op_imm_fun3[i])

  # concatonate with immediate
  # always have immediate at 2 for testing ease
  for i in range(0,len(sbtypefun3)):
    sbtypeinst.append("0000000" + sb_op_imm_fun3_rs[i])

  ''' build set up instructions to fill registers so they do not have unkown
  values, fill all useable registers with zeros to begin, add the 0 register
  with an all 0 instruction, pull 0 from the 0 address in data_mem'''
  setup = []
  
  # fill each address with 0 so we know what to expect in testing
  for address in addresses:
    setup.append("00000000000000000000" + address + "0000011")

  return(setup+rtypeinst+ldtypeinst+itypeinst+stypeinst+sbtypeinst)

def padinstruction(baselist, depth):

  instruction = baselist

  random.seed(8)

  # continually call the base constructor in order to fill mif
  while (depth - len(instruction) > 0):
    seeds = [random.randint(1,50),random.randint(1,50), random.randint(1,50)]
    newlist = instructiongenerator(seeds)
    instruction = instruction + newlist

  #likley this will result in overflow, reduce to necessary depth
  while (len(instruction) - depth > 0):
    instruction.pop()

  #double check nothing went wrong when filling to correct depth
  if (depth - len(instruction) != 0):
    print("there is an issue constructing the instructions")

  return(instruction)

def binarytonumeric(instruction):

  numericinstruction = []
  for i in instruction:
    numeric = int(i,2)
    numericinstruction.append(numeric)
  return(numericinstruction)

def createcsv(instruction, csvfilename):

  # create testing CSV
  cols = ("INSTURCTION TYPE,PC,INSTRUCTION,IMMEDIATE,FUNCT7,RS2,RS1,FUNCT3,RD,"+
  "OPCODE,BRANCH,MEMREAD,MEMTOREG,MEMWRITE,ALUOP,REGW,ALUOPCODE,ALUSRC,"+
  "DATA1OUT,DATA2OUT,DATA2IN,C,Z,ALUOUT,ADDR,WRDATAMEM,MEMOUT,WRDATAREG, REG5,"+
  "REG6, REG7, REG8, REG9, REG18, REG19, REG20, REG21, REG22, REG23, REG24,"+
  "REG25, REG26, REG27, REG28, REG29, REG30, REG31\n")
  name = []
  pc = []
  immediate = []
  funct7 = []
  rs2 = []
  rs1 = []
  funct3 = []
  rd = []
  opcode = []
  branch = []
  memread = []
  memtoreg = []
  memwrite = []
  aluop = []
  regw = []
  aluopcode = []
  alusrc = []
  data1out = []
  data2out = []
  data2in = []
  c = []
  z = []
  aluout = []
  addr = []
  wrdatamem = []
  memout = []
  wrdatareg = []
  # keep track of what is currently in the registers at the end of the datapath
  reg5 = []
  reg6 = []
  reg7 = []
  reg8 = []
  reg9 = []
  reg18 = []
  reg19 = []
  reg20 = []
  reg21 = []
  reg22 = []
  reg23 = []
  reg24 = []
  reg25 = []
  reg26 = []
  reg27 = []
  reg28 = []
  reg29 = []
  reg30 = []
  reg31 = []

  # create PC given incremented instuctions in 5 bit binary
  for i,inst in enumerate(instruction):
    pc.append(bin(i)[2:].zfill(5))

  # create csv with expected outputs given instruction type to be used for testing

  ''' anything left blank ("") means this needs to be calculated based on registers 
  used, and ordering and is best done by the user in the excel file, once these are
  created could consider reading them in from a csv'''
  for inst in instruction:
    #r-type
    if(inst[25:32] == "0110011"):
      name.append("r-type")
      immediate.append(inst)
      funct7.append(inst[0:7])
      rs2.append(inst[7:12])
      rs1.append(inst[12:17])
      funct3.append(inst[17:20])
      rd.append(inst[20:25])
      opcode.append(inst[25:32])
      branch.append("0")
      memread.append("0")
      memtoreg.append("0")
      memwrite.append("0")
      aluop.append("10")
      regw.append("1")
      # check the functs to know the ALU op
      if(inst[0:7] == "0000000"):
        if(inst[17:20] == "000"):
          aluopcode.append("0000")
        elif(inst[17:20] == "111"):
          aluopcode.append("0111")
        elif(inst[17:20] == "110"):
          aluopcode.append("0110")
        elif(inst[17:20] == "001"):
          aluopcode.append("0001")
        elif(inst[17:20] == "101"):
          aluopcode.append("0101")
        elif(inst[17:20] == "100"):
          aluopcode.append("0100")
        else:
          print("Function type error")
      elif(inst[0:7] == "0100000" and inst[17:20] == "000"):
        aluopcode.append("0010")
      elif(inst[0:7] == "0010011" and inst[17:20] == "101"):
        aluopcode.append("0011")
      else:
        print("Function type error")
        print("2")
        print(inst)
      alusrc.append("0")
      data1out.append("")
      data2out.append("")
      data2in.append("DATA2OUT")
      c.append("")
      z.append("")
      aluout.append("")
      addr.append("ALUOUT[7downto0]")
      wrdatamem.append("DATA2OUT")
      memout.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      wrdatareg.append("ALUOUT")
      reg5.append("")
      reg6.append("")
      reg7.append("")
      reg8.append("")
      reg9.append("")
      reg18.append("")
      reg19.append("")
      reg20.append("")
      reg21.append("")
      reg22.append("")
      reg23.append("")
      reg24.append("")
      reg25.append("")
      reg26.append("")
      reg27.append("")
      reg28.append("")
      reg29.append("")
      reg30.append("")
      reg31.append("")
    # ld-type
    elif(inst[25:32] == "0000011"):
      name.append("ld-type")
      immediate.append("00000000000000000000"+inst[0:13])
      funct7.append("0000000")
      rs2.append("00000")
      rs1.append(inst[12:17])
      funct3.append(inst[17:20])
      rd.append(inst[20:25])
      opcode.append(inst[25:32])
      branch.append("0")
      memread.append("1")
      memtoreg.append("1")
      memwrite.append("0")
      aluop.append("00")
      regw.append("1")
      aluopcode.append("0000")
      alusrc.append("1")
      data1out.append("")
      data2out.append("")
      data2in.append("IMMEDIATE")
      c.append("")
      z.append("")
      aluout.append("")
      addr.append("ALUOUT[7downto0]")
      wrdatamem.append("DATA2OUT")
      memout.append("")
      wrdatareg.append("MEMOUT")
      reg5.append("")
      reg6.append("")
      reg7.append("")
      reg8.append("")
      reg9.append("")
      reg18.append("")
      reg19.append("")
      reg20.append("")
      reg21.append("")
      reg22.append("")
      reg23.append("")
      reg24.append("")
      reg25.append("")
      reg26.append("")
      reg27.append("")
      reg28.append("")
      reg29.append("")
      reg30.append("")
      reg31.append("")
    # i-type
    elif(inst[25:32] == "0010011"):
      name.append("i-type")
      immediate.append("00000000000000000000"+inst[0:13])
      funct7.append(inst[0:7])
      rs2.append("00000")
      rs1.append(inst[12:17])
      funct3.append(inst[17:20])
      rd.append(inst[20:25])
      opcode.append(inst[25:32])
      branch.append("0")
      memread.append("0")
      memtoreg.append("0")
      memwrite.append("0")
      aluop.append("11")
      regw.append("1")
      # check the functs to know the ALU op
      if(inst[0:7] == "0000000"):
        if(inst[17:20] == "000"):
          aluopcode.append("0000")
        elif(inst[17:20] == "111"):
          aluopcode.append("0111")
        elif(inst[17:20] == "110"):
          aluopcode.append("0110")
        elif(inst[17:20] == "001"):
          aluopcode.append("0001")
        elif(inst[17:20] == "101"):
          aluopcode.append("0101")
        elif(inst[17:20] == "100"):
          aluopcode.append("0100")
        else:
          print("Function type error")
      elif(inst[0:7] == "0100000" and inst[17:20] == "101"):
        aluopcode.append("0011")
      else:
        print("Function type error")
      alusrc.append("1")
      data1out.append("")
      data2out.append("")
      data2in.append("IMMEDIATE")
      c.append("")
      z.append("")
      aluout.append("")
      addr.append("ALUOUT[7downto0]")
      wrdatamem.append("DATA2OUT")
      memout.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      wrdatareg.append("ALUOUT")
      reg5.append("")
      reg6.append("")
      reg7.append("")
      reg8.append("")
      reg9.append("")
      reg18.append("")
      reg19.append("")
      reg20.append("")
      reg21.append("")
      reg22.append("")
      reg23.append("")
      reg24.append("")
      reg25.append("")
      reg26.append("")
      reg27.append("")
      reg28.append("")
      reg29.append("")
      reg30.append("")
      reg31.append("")
    # s-type
    elif(inst[25:32] == "0100011"):
      name.append("s-type")
      immediate.append("00000000000000000000"+inst[0:7]+inst[20:25])
      funct7.append("0000000")
      rs2.append(inst[7:12])
      rs1.append(inst[12:17])
      funct3.append(inst[17:20])
      rd.append("00000")
      opcode.append(inst[25:32])
      branch.append("0")
      memread.append("0")
      memtoreg.append("X")
      memwrite.append("1")
      aluop.append("00")
      regw.append("0")
      aluopcode.append("0000")
      alusrc.append("1")
      data1out.append("")
      data2out.append("")
      data2in.append("IMMEDIATE")
      c.append("")
      z.append("")
      aluout.append("")
      addr.append("ALUOUT[7downto0]")
      wrdatamem.append("DATA2OUT")
      memout.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      wrdatareg.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      reg5.append("")
      reg6.append("")
      reg7.append("")
      reg8.append("")
      reg9.append("")
      reg18.append("")
      reg19.append("")
      reg20.append("")
      reg21.append("")
      reg22.append("")
      reg23.append("")
      reg24.append("")
      reg25.append("")
      reg26.append("")
      reg27.append("")
      reg28.append("")
      reg29.append("")
      reg30.append("")
      reg31.append("")
    # branch type
    elif(inst[25:32] == "1100011"):
      name.append("sb-type")
      immediate.append(
        "00000000000000000000"+inst[0]+inst[24]+inst[1:7]+inst[20:24])
      funct7.append("0000000")
      rs2.append(inst[7:12])
      rs1.append(inst[12:17])
      funct3.append(inst[17:20])
      rd.append("00000")
      opcode.append(inst[25:32])
      branch.append("1")
      memread.append("0")
      memtoreg.append("X")
      memwrite.append("0")
      aluop.append("01")
      regw.append("0")
      aluopcode.append("0010")
      alusrc.append("0")
      data1out.append("")
      data2out.append("")
      data2in.append("DATA2OUT")
      c.append("")
      z.append("")
      aluout.append("")
      addr.append("ALUOUT[7downto0]")
      wrdatamem.append("DATA2OUT")
      memout.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      wrdatareg.append("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
      reg5.append("")
      reg6.append("")
      reg7.append("")
      reg8.append("")
      reg9.append("")
      reg18.append("")
      reg19.append("")
      reg20.append("")
      reg21.append("")
      reg22.append("")
      reg23.append("")
      reg24.append("")
      reg25.append("")
      reg26.append("")
      reg27.append("")
      reg28.append("")
      reg29.append("")
      reg30.append("")
      reg31.append("")
    else:
      print("This is not a correct instruction type")
      exit(1)
  csvfile = open(f"{csvfilename}.csv", "w+")

  csvfile.write(cols)

  for i, inst in enumerate(instruction):
    csvfile.write(
      name[i]+","+pc[i]+","+inst+","+immediate[i]+","+funct7[i]+","+rs2[i]+","
      +rs1[i]+","+funct3[i]+","+rd[i]+","+opcode[i]+","+branch[i]+","+memread[i]
      +","+memtoreg[i]+","+memwrite[i]+","+aluop[i]+","+regw[i]+","+aluopcode[i]
      +","+alusrc[i]+","+data1out[i]+","+data2out[i]+","+data2in[i]+","+c[i]+","
      +z[i]+","+aluout[i]+","+addr[i]+","+wrdatamem[i]+","+memout[i]+","
      +wrdatareg[i]+","+reg5[i]+","+reg6[i]+","+reg7[i]+","+reg8[i]+","+reg9[i]+
      ","+reg18[i]+","+reg19[i]+","+reg20[i]+","+reg21[i]+","+reg22[i]+","+
      reg23[i]+","+reg24[i]+","+reg25[i]+","+reg26[i]+","+reg27[i]+","+reg28[i]+
      ","+reg29[i]+","+reg30[i]+","+reg31[i]+"\n"
    )

  csvfile.close()
