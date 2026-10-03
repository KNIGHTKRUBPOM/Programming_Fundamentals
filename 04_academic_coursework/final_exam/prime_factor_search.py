"""
Final Exam - Prime Factor Search & Decomposition
================================================
Generates prime numbers up to n using trial division, then finds
factor pairs or prime decompositions that multiply to a given target number.
"""

from typing import List, Optional, Tuple


def generate_primes(n: int) -> List[int]:
    """Generate all prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for d in range(2, int(num**0.5) + 1):
            if num % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def find_prime_factor_pair(target: int) -> Optional[Tuple[int, int]]:
    """Find a pair of prime numbers (p1, p2) such that p1 * p2 == target."""
    # Check perfect squares first
    root = int(target**0.5)
    if root * root == target:
        return (root, root)

    primes = generate_primes(target)
    seen = set()

    for p in primes:
        if target % p == 0:
            complement = target // p
            if complement in seen or complement == p:
                return (min(p, complement), max(p, complement))
            seen.add(p)

    return None


if __name__ == "__main__":
    assert generate_primes(10) == [2, 3, 5, 7]
    assert find_prime_factor_pair(4) == (2, 2)
    assert find_prime_factor_pair(6) == (2, 3)
    assert find_prime_factor_pair(15) == (3, 5)
    assert find_prime_factor_pair(77) == (7, 11)

    print("Sample primes up to 30:", generate_primes(30))
    print("Prime factors for 77:", find_prime_factor_pair(77))
    print("Prime Factor Search: All tests passed!")
