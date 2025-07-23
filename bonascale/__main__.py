# bonascale/__main__.py
import argparse
from bonaventure_scale import (
    bonaventure_to_celsius,
    bonaventure_to_fahrenheit,
    bonaventure_to_kelvin,
)

def main():
    parser = argparse.ArgumentParser(description="Convert Bonaventure Scale (\u00b0B) to other temperature units.")
    parser.add_argument("value", type=float, help="Temperature in \u00b0B")
    parser.add_argument("--to", choices=["celsius", "fahrenheit", "kelvin"], required=True, help="Target scale")

    args = parser.parse_args()

    if args.to == "celsius":
        result = bonaventure_to_celsius(args.value)
        print(f"{args.value} \u00b0B = {result:.2f} \u00b0C")
    elif args.to == "fahrenheit":
        result = bonaventure_to_fahrenheit(args.value)
        print(f"{args.value} \u00b0B = {result:.2f} \u00b0F")
    elif args.to == "kelvin":
        result = bonaventure_to_kelvin(args.value)
        print(f"{args.value} \u00b0B = {result:.2f} K")

if __name__ == "__main__":
    main()
