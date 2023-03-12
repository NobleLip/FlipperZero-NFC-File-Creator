

import argparse

parser = argparse.ArgumentParser(description='NFC file Output')
parser.add_argument('-o', dest='Output', type=str,
                    help='Name of the Output nfc file')
parser.add_argument('-l', dest='Link', type=str,
                    help='Link To the NFC')

args = parser.parse_args()

f = open(str(args.Output)+".nfc", "w")

f.write("""
Filetype: Flipper NFC device
Version: 2
Device type: NTAG215
UID: 04 1B 13 D3 70 00 00
ATQA: 44 00
SAK: 00
Signature: 04 1B 13 84 D3 70 00 00 04 1B 13 84 D3 70 00 00 04 1B 13 84 D3 70 00 00 04 1B 13 84 D3 70 00 00
Mifare version: 00 04 04 02 01 00 11 03
Counter 0: 0
Tearing 0: 00
Counter 1: 0
Tearing 1: 00
Counter 2: 0
Tearing 2: 00
Pages total: 135
Page 0: 04 1B 13 84
Page 1: D3 70 00 00
Page 2: A3 A3 00 00""")

