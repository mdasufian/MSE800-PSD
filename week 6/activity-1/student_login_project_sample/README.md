# Student Login Project — Python Decorator Sample

A small teaching project that demonstrates how a Python **decorator** can be
used to attach cross-cutting behaviour (here: activity logging) to several
unrelated functions without duplicating code.

## Project structure

| File | Role |
|------|------|
| `decorators.py` | Defines the `log_activity` decorator. |
| `users.py` | Defines three student-action functions, each decorated with `@log_activity`. |
| `main.py` | Entry point — simulates a sequence of student activities. |
| `README.md` | This file — debugging notes and findings. |

## How the decorator is used

`log_activity` is defined in `decorators.py`. It is a classic Python decorator:

1. It takes the original function `func` as input.
2. It defines an inner `wrapper(*args, **kwargs)` that:
   - prints a banner, the function name (`func.__name__`) and the current
     timestamp **before** calling `func`,
   - calls `func(*args, **kwargs)` and captures its `result`,
   - prints a closing banner **after** the call,
   - returns the captured `result` so the wrapped function still behaves
     normally from the caller's perspective.
3. It returns the `wrapper`, which replaces the original function.

In `users.py`, the decorator is applied with the `@log_activity` syntax to
three different functions with **different signatures**:

```python
@log_activity
def student_login(username): ...

@log_activity
def submit_assignment(username, assignment): ...

@log_activity
def view_grades(username): ...
```

Because `wrapper` accepts `*args, **kwargs`, the same decorator works for all
three signatures without modification. `main.py` then calls these functions
normally — it has no knowledge of the decorator, yet every call is logged.

## Debugging process

The code as supplied works, so debugging consisted of **tracing execution**
and **verifying invariants** rather than fixing bugs. I added inline comments
to each function describing what was checked:

1. **`decorators.py → log_activity` / `wrapper`**
   - Verified `func.__name__` resolves to the *original* function's name
     (e.g. `student_login`), not `wrapper`.
   - Verified `*args, **kwargs` correctly forward arguments to functions with
     different signatures.
   - Verified `return result` is present — a common decorator pitfall is to
     forget this line, which silently drops any return value.

2. **`users.py` (three decorated functions)**
   - Ran `main.py` and confirmed each function produced exactly one logged
     block, in the order it was called.
   - Confirmed that decorating multiple functions with the same decorator
     does not cause any shared/mutable state issues — each invocation creates
     its own `wrapper` frame.

3. **`main.py → main`**
   - Confirmed the `if __name__ == "__main__":` guard correctly gates the
     call to `main()` so importing the module would not auto-execute it.
   - Confirmed the username differs between calls (`Mohammad` vs `Alex`) and
     the decorator does not "freeze" caller-specific data.

### Observed output

```
===================================
Function: student_login
Time: 2026-05-16 03:07:15.562684
Activity started...
Mohammad logged into the system.
Activity completed.
===================================
... (similar blocks for submit_assignment and view_grades)
```

This matches the expected behaviour: pre-call log → original print → post-call
log, repeated once per call.

## Findings / Conclusion

- The decorator pattern is used here as a **lightweight, reusable logging
  layer**. Without it, each of the three functions in `users.py` would need
  its own banner/timestamp/closing print statements — three copies of the
  same boilerplate.
- Using `*args, **kwargs` inside `wrapper` is what makes a single decorator
  usable across functions of different arity. This is the key generalisation
  step.
- Returning `result` from `wrapper` preserves transparency: callers see the
  same return value they would have seen without the decorator.
- The project is a clean example of **separation of concerns**: business
  logic (what the student does) lives in `users.py`; cross-cutting concerns
  (logging) live in `decorators.py`; orchestration lives in `main.py`.
- No defects were found during debugging — the sample is correct as supplied
  and produces deterministic, well-ordered output.

## How to run

```bash
python3 main.py
```