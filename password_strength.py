import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

# Analyze password strength using zxcvbn
def analyze_password_strength(password):
    results = zxcvbn(password)
    score = results['score']
    feedback = results['feedback']
    
    strength_report = f"\n--- Password Strength ---\nScore: {score}/4\n"
    if feedback['warning']:
        strength_report += f"Warning: {feedback['warning']}\n"
    if feedback['suggestions']:
        strength_report += "Suggestions: " + ", ".join(feedback['suggestions']) + "\n"
    strength_report += "-------------------------\n"
    return strength_report

# Generate password variants using leetspeak and years
def generate_variants(word):
    leet_map = {'a': ['@', '4'], 's': ['$', '5'], 'o': ['0'], 'e': ['3'], 'i': ['1'], 'l': ['1']}
    variants = set()
    word_lower = word.lower()

    variants.add(word_lower)
    for year in ['2025', '2024', '123', '321', '111']:
        variants.add(word_lower + year)

    for char in word_lower:
        if char in leet_map:
            for leet in leet_map[char]:
                variant = word_lower.replace(char, leet)
                variants.add(variant)

    return list(variants)

# Save wordlist to file
def save_wordlist(words, filename="custom_wordlist.txt"):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')

# Main function to handle GUI inputs
def generate():
    pw = entry_pw.get()
    name = entry_name.get()
    pet = entry_pet.get()
    birth = entry_birth.get()

    if not pw:
        messagebox.showwarning("Missing Password", "Please enter a password to analyze.")
        return

    # Password analysis
    report = analyze_password_strength(pw)

    # Wordlist generation
    inputs = [name, pet, birth]
    wordlist = []
    for item in inputs:
        if item:
            wordlist.extend(generate_variants(item))

    wordlist = list(set(wordlist))  # Remove duplicates
    save_wordlist(wordlist)

    messagebox.showinfo("Success", f"Wordlist saved as 'custom_wordlist.txt'\n{report}")

# GUI Design
root = tk.Tk()
root.title("Password Tool")
root.geometry("300x250")

tk.Label(root, text="Password").pack()
entry_pw = tk.Entry(root, show="*")
entry_pw.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Pet Name").pack()
entry_pet = tk.Entry(root)
entry_pet.pack()

tk.Label(root, text="Birth Year").pack()
entry_birth = tk.Entry(root)
entry_birth.pack()

tk.Button(root, text="Generate", command=generate).pack(pady=10)

root.mainloop()
 
