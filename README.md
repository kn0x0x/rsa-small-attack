# Small Plaintext Attack on RSA

A Python script to perform a **small plaintext attack** on RSA encryption. It recovers the plaintext (`m`) from a ciphertext (`c`) when the plaintext and public exponent (`e`) are small. Useful for CTF challenges or educational purposes.

## Requirements
- Python 3.x
- `gmpy2` library: `pip install gmpy2`

## Usage
1. Set `c` (ciphertext), `e` (public exponent), and `n` (modulus) in the script.
2. Run: `python small_plaintext_attack.py`
3. Output: Plaintext as an integer and, if possible, an ASCII string (e.g., a CTF flag).

## Example
```python
from gmpy2 import iroot

c = 27  # Ciphertext
e = 3   # Exponent
n = 100 # Modulus

m, exact = iroot(c, e)
if exact and pow(m, e, n) == c:
    print("Plaintext:", m)
else:
    print("Attack failed.")
