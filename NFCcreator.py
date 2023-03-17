

import argparse

parser = argparse.ArgumentParser(description='NFC file Output')
parser.add_argument('-o', dest='Output', type=str,
                    help='Name of the Output nfc file')
parser.add_argument('-l', dest='Link', type=str,
                    help='Link To the NFC')
parser.add_argument('-t', dest='Type', type=str,
                    help='NFC type (NTAG213 = N3 , NTAG215 = N5 , NTAG216 = N6)')

args = parser.parse_args()

f = open(str(args.Output)+".nfc", "w")

f.write("""Filetype: Flipper NFC device
Version: 2
# Nfc device type can be UID, Mifare Ultralight, Mifare Classic, Bank card
Device type: NTAG213
# UID, ATQA and SAK are common for all formats
UID: 04 39 91 C2 FC 67 80
ATQA: 44 00
SAK: 00
# Mifare Ultralight specific data
Signature: AF 0D 47 F0 EF FF DC 7B 8B 7B 78 DD 93 9B E6 C1 BF 15 33 0A 1A 82 B6 C8 87 B1 69 63 54 5F 31 85
Mifare version: 00 04 04 02 01 00 0F 03
Counter 0: 0
Tearing 0: 00
Counter 1: 0
Tearing 1: 00
Counter 2: 0
Tearing 2: 00
Pages total: 45
Page 0: 04 39 91 24
Page 1: C2 FC 67 80
Page 2: D9 48 00 00
Page 3: E1 10 12 00
Page 4: 01 03 A0 0C
Page 5: 34 03 """)

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
Page 2: A3 A3 00 00
Page 3: E1 10 3E 00
Page 4: 03 """)

f.write("""Filetype: Flipper NFC device
Version: 2
# Nfc device type can be UID, Mifare Ultralight, Mifare Classic, Bank card
Device type: NTAG216
# UID, ATQA and SAK are common for all formats
UID: 04 B8 31 3A 30 73 80
ATQA: 44 00
SAK: 00
# Mifare Ultralight specific data
Signature: 31 B5 99 8B 1D 1C 6A F2 C6 C7 AE C2 E1 44 29 95 2F A9 E7 57 29 2B FB 39 E1 6D DC 43 E2 CE C5 80
Mifare version: 00 04 04 02 01 00 13 03
Counter 0: 0
Tearing 0: 00
Counter 1: 0
Tearing 1: 00
Counter 2: 0
Tearing 2: 00
Pages total: 231
Page 0: 04 B8 31 05
Page 1: 3A 30 73 80
Page 2: F9 48 00 00
Page 3: E1 10 6D 00
Page 4: 03 """)
if args.Link

