'''
for the generation of the 52 keys
'''

key = raw_input("Enter the 128bit keys for the generation of the 52 sub keys")
key =  key.lstrip('0x').lstrip('0X').strip()
key = int (key,16)
key  = '{:032x}'.format(key)
sub_keys = list(i for i in range(52))
# first set of keys
sub_keys[0] = key[0:4]; sub_keys[1] = key[4:8] ; sub_keys[2] = key[8:12] ; sub_keys[3] = key[12:16]
sub_keys[4] = key[16:20]; sub_keys[5] = key[20:24] ; sub_keys[6] = key[24:28] ; sub_keys[7] = key[28:32]

key  = key.lstrip("0x").rstrip("L")
key = int (key,16)
key = '{:0128b}'.format(key)
key = key[25:128]+ key[0:25]
key  = int (key,2)
key  = '{:032x}'.format(key)

# second set of keys
sub_keys[8] = key[0:4]; sub_keys[9] = key[4:8] ; sub_keys[10] = key[8:12] ; sub_keys[11] = key[12:16]
sub_keys[12] = key[16:20]; sub_keys[13] = key[20:24] ; sub_keys[14] = key[24:28] ; sub_keys[15] = key[28:32]

key  = key.lstrip("0x").rstrip("L")
key = int (key,16)
key = '{:0128b}'.format(key)
key = key[25:128]+ key[0:25]
key  = int (key,2)
key  = '{:032x}'.format(key)

#Third set of keys
sub_keys[16] = key[0:4]; sub_keys[17] = key[4:8] ; sub_keys[18] = key[8:12] ; sub_keys[19] = key[12:16]
sub_keys[20] = key[16:20]; sub_keys[21] = key[20:24] ; sub_keys[22] = key[24:28] ; sub_keys[23] = key[28:32]

key  = key.lstrip("0x").rstrip("L")
key = int (key,16)
key = '{:0128b}'.format(key)
key = key[25:128]+ key[0:25]
key  = int (key,2)
key  = '{:032x}'.format(key)

# fourth set of keys
sub_keys[24] = key[0:4]; sub_keys[25] = key[4:8] ; sub_keys[26] = key[8:12] ; sub_keys[27] = key[12:16]
sub_keys[28] = key[16:20]; sub_keys[29] = key[20:24] ; sub_keys[30] = key[24:28] ; sub_keys[31] = key[28:32]

key  = key.lstrip("0x").rstrip("L")
key = int (key,16)
key = '{:0128b}'.format(key)
key = key[25:128]+ key[0:25]
key  = int (key,2)
key  = '{:032x}'.format(key)

# fifth set of keys
sub_keys[32] = key[0:4]; sub_keys[33] = key[4:8] ; sub_keys[34] = key[8:12] ; sub_keys[35] = key[12:16]
sub_keys[36] = key[16:20]; sub_keys[37] = key[20:24] ; sub_keys[38] = key[24:28] ; sub_keys[39] = key[28:32]

key  = key.lstrip("0x").rstrip("L")
key = int (key,16)
key = '{:0128b}'.format(key)
key = key[25:128]+ key[0:25]
key  = int (key,2)
key  = '{:032x}'.format(key)

# sixth set of keys
sub_keys[40] = key[0:4]; sub_keys[41] = key[4:8] ; sub_keys[42] = key[8:12] ; sub_keys[43] = key[12:16]
sub_keys[44] = key[16:20]; sub_keys[45] = key[20:24] ; sub_keys[46] = key[24:28] ; sub_keys[47] = key[28:32]

key  = key.lstrip("0x").rstrip("L")
key = int (key,16)
key = '{:0128b}'.format(key)
key = key[25:128]+ key[0:25]
key  = int (key,2)
key  = '{:032x}'.format(key)

# seventh set of keys
sub_keys[48] = key[0:4]; sub_keys[49] = key[4:8] ; sub_keys[50] = key[8:12] ; sub_keys[51] = key[12:16]
print sub_keys
with open('sub_keys.txt', 'w') as file:
 for data in sub_keys:
    file.write("{}\n".format(data))

