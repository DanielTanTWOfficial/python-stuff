import argparse

parser = argparse.ArgumentParser(description='Calculate the product of a given number times 2')
parser.add_argument("-d", "--double", help="display the result of a given number times 2",
                    type=int)
args = parser.parse_args()
print(args.double*2)