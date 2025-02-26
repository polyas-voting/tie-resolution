import hmac
import hashlib
import struct

def tie_resolution(s_seed: str, u_seed: str, ballot_id: str, list_id: str, tied_candidates: int):
    seed = (s_seed + u_seed).encode("utf-8")
    numbers = DerivedNumbers(seed, ballot_id.encode("utf-8"), list_id.encode("utf-8"))
    return random_permutation(tied_candidates, numbers)

## Integers from seed

def derived_integers(seed: bytes, bid: bytes, lid: bytes):
    i = 0
    while True:
        b = block(seed, bid, lid, i)
        for start_pos in range(0, 30, 4):
            v = (bytes_to_int(b[start_pos:start_pos+4]))
            yield v & 0x7FFFFFFF
        i += 1

def block(seed: bytes, bid: bytes, lid: bytes, i: int) -> bytes:
    key = seed
    value = int_to_bytes(i) + bid + bytearray([0]) + lid
    return mac_sha256(key, value)

## Next random number in the range

class DerivedNumbers:

    def __init__(self, seed: bytes, bid: bytes, lid: bytes):
        self.derived_integers = derived_integers(seed, bid, lid)

    def next(self, upper_bound: int):
        m = minimal_mask(upper_bound)
        while True:
            a = next(self.derived_integers) & m
            if a < upper_bound:
                return a

def minimal_mask(upper_bound: int) -> int:
    assert upper_bound >= 0, "Upper bound must be non-negative"
    leading_zeros_bits_count = (32 - (upper_bound - 1).bit_length()) - 1
    return 0x7fffffff >> leading_zeros_bits_count

## random permutation

def random_permutation(n: int, derived_numbers: DerivedNumbers):
    array = list(range(n))
    for i in range(n):
        k: int = derived_numbers.next(n - i) + i
        array[i], array[k] = array[k], array[i]
    return array

## Helper functions

def mac_sha256(key: bytes, value: bytes) -> bytes:
    return hmac.new(key, value, hashlib.sha256).digest()

def int_to_bytes(i: int) -> bytes:
    return struct.pack('>I', i)

def bytes_to_int(b: bytes) -> int:
    return struct.unpack('>I', b)[0]
