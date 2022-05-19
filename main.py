data = [
    0x13, 0x55, 0xb6, 0x76, 0x79, 0x88, 0x29, 0x5e, 
    0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x34,
     0x7e, 0x58, 0x1e, 0x36, 0x00, 0x00, 0x00, 0x00, 
     0x00, 0x00, 0x00, 0x00
]

print("Q1.")
source_port = 0
source_port |= data[0] << 8
source_port |= data[1]
print("Source Port:",source_port)

dest_port = 0 
dest_port |= data[2] << 8
dest_port |= data[3]

print("Destination port:", dest_port)

verification_tag = 0 
verification_tag |= data[4] << 24
verification_tag |= data[5] << 16
verification_tag |= data[6] << 8
verification_tag |= data[7]

print("Verification Tag:", verification_tag)

type_ = data[12]
print("Type:",type_)

b_flag = data[13] & 0b00000010 != 0
print("B-flag: ", b_flag)

length=0
length |= data[14] << 8
length |= data[14]
print("Length: ",length)

