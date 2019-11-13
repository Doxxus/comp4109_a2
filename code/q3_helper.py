import struct

def h(x):
    y = struct.unpack(">q", x)
    return struct.pack(">I", ((2*y[0] + 1) % 65521))

def i2osp(integer, size=4):
    return struct.pack(">I", integer)

def mgf1(input, length):
    counter = 0
    output = b''
    
    while (len(output) < length):
        C = i2osp(counter, 4)
        output += h(input + C)
        counter += 1
  
    return output[:length+1]
    
print(mgf1(struct.pack(">I", ((2**7) + (2**9) + (2**10))), 5))