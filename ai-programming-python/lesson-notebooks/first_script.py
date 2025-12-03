new_content = """
print("This is my edited script!")
print("Python is working through Colab!")
"""

with open('first_script.py', 'w') as f:
    f.write(new_content)
