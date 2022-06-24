def int32_to_ip(int32):
    ans = ''
    tmp = bin(int32)[2:]
    tmp = '0' * (32 - len(tmp)) + tmp
    for i in range(0, len(tmp), 8):
        ans += str(int(tmp[i:i+8], 2))
        ans += '.'
    return ans[:-1]


print(int32_to_ip(2154959208)) #128.114.17.104
print(int32_to_ip(0)) #0.0.0.0
print(int32_to_ip(2149583361)) #128.32.10.1