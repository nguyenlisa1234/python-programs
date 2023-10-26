def largestPowerOf2AtMost(n):
    for exponent in range(20):
        if 2 ** exponent > n:
            return exponent - 1

def decimalToBinaryStringConverter(n):
    if n == 0:
        return "0"
    n1 = largestPowerOf2AtMost(n)
    binaryString = ""
    for exponent in range(n1, -1, -1):
        powerOf2 = 2 ** exponent
        if powerOf2 <= n:
            binaryString += "1"
            n -= powerOf2
        else:
            binaryString += "0"
    return binaryString

print(decimalToBinaryStringConverter(5))