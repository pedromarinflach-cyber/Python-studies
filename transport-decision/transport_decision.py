** start of main.py **

distance_mi = 8
is_raining = True 
has_bike = False 
has_car = True 
has_ride_share_app= False
if not distance_mi:
    print(False)
elif distance_mi <= 1 and not is_raining:
    print(True)
elif distance_mi <= 1 and is_raining:
    print(False)
elif distance_mi > 1 and distance_mi <= 6 and is_raining and not has_bike:
    print(False)
elif distance_mi > 1 and distance_mi <= 6 and not is_raining and not has_bike:
    print(False)
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print(True)
elif distance_mi > 6 and has_ride_share_app:
    print(True)
elif distance_mi > 6 and has_car:
    print(True)
else:
    print(False)

** end of main.py **

