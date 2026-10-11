import re

text = "My phone number is 891513510"

pattern = r"\d{10}"

result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")
