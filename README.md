# Python Studies

This repository contains some of my Python learning exercises and small projects.
The goal is to practice logic, problem-solving, and start building simple systems that simulate real situations.

##  What I'm learning

* Python basics
* Automation
* Security-related scripts
* Logical thinking applied to real-world scenarios

---

## Project: `transport_decision.py`

This project is a simple decision-making script.
It determines whether a person should go somewhere based on a few conditions like distance, weather, and available transportation.

### Idea behind the project

I wanted to simulate a real-life situation using conditional logic.
Instead of just doing abstract exercises, this script tries to model a practical decision: *“Should I go or not?”*

---

##  Variables used

The decision is based on:

* `distance_mi` → distance to the destination
* `is_raining` → whether it's raining or not
* `has_bike` → if a bike is available
* `has_car` → if a car is available
* `has_ride_share_app` → if ride-sharing is an option

---

##  Decision logic (simplified)

* Very short distance (≤ 1 mile):

  * If it's not raining → go
  * If it's raining → don't go

* Medium distance (1 to 6 miles):

  * Depends on weather and bike availability

* Long distance (> 6 miles):

  * Requires either a car or ride-sharing

If none of the conditions are met → don't go.

---

##  Example

**Input:**

```
Distance: 2
Raining: False
Has bike: True
```

**Output:**

```
True
```

---

##  What I practiced with this project

* Writing multiple conditional statements (`if`, `elif`, `else`)
* Structuring decision logic
* Thinking about edge cases
* Turning a real situation into code

---

##  Possible improvements

* Refactor the logic to make it cleaner and less repetitive
* Turn the script into a function
* Let the user input all variables (not just distance)
* Create a simple interface (CLI or web)

---
##  Final note

This is a small project, but the focus here is on building logic and consistency.
Over time, the goal is to evolve from simple scripts like this into more complete and scalable systems.
