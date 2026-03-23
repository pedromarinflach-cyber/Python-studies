# Guess The Number

A Python script that simulates a classic number guessing game where the player must find a randomly generated secret number through directional feedback.

---

## Overview

The script generates a random number between 1 and 20 and prompts the player to guess it. After each guess, it responds with **Too low**, **Too high**, or **Out of range** until the player gets it right — then it shows how many attempts it took.

**Example output:**

```
I'm thinking of a number between 1 and 20
Take a guess: 10
Too low, try again.
Take a guess: 17
Too high, try again.
Take a guess: 14
You got it in 3 tries!
```

---

## Variables

| Variable | Type  | Description                                      |
|----------|-------|--------------------------------------------------|
| `secret` | `int` | Randomly generated target number (1–20)          |
| `tries`  | `int` | Counter for the number of attempts made          |
| `guess`  | `int` | The player's current guess (converted from input)|
| `text`   | `str` | Raw string returned by `input()`                 |

---

## Code Structure and Flow

The script uses a `while True` loop that runs indefinitely until the correct guess triggers a `break`. Every guess passes through the same validation and feedback chain.

### Step 1 — Generate Secret Number

```python
import random

secret = random.randint(1, 20)
tries = 0
```

A random integer between 1 and 20 (inclusive) is generated using `random.randint()`. The attempt counter starts at 0.

### Step 2 — Game Loop

```python
while True:
    text = input("Take a guess: ")
    guess = int(text)
    tries += 1
```

The loop runs until broken. Each iteration reads a new guess from the player via `input()`, converts it from string to integer with `int()`, and increments the attempt counter.

### Step 3 — Range Validation

```python
if guess < 1 or guess > 20:
    print("That number is out of range. Try again.")
```

If the guess falls outside the valid range, the player is warned. The loop continues — the attempt still counts.

### Step 4 — Directional Feedback

```python
elif guess < secret:
    print("Too low, try again.")
elif guess > secret:
    print("Too high, try again.")
```

If the guess is within range but wrong, the script tells the player which direction to adjust.

### Step 5 — Win Condition

```python
else:
    print("You got it in", tries, "tries!")
    break
```

When `guess == secret`, the script prints the final result and exits the loop with `break`. This is the only exit point.

---

## Full Flow Diagram

```
Game starts
     │
     ▼
Generate secret number (1–20), set tries = 0
     │
     ▼
Player enters a guess
     │
     ▼
Is guess < 1 or > 20? ──Yes──► "Out of range" → loop again
     │ No
     ▼
Is guess < secret? ──────Yes──► "Too low" → loop again
     │ No
     ▼
Is guess > secret? ──────Yes──► "Too high" → loop again
     │ No
     ▼
guess == secret ──────────────► "You got it in X tries!" → break
```

---

## Known Limitations

- No input error handling — typing letters will crash the program with a `ValueError`
- The number range is hardcoded to 1–20
- No option to play again without restarting the script
- Out-of-range guesses still increment the tries counter

---

## Possible Improvements

- Add a `try / except` block to handle non-numeric input gracefully
- Let the player choose the difficulty range via `input()`
- Add a play-again prompt at the end using an outer loop
- Stop counting out-of-range guesses as valid attempts
- Track and display the player's best score across rounds

---

## What I Practiced

- Using `random.randint()` to generate random numbers
- Reading and converting user input with `input()` and `int()`
- Structuring game logic with `while True` and `break`
- Handling edge cases with range validation
- Tracking state across loop iterations with a counter

---

## Requirements

- Python 3.x
- No external libraries needed

---

## Origin

Developed as part of the [Python Simple Demo](https://tryhackme.com/room/pythonsimpledemo) room on TryHackMe.

---

## Author

[pedromarinflach-cyber](https://github.com/pedromarinflach-cyber)
