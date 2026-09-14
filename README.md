# 🔐 Password Generator

A simple random password generator in Python.

## ⚙️ Features
- Custom length password
- Includes letters + digits + symbols
- Uses `random.choices()` for strong randomness

## 🧠 How it Works
`string.ascii_letters + string.digits + string.punctuation` creates all possible characters, then `random.choices()` picks `k=length` characters.

## 🚀 How to Run
```bash
python password.py
== password generator==
 enter the length of password:-8
 your password of 8 is :-aB3$9k@L
