


prompt = "-->"

caps = "CAPS"

print("Hello Welcome")
print(f"This is a {caps} CONVERTER")
print(f"""This will convert your inputed words into {caps}.""")

#This is the input that we (I) am going to comvert into CAPS
print("Please input your word's")
words = input(prompt)

print("converting", words, "to caps")

CAPPED = str.upper(words)

print(CAPPED)