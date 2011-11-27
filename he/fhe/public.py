from random import *
from he.math.functions import *

#def encrypt_int64(l, pk, plain, n):
#	bits = int64_to_bits(plain)
#	zeros = [sum([pk[i] for i in [randint(2,len(pk)-1) for j in range(n)]]) for x in range(64)]
#	return [bits[i] + zeros[i] for i in range(64)]
#
#def encrypted_int64_add(l, pk, c1, c2, n):
#	out = [0 for i in range(64)]
#	for i in range(64):
#		if i > 0:
#			[out[i], carry] = encrypted_bits_fulladder(c1[i], c2[i], carry)
#		else:
#			[out[i], carry] = encrypted_bits_halfadder(c1[i], c2[i])
#	return out
#
#def encrypted_bits_and(c1, c2):
#	return c1 * c2
#
#def encrypted_bits_xor(c1, c2):
#	return c1 + c2
#
#def encrypted_bits_halfadder(c1, c2):
#	return [ encrypted_bits_xor(c1, c2), encrypted_bits_and(c1, c2) ]
#
#def encrypted_bits_fulladder(c1, c2, c3):
#	halfsum_23 = encrypted_bits_halfadder(c2, c3)
#	sum = encrypted_bits_xor(c1, halfsum_23[0])
#	carry = encrypted_bits_xor(
#			encrypted_bits_and( c1, halfsum_23[0] ),
#			halfsum_23[1])
#	return [sum,carry]
#
#def encrypt_bit(l, pk, b, n):
#	N = l
#	P = l*l
#	Q = P*P*l
#	return b + sum([pk[i] for i in [randint(0,len(pk)-1) for j in range(n)]])

def keygen(l, pk_length, alpha, beta):
	[N,P,Q] = [l,l**2,l**5]
	[rN,rP,rQ] = [2**N,2**P,2**Q]
	p = 2*randint(0,rP/2) + 1
	F = [2*random() for i in range(beta)]
	S = sample(range(beta), alpha)
	print "F = %s" % F
	print "S = %s" % S
	print "1/p = %0.66f" % (1.0/p)
	return {
			"sk":p,
			"pk":[
				2*randint(0, rN/2) + p*randint(0,rQ)
				for x in range(pk_length)
				]
			}

