# Zoo Admin Login — Decorator Demo

A very basic Python demo showing how to use a **decorator** to validate input
before a function runs. Built for a Software Engineering Python class activity.

## Goal
Demonstrate that a decorator can:
1. Intercept a function call.
2. Validate the password (must be at least 8 characters).
3. Return `"Success"` or `"Failed"` based on the validation result.

## Project Structure
```
activity-2/
├── decorator.py        # Defines the validate_password decorator
├── authentication.py   # Contains the login() function decorated with @validate_password
├── main.py             # ZooApp class — entry point that calls login()
└── README.md
```

## How It Works
- `decorator.py` defines `validate_password`, which checks `len(password) >= 8`.
- `authentication.py` declares `login(username, password)` and decorates it with `@validate_password`.
- `main.py` runs the `ZooApp` class, prompts for credentials, calls `login()`, and prints the result returned by the decorator.

## Run
```bash
python3 main.py
```

## Sample Output

**Valid password (8+ characters):**
```
=== Welcome to the Zoo Admin Login ===
Enter admin username: admin
Enter password: password
Decorator: Password is valid (at least 8 characters).
Login function: Welcome admin to the Zoo Admin Panel!
Login result from decorator: Success
```

**Invalid password (less than 8 characters):**
```
=== Welcome to the Zoo Admin Login ===
Enter admin username: admin
Enter password: short
Decorator: Password is invalid (must be at least 8 characters).
Login result from decorator: Failed
```
