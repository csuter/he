
def int64_to_bits(int64):
	return [1 if (int64 & (1 << m)) > 0 else 0 for m in range(64)]

def bits_to_int64(bits):
	return sum([2**i if bits[i] == 1 else 0 for i in range(64)])

