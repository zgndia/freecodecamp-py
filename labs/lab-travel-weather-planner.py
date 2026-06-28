distance_mi = 7
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print("False")
elif distance_mi <= 1:
    if not is_raining:
        print("True")
    else:
        print("False")

if distance_mi > 1 and distance_mi <= 6:
    if is_raining and not has_bike:
        print("False")
    elif not is_raining and not has_bike:
        print("False")
    elif not is_raining and has_bike:
        print("True")
elif distance_mi > 6:
    if has_ride_share_app:
        print("True")
    if has_car:
        print("True")
    if not has_car and not has_ride_share_app:
        print("False")