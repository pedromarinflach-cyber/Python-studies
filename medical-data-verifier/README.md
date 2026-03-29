# Medical Records Validator

A Python script that validates a list of patient medical records against a defined format and field constraints.

---

## Overview

`validate` receives a list of patient dictionaries and checks whether every record conforms to the expected structure and value rules. Invalid fields are reported individually — specifying the field name, the value, and the position of the record in the list.

**Example output (invalid data):**

```
Unexpected format 'patient_id: p1002' at position 1.
Unexpected format 'gender: male' at position 1.
Unexpected format 'last_visit_id: v2302' at position 2.
```

**Example output (valid data):**

```
Valid format.
```

---

## Function Signatures

```python
find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id)
validate(data)
```

### `find_invalid_records`

| Parameter | Type | Valid Condition |
|-----------|------|-----------------|
| `patient_id` | `str` | Matches pattern `P` followed by digits — case-insensitive (`P1001`, not `p1002`) |
| `age` | `int` | Integer, 18 or older |
| `gender` | `str` | `"Male"` or `"Female"` — case-insensitive |
| `diagnosis` | `str` or `None` | String or explicitly `None` |
| `medications` | `list` | List where every item is a string |
| `last_visit_id` | `str` | Matches pattern `V` followed by digits — case-insensitive (`V2301`, not `v2302`) |

### `validate`

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | `list` or `tuple` | Collection of patient record dictionaries |

---

## Code Structure and Flow

The script is split into two functions with distinct responsibilities. `find_invalid_records` handles field-level validation for a single record. `validate` handles structural validation for the entire dataset and orchestrates the calls to `find_invalid_records`.

### `find_invalid_records` — Field-Level Validation

Unlike the fail-fast pattern, this function evaluates **all fields at once** using a dictionary of boolean constraints. Every field is checked regardless of whether others have already failed — the goal is to report every invalid field in a record, not just the first one.

#### Step 1 — Build the constraints dictionary

```python
constraints = {
    'patient_id': isinstance(patient_id, str)
        and re.fullmatch(r'P\d+', patient_id, re.IGNORECASE),
    'age': isinstance(age, int) and age >= 18,
    'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
    'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
    'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
    'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'V\d+', last_visit_id, re.IGNORECASE)
}
```

Each key maps to a boolean expression. `re.fullmatch` is used for `patient_id` and `last_visit_id` — it requires the entire string to match the pattern, not just a substring. The `re.IGNORECASE` flag makes the match case-insensitive, but the data is still expected to use uppercase (`P`, `V`) — records with lowercase prefixes are flagged as invalid.

#### Step 2 — Return the list of failed fields

```python
return [key for key, value in constraints.items() if not value]
```

A list comprehension filters only the keys whose constraint evaluated to `False`. If all fields are valid, an empty list is returned.

---

### `validate` — Structural and Dataset-Level Validation

This function operates in layers — structural checks first, field-level checks last. It never stops early: even if one record is malformed, it continues checking the rest.

#### Step 1 — Check the container type

```python
is_sequence = isinstance(data, (list, tuple))
if not is_sequence:
    print('Invalid format: expected a list or tuple.')
    return False
```

The entire dataset must be a list or tuple. Anything else (a single dictionary, a string, `None`) is rejected immediately — there is no point iterating over something that is not a sequence.

#### Step 2 — Iterate and check each record's type

```python
for index, dictionary in enumerate(data):
    if not isinstance(dictionary, dict):
        print(f'Invalid format: expected a dictionary at position {index}.')
        is_invalid = True
        continue
```

Each item in the sequence must be a dictionary. If it is not, a message is printed, `is_invalid` is set to `True`, and the loop continues to the next record — the malformed item is skipped rather than crashing the validator.

#### Step 3 — Check for correct keys

```python
key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

if set(dictionary.keys()) != key_set:
    print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
    is_invalid = True
    continue
```

The set of keys in the dictionary is compared against the expected set. Set comparison catches both missing keys and unexpected extra keys in one operation. If the keys do not match exactly, field-level validation is skipped for that record — it cannot be safely unpacked.

#### Step 4 — Field-level validation via `find_invalid_records`

```python
invalid_records = find_invalid_records(**dictionary)
for key in invalid_records:
    val = dictionary[key]
    print(f"Unexpected format '{key}: {val}' at position {index}.")
    is_invalid = True
```

The dictionary is unpacked with `**` and passed directly to `find_invalid_records`. Each invalid field returned is reported with its key, its actual value, and the index of the record in the dataset.

#### Step 5 — Final result

```python
if is_invalid:
    return False
print('Valid format.')
return True
```

After all records have been checked, the function returns `False` if any issue was found, or prints `'Valid format.'` and returns `True` if everything passed.

---

## Full Flow Diagram

```
validate(data) called
     │
     ▼
Is data a list or tuple? ──No──► Print error, return False
     │ Yes
     ▼
For each item in data:
     │
     ├──► Is item a dict? ──No──► Print error, set is_invalid, continue
     │
     ├──► Does item have exactly the right keys? ──No──► Print error, set is_invalid, continue
     │
     └──► Call find_invalid_records(**item)
               │
               ▼
          Evaluate all field constraints simultaneously
               │
               ▼
          Return list of failed fields
               │
               ▼
          For each failed field → print field, value, and position
               │
               ▼
          Set is_invalid = True if any field failed
     │
     ▼
All records checked
     │
     ├──► is_invalid == True ──► return False
     │
     └──► is_invalid == False ──► print 'Valid format.', return True
```

---

## Origin

Developed as part of a course on [freeCodeCamp](https://www.freecodecamp.org/).

---

## Requirements

- Python 3.x
- Standard library only — `re` module (no external dependencies)

---

## Author

[pedromarinflach-cyber](https://github.com/pedromarinflach-cyber)
