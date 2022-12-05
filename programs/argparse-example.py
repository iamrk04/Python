import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-sq",
    "--square",
    # dest="square",
    help="display square of given number",
    type=int,
    default=0,
    choices=[0, 1, 2, 3],
    nargs="*"
)
args = parser.parse_args()
print(args.square)
# print(args.square**2)








