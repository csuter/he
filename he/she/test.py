from random import *
from he.she.public import *
from he.she.private import *

def test_she_bit_encryption_decryption():
	l = 8
	key = keygen(l,l**2)
	sk = key['sk']
	pk = key['pk']
	num_tests = 1000
	test_cases = [randint(0,1) for x in range(num_tests)]
	assert(0 == sum([decrypt_bit(sk,encrypt_bit(l, pk, r, l)) - r for r in test_cases]))

def test_she_int64_encryption_decryption():
	l = 8
	key = keygen(l,l**2)
	sk = key['sk']
	print(sk)
	pk = key['pk']
	num_tests = 100
	test_cases = [randint(0,2**64-1) for x in range(num_tests)]
	assert(0 == sum([decrypt_int64(sk,encrypt_int64(l, pk, r, l)) - r for r in test_cases]))

def test_she_int64_encrypted_single_add():
	l = 4
	key = keygen(l,l**2)
	sk = key['sk']
	pk = key['pk']
	print("sk: %d" % sk)
	n1 = 100000234
	n2 = 0
	c1 = encrypt_int64(l, pk, n1, l)
	c2 = encrypt_int64(l, pk, n2, l)
	csum = encrypted_int64_add(l, pk, c1, c2, l)
	d = decrypt_int64(sk, csum)
	print
	print("n1: %d" % n1)
	print
	print("n2: %d" % n2)
	print
	print("n1 + n2: %d" % (n1 + n2))
	print
	print("bits(n1+n2) = %s" % int64_to_bits(n1 + n2))
	print
	print("noise(c1): %s" % noise(sk,c1))
	print
	print("avg(noise(c1)): %s" % avgnoise(sk, c1))
	print
	print("noise(c2): %s" % noise(sk,c2))
	print
	print("avg(noise(c2)): %s" % avgnoise(sk, c2))
	print
	print("noise(csum): %s" % noise(sk,csum))
	print
	print("avg(noise(csum)): %s" % avgnoise(sk, csum))
	print
	print("d(c1+c2) = %s" % d)
	print
	print("bits(d(c1+c2)) = %s" % int64_to_bits(d))
	assert(d == (n1+n2))


