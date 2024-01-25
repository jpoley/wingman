class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    examples_fahrenheit = [32, -40, 63]
    examples_celsius = [100, 37, 8]
    
    for fahrenheit in examples_fahrenheit:
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        converted_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
        print(f"{fahrenheit} degrees F = {celsius} degrees C")
        print(f"{celsius} degrees C = {converted_fahrenheit} degrees F")
    
    for celsius in examples_celsius:
        fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
        converted_celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        print(f"{celsius} degrees C = {fahrenheit} degrees F")
        print(f"{fahrenheit} degrees F = {converted_celsius} degrees C")
