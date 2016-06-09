import argparse
import pandas

def gdd_calc(filename, tbase, tupper):
#    datafile= open(filename, "r")
#    data = datafile.read()
#    for line in data:
	GDD = 0
	df = pandas.read_csv(filename)
	sum =df.row['Max_Temp'] + df.row['Min_Temp']
	GDD =(float(sum)/2.0) + tbase
	return GDD

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The Fibonacci number you wish to calculate.", type=str)
    parser.add_argument("numeric", help="The Fibonacci number you wish to calculate.", type=float)
    parser.add_argument("numeric1", help="The Fibonacci number you wish to calculate.", type=float)

    args = parser.parse_args()
    
    result = gdd_calc(args.filename, args.numeric, args.numeric1)
    print ("The fib number is ", + str(result))

if __name__ == '__main__':
    Main()
