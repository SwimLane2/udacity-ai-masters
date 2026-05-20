import collections
from pathlib import Path


def count_unique_words(filename):
    # your code here
    counts = collections.Counter()
    file_path = Path(__file__).with_name(filename)
    with open(file_path, "r") as infile:
        for line in infile:
            words = line.split()
            counts.update(words)
            
    for word, count in counts.most_common(10):
        print(word, count) 
    
    return 


if __name__ == '__main__':
    count_unique_words('hamlet.txt')