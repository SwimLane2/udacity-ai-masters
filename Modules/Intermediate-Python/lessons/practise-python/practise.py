def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.
    while True:
        a, b, c = b, c, a + b + c 
        yield a
    
def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    for _ in generate_tribonacci_numbers():
        if _ == num:
            return True
        if _ > num:
            return False
        
for n in range(100):
    print(n, is_tribonacci(n))
    

