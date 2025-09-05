from decimalToBinary import decimalToBinary

def test_decimalToBinary():
    assert decimalToBinary(242) == "11110010"
    assert decimalToBinary(177) == "10110001"
    assert decimalToBinary(140) == "10001100"
    assert decimalToBinary(170) == "10101010"
    assert decimalToBinary(41) == "101001"
    assert decimalToBinary(90) == "1011010"
    assert decimalToBinary(59) == "111011"
    assert decimalToBinary(4) == "100"
    assert decimalToBinary(76) == "1001100"
    assert decimalToBinary(71) == "1000111"
    assert decimalToBinary(0) == "0"