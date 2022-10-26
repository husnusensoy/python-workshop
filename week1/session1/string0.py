s = "Hello World"
s1 = "Hello World"

s2 = "Hello" + " " + "World" + "!"

s3 = "Hello" " " "World" "!"

print(s)
print(s1)
print(s2)
print(s3)

# Indexing & Slicing
print(s[0])
print(s[:3])
print(s[-3:])
print(s[1:3])
print(s[-4])

print(len(s))


first_name = "HüSnÜ"
last_name = "ŞenSoY"

print(f"""
Hello {first_name} {last_name} with a total name 
length of {len(first_name) + len(last_name)}
""")

print(f"""Hello {first_name.lower()} {last_name.upper()} 
with a total name length of {len(first_name) + len(last_name)}
""")

print(f"""Hello {first_name.title()} {last_name.title()} 
with a total name length of {len(first_name) + len(last_name)}
""")

input_string_var = input("Enter some data: ")

print(f"User input was {input_string_var}")