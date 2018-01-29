import requests

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False
    f = 5
    while f <= int(n**0.5):
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modInverse(k,z):
    g, x, y = egcd(k, z)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    else:
        return x % z

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, b):
    return gcd(a, b) == 1

def random():
    param = {"num": 1, "min": 1000, "max": 10**9, "col": 1, "base": 10, "format": "plain", "rnd": "new"}
    response = requests.get("https://www.random.org/integers/", param)
    return int(response.content)

def rsagen():
    p = random()
    q = random()
    n = p * q
    z = (p - 1) * (q - 1)
    pub_key = z
    while not is_coprime(pub_key,z):
        pub_key = random()
    priv_key = modInverse(z,pub_key)

    print ("Public key: " + str(pub_key))
    print ("private key: " + str(priv_key))
    print ("Generated modulus: " + str(n))

if __name__ = "__main__":
    rsagen()
