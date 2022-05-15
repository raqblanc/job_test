import csv
import sys

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


def read_data(filepath):
    try:
        header = True
        data = []
        trip_distance = []
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if header: 
                    header = False
                else:
                    data.append(row)
                    trip_distance.append(float(row[4]))
    except:
        print("The file does not exist")
        sys.exit(1)
    
        return data, trip_distance

def calculate_percentile(data, k):
    if k < 0 or k > 1:
        print("p not in range [0,1]")
        sys.exit(1)
    else:
        # Sort data ascending
        sorted_data = sorted(enumerate(data), key=lambda i: i[1])
        # Calculate n
        n = len(sorted_data)
        # Calculate i
        i = n * k       

        if i.is_integer():
            pos = int((i+i+1)/2) + 1
        else:
            pos = int(i) + 1

        data_percentile = sorted_data[pos-1:]
    
    percentile_pos = [d[0] for d in data_percentile]
    return percentile_pos

def print_write_results(data, pos):
    percentile_data = [d for i, d in enumerate(data) if i in pos]
    
    print(percentile_data)

    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)        
        writer.writerows(percentile_data)

def main():

    try:
        parse_args()
    except:
        print("Usage: python percentile_calculator.py -f <filepath> -p <percentile>")
        sys.exit(1)
    
    
    filepath, k = parse_args()

    data, trip_distance = read_data(filepath)
    percentile_pos = calculate_percentile(trip_distance, k)
    print_write_results(data, percentile_pos)

if __name__ == '__main__':
    main()

