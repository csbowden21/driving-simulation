import random
import time

travel_speed = 55

def speed_control(speed):
    kmh = round(speed * 1.60934)
    return kmh

def vehicle_feed(mile):
    kmh = speed_control(travel_speed)
    encounters = ["Obstruction on Road", "Road Construction",
                  "Yellow Light", "Red Light", "Pedestrian Crossing Street"]

    while mile > 0:
        adjusted_speed = random.randint(1, 45)
        adjusted_kmh = round(adjusted_speed * 1.60934)
        time.sleep(1)
        mile -= 1
        print("=" * 45)
        print(f"Current Mile: {mile}")

        if mile == 0:
            print("Vehicle Status Update: Destination Reached")
        elif mile % 3 == 0 or mile % 5 == 0:
            random_encounter = random.choice(encounters)
            if random_encounter == "Red Light":
                adjusted_speed = 0
                adjusted_kmh = 0
            print(f"Vehicle Status Update: {random_encounter}")
            print(f"Current Vehicle Speed: {adjusted_speed} mph/{adjusted_kmh} kmh")
        else:
            print("Vehicle Status Update: Nothing to Report")
            print(f"Current Vehicle Speed: {travel_speed} mph/{kmh} kmh")

vehicle_feed(100)
