# Secure Password Generator

A Python-based secure password generator that creates customizable passwords using cryptographically secure randomness.

## Features

- Custom password length
- Optional uppercase letters
- Optional digits
- Optional special characters
- Guaranteed inclusion of selected character types
- Entropy-based password strength analysis
- Secure password generation using Python's `secrets` module

## Technologies Used

- Python 3

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Youssufathalla/secure-password-generator.git
```

2. Navigate to the project folder:

```bash
cd secure-password-generator
```

3. Run the script:

```bash
python password_generator.py
```

## Example Output

```text
Generated password: T7@mL9#q
Password strength: Strong
Entropy: 78 bits
Strength score: 78 / 100
```

## Screenshot

![Program Output](screenshots/example-output.png)

## What I Learned

- Structuring Python code using functions
- Validating user input
- Using cryptographically secure randomness
- Calculating password strength using entropy
- Creating and publishing a project with Git and GitHub

## Future Improvements

- Add password policy presets
- Add batch password generation
- Add clipboard copy support
- Add unit tests
- Add a simple graphical interface