import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument(
  "miffilename",
  help="mif file name"
)
parser.add_argument(
  "csvfilename",
  help="csv file name"
)
parser.add_argument(
  "bits",
  type = int,
  help="word size in bits"
)
args = parser.parse_args()

with open(f"{args.csvfilename}.csv") as csvfile:
    for line in csv.reader(csvfile, delimiter=','):
        addresses = line

header = """
-- Copyright (C) 1991-2015 Altera Corporation. All rights reserved.
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, the Altera Quartus II License Agreement,
-- the Altera MegaCore Function License Agreement, or other 
-- applicable license agreement, including, without limitation, 
-- that your use is for the sole purpose of programming logic 
-- devices manufactured by Altera and sold by Altera or its 
-- authorized distributors.  Please refer to the applicable 
-- agreement for further details.

-- Quartus II generated Memory Initialization File (.mif)

WIDTH={bits};
DEPTH={words};

ADDRESS_RADIX=UNS;
DATA_RADIX=UNS;

CONTENT BEGIN
""".format(
        bits = args.bits,
        words = len(addresses)
)

def contentLineGenerator(index, value):
    return f"\t{index}    :   {value};\n"

textfile = open(f'{args.miffilename}.mif', 'w+')

textfile.write(header)

for index, address in enumerate(addresses):
    textfile.write(contentLineGenerator(index, address))

textfile.write('END;\n')

textfile.close()
