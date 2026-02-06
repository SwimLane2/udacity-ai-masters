"""Generate an infinite stream of successively larger random lists."""
import helper
def generate_cases():
    size = 0
    while True:
        result = helper.random_list(size)
        yield result
        size += 1
    
    

    
        
if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)

g = generate_cases()
next(g)