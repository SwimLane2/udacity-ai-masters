import pathlib

# with open('queries.txt', 'w') as outfile:
#     contents = "This is a test file with test content"
#     outfile.write(contents)
    
with open('queries.txt', 'r') as infile:
    contents = infile.read() 
    print(contents)
