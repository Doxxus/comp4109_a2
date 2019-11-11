import hashlib

def i2osp(integer, size=4):
    return ''.join([chr((integer >> (8 * i)) & 0xFF) for i in reversed(range(size))])

def h(x):
    return str((2*x + 1) % 65521)

def mgf1(input, length):
    counter = 0
    output = ''
    while (len(output) < length):
        C = i2osp(counter, 4)
        output += h(int(input + int(C)))
        counter += 1
    return output[:length]
    
num = ((2**7) + (2**9) + (2**10))

print(str(mgf1(num, 5)))