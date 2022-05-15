import csv
import sys

def read_data(filepath):
    try:
        header = True
        data = []
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if header: 
                    header = False
                else:
                    data.append(float(row[4]))
    except:
        print("The file does not exist")
        sys.exit(1)
    
    return data

def calculate_percentile(data, k):
    if k < 0 or k > 1:
        print("p not in range [0,1]")
        sys.exit(1)
    else:
        # Sort data ascending
        data.sort()

        if k == 1:
            return data[-1]
        elif k == 0:
            return data[0]
        
        # Calculate n
        n = len(data)
        # Calculate i
        i = n * k
        
        if i.is_integer():
            pos = (i+i+1)/2
            pos_rdown = int(pos)
            pos_rup = int(pos) + 1
            pk = (data[pos_rdown - 1] + data[pos_rup - 1])/2
        else:
            pos = int(i) + 1
            pk = data[pos - 1]

    return pk

def parse_args():

    if len(sys.argv) != 5:
        raise Exception()

    filepath = ''
    k = 0

    if sys.argv[1] == '-f':
        filepath = sys.argv[2]
        if sys.argv[3] == '-p':
            k = sys.argv[4]
        else:
            raise Exception()
    elif sys.argv[1] == '-p':
        k = sys.argv[2]
        if sys.argv[3] == '-f':
            filepath = sys.argv[4]
        else:
            raise Exception()
    else:
        raise Exception()

    return filepath, float(k)


def main():

    try:
        parse_args()
    except:
        print("Usage: python percentile_calculator.py -f <filepath> -p <percentile>")
        sys.exit(1)
    
    
    filepath, k = parse_args()

    data = read_data(filepath)
    pk = calculate_percentile(data, k)
    print("Pk = " + str(pk))

if __name__ == '__main__':
    main()



#/Users/raquelblanco/Downloads/yellow_tripdata_2022-01.csv

