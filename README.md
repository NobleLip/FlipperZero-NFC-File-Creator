```
 _   _ ______ _____       _____                _             
| \ | ||  ___/  __ \     /  __ \              | |            
|  \| || |_  | /  \/_____| /  \/_ __ ___  __ _| |_ ___  _ __ 
| . ` ||  _| | |  |______| |   | '__/ _ \/ _` | __/ _ \| '__|
| |\  || |   | \__/\     | \__/\ | |  __/ (_| | || (_) | |   
\_| \_/\_|    \____/      \____/_|  \___|\__,_|\__\___/|_|   
                                                             
```

# Lost My Flipper Zero and had to stop the development of this project!


Since I didnt find any website, and could only manage to get NFC through apps, this project intends to eliminate the use of phone to create NFC custom files for the Flipper Zero.



# How NFC's Work



To construct a working NFC file we have to understand how it works, for that I had to search proper documentation from both the manufactors and from people who have dealt with projects that use NFC.



**What I found was:**

1 - [About the NDEF Format](https://learn.adafruit.com/adafruit-pn532-rfid-nfc/ndef)

2 - [NFCForum-TS-Type-2-Tag](./PDFs/NFCForum-TS-Type-2-Tag_1.1.pdf)

3 - [NTAG213_215_216](./PDFs/NTAG213_215_216.pdf)



First we need to understand the first 0 to 5 pages of stored information, in order to make the nfc work

#### Page (0 to 2)

| Page 0 | UID - Byte 1 | UID- Byte 2  | UID- Byte 3  | INTERNAL     |
| ------ | ------------ | ------------ | ------------ | ------------ |
| Page 1 | UID - Byte 4 | UID - Byte 5 | UID - Byte 6 | UID - Byte 7 |
| Page 2 | INTERNAL     | INTERNAL     | LOCK = 00    | LOCK = 00    |

#### Memory Content at Delivery (Page 3 to 5)

**NTAG213**

| Page Address | Byte number within page |
| ------------ |:-----------------------:|

| Page 3 | E1  | 10  | 12    | 00         |
| ------ | --- | --- | ----- | ---------- |
| Page 4 | 01  | 03  | A0    | 0C         |
| Page 5 | 34  | 03  | Start | FE= finish |

**NTAG215**

| Page Address | Byte number within page |
| ------------ | ----------------------- |

| Page 3 | E1  | 10    | 3E         | 00  |
| ------ | --- | ----- | ---------- | --- |
| Page 4 | 03  | START | FE= finish |     |

**NTAG216**

| Page Address | Byte number within page |
| ------------ | ----------------------- |

| Page 3 | E1  | 10    | 6D         | 00  |
| ------ | --- | ----- | ---------- | --- |
| Page 4 | 03  | Start | FE= finish |     |

**NDEF memory size**

| IC      | Value in Byte 2 | NDEF memory size |
| ------- | --------------- | ---------------- |
| NTAG213 | 12              | 144 Bytes        |
| NTAG215 | 3E              | 496 Bytes        |
| NTAG216 | 6D              | 872 Bytes        |



### Writing NDEF Message
