# 🔐 Password Strength Analyzer with Custom Wordlist Generator

This Python project allows you to check the strength of passwords and generate custom wordlists for password cracking tools. It has both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** using Tkinter.

---

## 🧰 Tools Used:
- **Python**
- **NLTK** – for word processing
- **zxcvbn** – for password strength estimation
- **Tkinter** – for GUI (optional)
- **argparse** – for CLI arguments

---

## 📁 Project Files:
| File Name               | Description                                     |
|------------------------|-------------------------------------------------|
| `password_tool.py`     | CLI tool for password strength & wordlist export |
| `password_strength.py` | GUI version built with Tkinter                  |
| `custom_wordlist.txt`  | Output file – contains the generated wordlist   |
| `README.md`            | Project overview (this file)                    |

---

## 🚀 How to Run

### 🖥️ Option 1: Run CLI version
```bash
python password_tool.py --password yourPassword123 --name "Ramya" --dob "2000" --pet "Tommy"
# PasswordAnalyzer
Password Strength Analyzer with Custom Wordlist Generator# 🔐 Password Strength Analyzer with Custom Wordlist Generator
A simple Python-based tool to:
- Analyze password strength using `zxcvbn`
- Generate personalized wordlists from user inputs (name, pet, etc.)
- Export wordlists in `.txt` format for password cracking tools like John the Ripper
- GUI version built using Tkinter (also runs on Android with Pydroid 3)

## 📁 Files Included
- `password_tool.py`: Command-line tool
- `password_strength.py`: GUI using Tkinter

## 📦 Output
Generates a `.txt` file containing a custom wordlist based on your inputs.

## 🛠 Technologies Used
- Python 3
- zxcvbn
- NLTK
- Tkinter
- Pydroid 3 (Android)

## 📱 How to Run
- Use **Pydroid 3** on mobile or any Python 3 IDE on PC
- Run the `.py` file of your choice
  - Follow CLI prompts (for terminal)
  - Use GUI (for Tkinter version)

## 👩‍💻 Author
Sai Ramya Cherala

