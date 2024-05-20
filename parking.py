import random
import string

class ParkingLot:
    def __init__(self, square_footage, spot_length=8, spot_width=12):
        self.square_footage = square_footage
        self.spot_size = spot_length * spot_width
        self.total_spots = self.square_footage // self.spot_size
        self.spots = [None] * self.total_spots
    
    def __repr__(self):
        return f"<ParkingLot: {self.total_spots} spots, {self.square_footage} sqft>"

class Car:
    def __init__(self, license_plate):
        if len(license_plate) != 7:
            raise ValueError("License plate must be exactly 7 characters long.")
        self.license_plate = license_plate
    
    def __str__(self):
        return self.license_plate
    
    def park(self, parking_lot, spot_num):
        if spot_num < 0 or spot_num >= parking_lot.total_spots:
            return f"Spot number {spot_num} is out of range."
        
        if parking_lot.spots[spot_num] is not None:
            return f"Spot number {spot_num} is already occupied."
        
        parking_lot.spots[spot_num] = self
        return f"Car with license plate {self.license_plate} parked successfully in spot {spot_num}."

def generate_random_license_plate():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

def main():
    square_footage = 2000
    parking_lot = ParkingLot(square_footage)
    print(parking_lot)
    
    cars = [Car(generate_random_license_plate()) for _ in range(25)]
    
    for car in cars:
        parked = False
        attempts = 0
        while not parked and attempts < parking_lot.total_spots:
            spot_num = random.randint(0, parking_lot.total_spots - 1)
            result = car.park(parking_lot, spot_num)
            attempts += 1
            if "successfully" in result:
                parked = True
                print(result)
            elif attempts == parking_lot.total_spots:
                print(f"Car with license plate {car.license_plate} could not find an empty spot.")
        
        if all(spot is not None for spot in parking_lot.spots):
            print("Parking lot is full.")
            break

if __name__ == "__main__":
    main()