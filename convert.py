import sys, csv, os.path, json

#Convert a CSV to JSON
def convert(fname):
    #Make sure it's a CSV file first
    if fname.endswith('.csv'):
        #Make sure it exists
        if os.path.isfile(fname):
            print('Converting', fname)
            dictionary = {}

            #Open the file
            with open(fname) as f:
                reader = csv.reader(f)
                keys = []

                #Read every line
                r = 0
                for row in reader:
                    #Save the keys if its the first row
                    if r == 0:
                        keys = row
                    else:
                        #Create a dictionary entry for the row
                        dictionary[row[0]] = {}

                        #Read every cell
                        for c in range(len(row)):
                            #Skip the first cell
                            if c == 0:
                                continue
                            else:
                                #Add the cell to the dictionary entry mapped to the right key
                                dictionary[row[0]][keys[c]] = row[c]
                    #Increase r to keep track of which row it is
                    r += 1

            #Get the filename without the extension
            name = fname.split('.')[0]

            #Save it as a JSON file
            file = open('{}.json'.format(name), 'w')
            file.write('{} = {}'.format(name.replace(' ', '_'), json.dumps(dictionary)))
            file.close()
            print('Done!')

        else:
            print(fname, 'does not exist!')
    else:
        print('Please provide a CSV file!')

if __name__ == '__main__':
    #Make sure there's at least one file to convert
    if len(sys.argv) < 2:
        print('Please provide a file to convert!')

    #Convert every file
    for i in range(len(sys.argv)):
        #Skip the first argument, because it's always convert.py
        if i == 0:
            continue

        #Convert it
        convert(sys.argv[i])