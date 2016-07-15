# Refer to the format of file revenue.txt shown above  
# 
# It returns a list of lists with: date, name, make, pymttype, charge  
##Krutarth Rao


def readRevenues(file):
     
     # Read file into list of lines 
     fl = open(file)
     complete_list = fl.readlines()
     fl.close
     # Split lines into fields     
     # For each list create a list/sublist
     # Add list to expense list.
     # It returns revenues in a list of lists with fields  
     # date,name,make,pymttype,charge,return revenues

     revenues_list = []
     for i in range(len(complete_list)):
          list_of_lines = complete_list[i].split(",")
          date = list_of_lines[0].strip('"\n')
          if i == 0:
               continue
          name = list_of_lines[1]
          make = list_of_lines[2]
          payment_method = list_of_lines[3]
          city = list_of_lines[4]
          charge = list_of_lines[5].strip('$"\n')

          individual_entry = [date, name, make, payment_method,
                              city, float(charge)]
          revenues_list.append(individual_entry)
     return revenues_list
          

def printRevenues(revenues): 
    # Print revenues
    print('')
    print("=================================== EXPENSES ==================================")
    print('Date'.ljust(13) + 'Name'.ljust(26) + 'Make'.ljust(11)
          + 'Payment type'.ljust(14) + 'City'.ljust(15) + 'Charge'.ljust(10) )
    total_rev = 0
    for ind_entry in revenues:
         print(ind_entry[0].ljust(12) , ind_entry[1].ljust(25),
               ind_entry[2].ljust(10), ind_entry[3].ljust(13),
               ind_entry[4].ljust(15), str('$%0.2f'%ind_entry[5]).ljust(10))
               
         total_rev += ind_entry[5]
    print('')
    print('')
    print('Actual Turnover: ' , '$%0.2f'%total_rev)
    
         
         
    

def Main():
    revenues = readRevenues("revenue.txt")
    printRevenues(revenues)
    
if __name__ == '__main__': Main()
