from binaryToDecimal import binaryToDecimal

def test_binaryToDecimal():
    assert binaryToDecimal("10100001") == 161
    assert binaryToDecimal("1011101") == 93
    assert binaryToDecimal("10001010") == 138
    assert binaryToDecimal("11110") == 30
    assert binaryToDecimal("10000101") == 133
    assert binaryToDecimal("1100100") == 100
    assert binaryToDecimal("100000") == 32
    assert binaryToDecimal("11011000") == 216
    assert binaryToDecimal("11011101") == 221
    assert binaryToDecimal("101010") == 42
    assert binaryToDecimal("0") == 0