# Simple Password Strength and Wordlist Generator

password = input("🔐 Enter a password to check strength: ")

# Simple strength check (not using zxcvbn)
if len(password) < 6:
    print("❌ Weak password: Too short!")
elif password.isalpha() or password.isdigit():
    print("⚠️ Medium password: Add numbers, letters, or symbols.")
else:
    print("✅ Strong password!")

print("\n📋 Now let's create a custom wordlist.")

# Take inputs
name = input("Enter your name: ")
dob = input("Enter your birth year or date (e.g. 1999 or 01011999): ")
pet = input("Enter your pet's name: ")

# Create wordlist combinations
wordlist = [
    name, dob, pet,
    name + dob,
    name + pet,
    dob + pet,
    name + "123",
    pet + "123",
    name[::-1],
    pet.upper(),
    name.capitalize() + "@" + dob[-2:]
]

# Save to .txt file
with open("easy_wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + "\n")

print("\n✅ Wordlist saved as 'easy_wordlist.txt'")