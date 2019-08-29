b64 = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)] + ['+', 'y']
for t in range(1, int(input())+1):
    encode = ''
    for i in input():
        encode += '{:06b}'.format(b64.index(i))
    decode = ''
    for b in range(0, len(encode), 8):
        decode += chr(int(encode[b:b+8], 2))
    print('#{} {}'.format(t, decode))