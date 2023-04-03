class TemperatureConversion:

    def __init__(self, temp=1):
        self._temp = temp

    def celsius_to_fahrenheit(self):
        return (self._temp * 9) / 5 + 32

    def celsius_to_kelvin(self):
        return self._temp + 273.15

    def fahrenheit_to_celsius(self):
        return (self._temp - 32) * 5 / 9

    def kelvin_to_celsius(self):
        return self._temp - 273.15


def main():
    temp_in_celsius = float(input("Enter the temperature in Celsius: "))
    temp_conversion = TemperatureConversion(temp_in_celsius)

    print(str(temp_conversion.celsius_to_kelvin()) + " Kelvin")
    print(str(temp_conversion.celsius_to_fahrenheit()) + " Fahrenheit")

    temp_in_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    temp_conversion = TemperatureConversion(temp_in_fahrenheit)

    print(str(temp_conversion.fahrenheit_to_celsius()) + " Celsius")

    temp_in_kelvin = float(input("Enter the temperature in Kelvin: "))
    temp_conversion = TemperatureConversion(temp_in_kelvin)

    print(str(temp_conversion.kelvin_to_celsius()) + " Celsius")


if __name__ == '__main__':
    main()
