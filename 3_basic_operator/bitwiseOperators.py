
#     Bitwise Operators

# Bitwise operator works on bits and performs bit by bit operation. Assume if a = 60; and b = 13; Now in the binary format their values will be 0011 1100 and 0000 1101 respectively. Following table lists out the bitwise operators supported by Python language with an example each in those, we use the above two variables (a and b) as operands −

# a = 0011 1100

# b = 0000 1101

# -----------------

# a&b = 0000 1100

# a|b = 0011 1101

# a^b = 0011 0001

# ~a  = 1100 0011

# There are following Bitwise operators supported by Python language

# [ Show Example ]
# Operator 	Description 	Example
# & Binary AND 	Operator copies a bit to the result if it exists in both operands 	(a & b) (means 0000 1100)
# | Binary OR 	It copies a bit if it exists in either operand. 	(a | b) = 61 (means 0011 1101)
# ^ Binary XOR 	It copies the bit if it is set in one operand but not both. 	(a ^ b) = 49 (means 0011 0001)
# ~ Binary Ones Complement 	It is unary and has the effect of 'flipping' bits. 	(~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
# << Binary Left Shift 	The left operands value is moved left by the number of bits specified by the right operand. 	a << 2 = 240 (means 1111 0000)
# >> Binary Right Shift 	The left operands value is moved right by the number of bits specified by the right operand. 	a >> 2 = 15 (means 0000 1111)
