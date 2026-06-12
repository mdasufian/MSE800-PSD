# Activity 1 — User Account Management (Console)

A small Python console application demonstrating maintainable design for a
user-account system. Built for the MSE800 / PSD master's software engineering
class.

## Features

- **Register** — username, password, full name, date of birth
- **Login** — credential check against a salted PBKDF2-SHA256 hash
- **Forgot password** — reset after verifying the date of birth on file
- **Profile view** — shown after successful login (name, DOB, age)

## Project layout

| File            | Responsibility                                         |
| --------------- | ------------------------------------------------------ |
| `main.py`       | Console menu and I/O — no business logic               |
| `auth.py`       | Auth service — orchestrates register / login / reset   |
| `storage.py`    | JSON-file persistence — swappable backend              |
| `user.py`       | `User` dataclass model                                 |
| `security.py`   | Password hashing (PBKDF2-HMAC-SHA256 + per-user salt)  |
| `validators.py` | Field validation rules                                 |

The layers are separated so each concern (UI, business rules, storage,
crypto, validation) can be changed or tested in isolation.

## Run

```bash
python3 main.py
```

User data is written to `users.json` in the project folder on first
registration.

## Password policy

- ≥ 8 characters
- at least one letter and one digit
- stored as `PBKDF2-HMAC-SHA256` (200,000 iterations) with a 16-byte salt

## Notes

- Passwords are **never** stored or printed in plaintext.
- `getpass` hides password input on supported terminals.
- Password reset requires the username and the date of birth on file to
  match before a new password is accepted.
