import argparse

#adding praser
ap = argparse.ArgumentParser()

#adding argument
ap.add_argument("n1",type=float , help="number 1")
ap.add_argument("n2",type=float , help="number 2")
ap.add_argument("n3",type=float , help="number 3")
ap.add_argument("n4",type=float , help="number 4")

#reading agrument
i_read_argument = vars(ap.parse_args())

print(i_read_argument)