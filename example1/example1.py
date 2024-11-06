class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

def main():
    # Examples of Fahrenheit to Celsius
    print(f"32°F is {TemperatureConverter.fahrenheit_to_celsius(32):.2f}°C")
    print(f"-40°F is {TemperatureConverter.fahrenheit_to_celsius(-40):.2f}°C")
    print(f"63°F is {TemperatureConverter.fahrenheit_to_celsius(63):.2f}°C")

    # Examples of Celsius to Fahrenheit
    print(f"100°C is {TemperatureConverter.celsius_to_fahrenheit(100):.2f}°F")
    print(f"37°C is {TemperatureConverter.celsius_to_fahrenheit(37):.2f}°F")
    print(f"8°C is {TemperatureConverter.celsius_to_fahrenheit(8):.2f}°F")

if __name__ == "__main__":
    main()
