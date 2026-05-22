# Factory Design Pattern — `factory_pattern.py`
How the Pattern Is Used in the Sample Code

The file `factory_pattern.py` implements two parallel hierarchies:

### A. The Factory hierarchy (the "creators")

| Class            | Role                                      |
|------------------|-------------------------------------------|
| `Factory`        | Abstract base class — defines the contract `create_product()` |
| `AnimalFactory`  | Concrete factory — knows how to build a `Dog` or a `Cat` based on the `kind` argument |
| `DogFactory`     | Concrete factory — intended to build only `Dog` objects |
| `CatFactory`     | Concrete factory — intended to build only `Cat` objects |

### B. The Product hierarchy (the "things being created")

| Class     | Role                                  |
|-----------|---------------------------------------|
| `Animals` | Abstract base class — defines the contract `run()` |
| `Dog`     | Concrete product — implements `run()` |
| `Cat`     | Concrete product — implements `run()` |

The **client** (bottom of the file) does not call `Dog()` or `Cat()` directly
to use the pattern — it asks a factory:

```python
factory = DogFactory()
dog = factory.create_product()
dog.run()
```

---

## Are There Classes and Subclasses?

**Yes — there are two distinct inheritance hierarchies:**

```
Factory (ABC)                Animals (ABC)
   ├── AnimalFactory             ├── Dog
   ├── DogFactory                └── Cat
   └── CatFactory
```

- `Factory` is an **abstract superclass**; `AnimalFactory`, `DogFactory`, and
  `CatFactory` are its **subclasses**.
- `Animals` is an **abstract superclass**; `Dog` and `Cat` are its
  **subclasses**.
- The abstract method `create_product()` in `Factory` and `run()` in `Animals`
  *force* every subclass to provide its own implementation.

---

## Outcome of the Implementation

### What actually runs

```python
factory = DogFactory()
dog = Dog()
dog = factory.create_product()
dog.run()
```

1. A `DogFactory` instance is created.
2. A `Dog` instance is created directly (then immediately overwritten).
3. `factory.create_product()` is called on the `DogFactory`.
4. `dog.run()` is invoked.

### Expected vs. actual behaviour

- **Expected (if the pattern were fully wired up):** the factory would
  produce a `Dog` and the program would print:
  ```
  I'm a Dog, I can run!!
  ```

- **Actual:** `DogFactory.create_product()` currently has only `pass` as its
  body, so it returns `None`. The variable `dog` is then re-bound to `None`,
  and the final line `dog.run()` raises:
  ```
  AttributeError: 'NoneType' object has no attribute 'run'
  ```

### How to make it work

Either:

**Option 1 — use `AnimalFactory` (which is fully implemented):**
```python
factory = AnimalFactory()
dog = factory.create_product("dog")
dog.run()        # I'm a Dog, I can run!!

cat = factory.create_product("cat")
cat.run()        # I'm a Cat, I can run!!
```

**Option 2 — finish `DogFactory` / `CatFactory`:**
```python
class DogFactory(Factory):
    def create_product(self, kind=None):
        return Dog()

class CatFactory(Factory):
    def create_product(self, kind=None):
        return Cat()
```

---

## Key Takeaways

- The sample demonstrates the **Factory Pattern** by separating *who creates
  the object* (`*Factory` classes) from *who uses it* (the client).
- It uses **abstract base classes** (`ABC`) and `@abstractmethod` to enforce
  the contracts on both factories and products.
- It contains **two class-and-subclass hierarchies**: factories and animals.
- As written, only `AnimalFactory` is functional; `DogFactory` and
  `CatFactory` are stubs, so running the script as-is will raise an
  `AttributeError`. Filling in their `create_product()` methods completes the
  pattern.
