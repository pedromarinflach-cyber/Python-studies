# Transport Decision

A Python script that simulates a real-life decision: whether a person should travel to a destination based on distance, weather, and available transportation.

---

## Overview

The script evaluates five variables and returns `True` (go) or `False` (do not go) based on a set of conditional rules that mirror how someone would actually think through this decision.

**Variables:**

| Variable             | Type    | Description                          |
|----------------------|---------|--------------------------------------|
| `distance_mi`        | `int`   | Distance to destination in miles     |
| `is_raining`         | `bool`  | Whether it is currently raining      |
| `has_bike`           | `bool`  | Whether a bike is available          |
| `has_car`            | `bool`  | Whether a car is available           |
| `has_ride_share_app` | `bool`  | Whether a ride-sharing app is available |

---

## Code Structure and Flow

The script uses a chain of `if / elif / else` conditions to evaluate the situation step by step. Each condition is checked in order — the first one that matches determines the output, and the rest are skipped.

### Step 1 — No Distance

```python
if not distance_mi:
    print(False)
```

If `distance_mi` is `0` or not set, the script immediately outputs `False`. There is no destination to go to.

### Step 2 — Short Distance (≤ 1 mile)

```python
elif distance_mi <= 1 and not is_raining:
    print(True)
elif distance_mi <= 1 and is_raining:
    print(False)
```

For short distances, the only factor that matters is the weather:
- Not raining → go
- Raining → don't go

A short distance is walkable, so no transportation is required — but rain makes it impractical.

### Step 3 — Medium Distance (1 to 6 miles)

```python
elif distance_mi > 1 and distance_mi <= 6 and is_raining and not has_bike:
    print(False)
elif distance_mi > 1 and distance_mi <= 6 and not is_raining and not has_bike:
    print(False)
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print(True)
```

For medium distances, two factors are evaluated together:
- No bike available → don't go, regardless of weather
- Bike available but raining → don't go (no condition matches, falls to `else`)
- Bike available and not raining → go

Note: a bike is the only transportation considered viable for this range. Having a car does not change the outcome here.

### Step 4 — Long Distance (> 6 miles)

```python
elif distance_mi > 6 and has_ride_share_app:
    print(True)
elif distance_mi > 6 and has_car:
    print(True)
```

For long distances, motorized transport is required:
- Ride-share available → go
- Car available → go

Both conditions are checked separately so that either one is enough to proceed.

### Step 5 — Default

```python
else:
    print(False)
```

If none of the conditions above matched, the script defaults to `False`. This covers edge cases like medium distance with a bike but raining, or long distance with no car and no ride-share.

---

## Full Flow Diagram

```
Input received
     │
     ▼
distance_mi is 0 or missing? ──Yes──► False
     │ No
     ▼
distance_mi ≤ 1?
     ├── Yes → is_raining? ──Yes──► False
     │                    └──No───► True
     │
     ▼
distance_mi between 1 and 6?
     ├── No bike → False
     ├── Bike + raining → False (else)
     └── Bike + not raining → True
     │
     ▼
distance_mi > 6?
     ├── has_ride_share_app → True
     ├── has_car → True
     └── Neither → False (else)
```

---

## Example

**Input (hardcoded in the script):**

```python
distance_mi = 8
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False
```

**Execution path:**

1. `distance_mi` is 8 — not zero, move on
2. Not ≤ 1 — skip short distance checks
3. Not between 1 and 6 — skip medium distance checks
4. Greater than 6 — check long distance conditions
5. `has_ride_share_app` is `False` — skip
6. `has_car` is `True` → **output: `True`**

---

## Known Limitations

- All variables are hardcoded — there is no user input yet
- Some conditions in the medium distance range are repetitive and could be simplified
- Rain is not considered for long distances (having a car or ride-share overrides weather)

---

## Possible Improvements

- Refactor repeated conditions using cleaner boolean logic
- Wrap the script in a reusable function with parameters
- Accept user input via `input()` or command-line arguments
- Add additional factors such as time, urgency, or cost
- Build a simple CLI or web interface

---

## What I Practiced

- Writing and structuring `if / elif / else` chains
- Modeling real-world decision logic in code
- Handling multiple boolean variables simultaneously
- Thinking through edge cases and default behaviors

---

## Requirements

- Python 3.x
- No external libraries needed

---

## Author

[pedromarinflach-cyber](https://github.com/pedromarinflach-cyber)
