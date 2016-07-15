def readTarget(targetFile):
    # Read the file into list lines
    f = open(targetFile)
    lines = f.readlines()
    f.close()
    
    # This is a list of lists
    target = []
    
    # Parse the lines
    for i in range(len(lines)):
        # Split line on comma ','
        list = lines[i].split(",")
        city = list[0].strip('" \n')

        # Skip first line, it is the column name
        if i == 0:
                continue
        
        # Strip '$' symbol and newline character '\n'
        amount = list[1].strip('$" \n')
        
        entry = [city, float(amount)]
        
        # entry[0] is the city name
        # entry[1] is the target revenue
        target.append(entry)
        
    return target

def printTarget(target):
    print("")
    print("================= TARGET ==================")
    print("City".ljust(15) + "Target Revenue".ljust(15))
    
    total = 0
    for t in target:
        
        # t[0] is the city name
        # t[1] is the amount
        print(t[0].ljust(15) +  str("$%0.2f" %t[1]).ljust(53))
        total += t[1]
    
    print("")
    print("Turnover: " + "$%0.2f" % total)

def Main():
    target = readTarget("target.txt")
    printTarget(target)

if __name__ == '__main__':
    Main()
