from gcd import *

if __name__ == '__main__':
    assert gcd(1, 1) == 1
    assert gcd(13, 13) == 13
    assert gcd(37, 600) == 1
    assert gcd(20, 100) == 20
    assert gcd(624129, 2061517) == 18913

    assert phi(1) == 1
    assert phi(2) == 1
    assert phi(3) == 2
    assert phi(4) == 2
    assert phi(5) == 4
    assert phi(6) == 2
    assert phi(7) == 6
    assert phi(8) == 4
    assert phi(9) == 6
    assert phi(10) == 4
