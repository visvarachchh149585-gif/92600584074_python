s1 = 'Single quote string'
s2 = "Double Quotes string"
multi_line = """This is
multi-line string."""

print(s1[0:3])
print(s1[-1])
print(s1[0])
print(s1[0:8])
print(s1[0:-4])

s3 = "basic string function"
print(len(s3)) 
print(s3.strip()) 
print(s3.upper()) 
print(s3.lower()) 
print(s3.replace("basic", "Python")) 
print(s3.startswith("ba"))
print(s3.endswith("on")) 

name,age = "vishw",20
print("My name is {} and I am {} years old.".format(name, age))
