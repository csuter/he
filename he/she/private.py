from he.math.functions import *
from he.she.public import *

def decrypt_int64(sk, cypher):
	return bits_to_int64([decrypt_bit(sk, x) for x in cypher])

def decrypt_bit(sk, cypher):
	return noise(sk, cypher) % 2

def noise(sk, cypher):
	if type(cypher) == long or type(cypher) == int:
		t = cypher % sk
		return t if t < sk/2 else t - sk
	elif type(cypher) == list:
		return [noise(sk, c) for c in cypher]
	else:
		print("Unknown type: %s" % type(cypher))

def avgnoise(sk, cypher):
	return 1.0*sum(noise(sk, cypher))/len(cypher)

def private_encrypted_int64_add(l, pk, sk, c1, c2, n):
	out = [0 for i in range(64)]
	for i in range(64):
		if i > 0:
			[out[i], carry] = encrypted_bits_fulladder(c1[i], c2[i], carry)
		else:
			[out[i], carry] = encrypted_bits_halfadder(c1[i], c2[i])
	return out

