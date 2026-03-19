# 🚗 Transport Decision

This project is a simple Python script that simulates a real-life decision: whether a person should go somewhere based on different conditions.

---

## 📌 Project Idea

The goal of this project is to practice conditional logic by modeling a common situation:

> “Should I go or not based on distance, weather, and transportation options?”

Instead of solving abstract problems, this script applies logic to something practical and easy to understand.

---

## ⚙️ How it works

The script takes into account the following variables:

* `distance_mi` → distance to the destination (in miles)
* `is_raining` → whether it is raining or not
* `has_bike` → if a bike is available
* `has_car` → if a car is available
* `has_ride_share_app` → if a ride-sharing option is available

Based on these factors, the program returns:

* `True` → go
* `False` → do not go

---

## 🔍 Decision Logic

The logic follows these general rules:

### 📏 Short distance (≤ 1 mile)

* If it's not raining → go
* If it's raining → don't go

### 🚴 Medium distance (1 to 6 miles)

* If no bike is available → don't go
* If it's raining → don't go
* If bike is available and it's not raining → go

### 🚗 Long distance (> 6 miles)

* If ride-sharing is available → go
* If a car is available → go
* Otherwise → don't go

---

## ▶️ How to run

1. Clone the repository
2. Open the project folder
3. Run the script:

```
python transport_decision.py
```

---

## ▶️ Example

**Input:**

```
Distance: 2
Raining: False
Has bike: True
Has car: True
Ride share: False
```

**Output:**

```
True
```

---

## 🧪 What I practiced

* Writing conditional statements (`if`, `elif`, `else`)
* Structuring decision logic step by step
* Thinking about real-world scenarios in code
* Handling multiple variables at the same time

---

## ⚠️ Limitations

* Not all variables are taken as user input yet
* The logic could be simplified and optimized
* Some conditions are repetitive

---

## 🔧 Possible Improvements

* Refactor the logic to make it cleaner and more efficient
* Turn the script into a reusable function
* Allow user input for all variables
* Add more conditions (time, urgency, cost, etc.)
* Build a simple interface (CLI or web version)

---

## 💡 Final Thoughts

This is a simple project, but it represents an important step in developing logical thinking and problem-solving skills.

The focus is on consistency and building a solid foundation for more complex projects in the future.
