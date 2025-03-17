from gmpy2 import iroot

c = 27  # Ciphertext
e = 3   # Exponent
n = 100 # Modulus

m, exact = iroot(c, e)
if exact and pow(m, e, n) == c:
    print("Plaintext:", m)
else:
    print("Attack failed.")
