# RPG Character Creator

A Python function that generates a simple RPG character sheet with name and stat validation.

---

## Overview

`create_character` takes a character name and three stats — **Strength**, **Intelligence**, and **Charisma** — and returns a formatted character sheet.

Stats are represented as dot bars with 10 positions, where filled dots (`●`) represent the stat value and empty dots (`○`) represent the remaining slots.

**Example output:**

```
Pedro
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○
```

---

## Function Signature

```python
create_character(name, strength, intelligence, charisma)
```

| Parameter      | Type   | Description                        |
|----------------|--------|------------------------------------|
| `name`         | `str`  | Character name                     |
| `strength`     | `int`  | Strength stat (STR)                |
| `intelligence` | `int`  | Intelligence stat (INT)            |
| `charisma`     | `int`  | Charisma stat (CHA)                |

---

## Code Structure and Flow

The function follows a **fail-fast** pattern: every input is validated before any output is generated. If any check fails, the function immediately returns an error message and stops — it never reaches the next step.

This is a common pattern in automation and security tools, where you never want to process invalid or unexpected input.

### Step 1 — Name Type Check

```python
if not isinstance(name, str):
    return "The character name should be a string"
```

The first check verifies that `name` is actually a string. This prevents unexpected types (integers, lists, `None`) from being passed as a name.

### Step 2 — Name Content Checks

```python
if name == "":
    return "The character should have a name"
if len(name) > 10:
    return "The character name is too long"
if " " in name:
    return "The character name should not contain spaces"
```

After confirming the type, the function checks the content of the string:
- Rejects empty strings
- Enforces a maximum length of 10 characters
- Rejects names with spaces

These checks happen in order — if the name is empty, there is no point checking its length.

### Step 3 — Stats Type Check

```python
if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
    return "All stats should be integers"
```

All three stats are checked at once. If any of them is not an integer (for example, a float or a string), the function stops here.

### Step 4 — Stats Value Checks

```python
if strength < 1 or intelligence < 1 or charisma < 1:
    return "All stats should be no less than 1"
if strength > 4 or intelligence > 4 or charisma > 4:
    return "All stats should be no more than 4"
if strength + intelligence + charisma != 7:
    return "The character should start with 7 points"
```

Three separate value checks are applied:
- Each stat must be at least 1 (no zero or negative values)
- Each stat must be at most 4
- The total of all stats must equal exactly 7

The order matters here too — checking the range before the total avoids misleading errors. If a stat is 10, it is more accurate to say "stat is too high" than "total is wrong".

### Step 5 — Output Generation

```python
str_line = "STR " + full_dot * strength + empty_dot * (10 - strength)
int_line = "INT " + full_dot * intelligence + empty_dot * (10 - intelligence)
cha_line = "CHA " + full_dot * charisma + empty_dot * (10 - charisma)

return name + "\n" + str_line + "\n" + int_line + "\n" + cha_line
```

Only after all validations pass does the function build the output. Each stat line is constructed by repeating the filled dot character by the stat value, and the empty dot for the remaining positions up to 10. The lines are then joined with newline characters and returned as a single string.

---

## Full Flow Diagram

```
Input received
     │
     ▼
Is name a string? ──No──► Return error
     │ Yes
     ▼
Is name valid (not empty, ≤10 chars, no spaces)? ──No──► Return error
     │ Yes
     ▼
Are all stats integers? ──No──► Return error
     │ Yes
     ▼
Are all stats between 1 and 4? ──No──► Return error
     │ Yes
     ▼
Do stats total exactly 7? ──No──► Return error
     │ Yes
     ▼
Build and return character sheet
```

---

## Requirements

- Python 3.x
- No external libraries needed

---

## Author

[pedromarinflach-cyber](https://github.com/pedromarinflach-cyber)
