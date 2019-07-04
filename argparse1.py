import argparse

parser = argparse.ArgumentParser(description='Calculate the square of a number')
parser.add_argument("num2square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.num2square**2)