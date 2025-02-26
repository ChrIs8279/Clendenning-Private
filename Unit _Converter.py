
class UnitsConverter:

    def meters_to_kilometers(self,meters):
        return meters / 1000

    def kilometers_to_meters(self,kilometers):
        return kilometers * 1000

    def feet_to_meters(self,feet):
        return feet * 0.3048

    def meters_to_feet(self,meters):
        return meters / 0.3048

    def miles_to_kilometers(self,miles):
        return miles * 1.60934

    def kilometers_to_miles(self,kilometers):
        return kilometers / 1.60934

    def length_converter(self):
        print("Length Converter")
        print("1. Meters to Kilometers")
        print("2. Kilometers to Meters")
        print("3. Feet to Meters")
        print("4. Meters to Feet")
        print("5. Miles to Kilometers")
        print("6. Kilometers to Miles")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            meters = float(input("Enter length in meters: "))
            print("Length in kilometers:", self.meters_to_kilometers(meters))
        elif choice == 2:
            kilometers = float(input("Enter length in kilometers: "))
            print("Length in meters:", self.kilometers_to_meters(kilometers))
        elif choice == 3:
            feet = float(input("Enter length in feet: "))
            print("Length in meters:", self.feet_to_meters(feet))
        elif choice == 4:
            meters = float(input("Enter length in meters: "))
            print("Length in feet:", self.meters_to_feet(meters))
        elif choice == 5:
            miles = float(input("Enter length in miles: "))
            print("Length in kilometers:", self.miles_to_kilometers(miles))
        elif choice == 6:
            kilometers = float(input("Enter length in kilometers: "))
            print("Length in miles:", self.kilometers_to_miles(kilometers))
        else:
            print("Invalid choice")


if __name__ == "__main__":
    converter = UnitsConverter()
    converter.length_converter()