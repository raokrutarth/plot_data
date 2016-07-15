from readRentals import *
from target import *

##Krutarth Rao

# Returns the revenues by city 
def revenueByCity(revenues, target):
    # Create a list of revenue by city 
    # The list contains lists for each rental  
    # with the fields city, target revenue, June ’14  ..
    # .. and performance 
    # Write your code here
    revByCity = []
    
    Bloomington_rev = 0
    Indianapolis_rev = 0
    FortWayne_rev = 0
    Lafayette_rev = 0
    TerreHaute_rev = 0
    Kokomo_rev = 0
    Muncie_rev = 0
    Columbus_rev = 0

    for act_rev_entry in revenues:
        if act_rev_entry[4] == 'Bloomington':
            Bloomington_rev += act_rev_entry[5]
        elif act_rev_entry[4] =='Indianapolis':
            Indianapolis_rev +=act_rev_entry[5]
        elif act_rev_entry[4] =='Fort Wayne':
            FortWayne_rev +=act_rev_entry[5]
        elif act_rev_entry[4] =='Lafayette':
            Lafayette_rev +=act_rev_entry[5]
        elif act_rev_entry[4] =='Terre Haute':
            TerreHaute_rev +=act_rev_entry[5]
        elif act_rev_entry[4] =='Kokomo':
            Kokomo_rev +=act_rev_entry[5]
        elif act_rev_entry[4] =='Muncie':
            Muncie_rev += act_rev_entry[5]            
        elif act_rev_entry[4] =='Columbus':
            Columbus_rev +=act_rev_entry[5]
    
    for i in range(len(target)):
        city = target[i][0]
        target_rev = target[i][1]
        
        if city == 'Bloomington':
            june14 = Bloomington_rev
        elif city =='Indianapolis':
            june14 = Indianapolis_rev
        elif city == 'Fort Wayne':
            june14 = FortWayne_rev
        elif city == 'Lafayette':
            june14 = Lafayette_rev
        elif city == 'Terre Haute':
            june14 = TerreHaute_rev
        elif city == 'Kokomo':
            june14 = Kokomo_rev
        elif city == 'Muncie':
            june14 = Muncie_rev
        elif city == 'Columbus':
            june14 = Columbus_rev

        ind_city_rev = [city, target_rev, float(june14)]
        revByCity.append(ind_city_rev)   
    
    return revByCity;

def printRevenueByCity(revByCity):
    
    for ind_city in revByCity:
        june14 = ind_city[2]
        target_rev = ind_city[1]
        if june14 <= (target_rev -  177):
            performance = 'Poor'
        elif june14 >= (target_rev + 177):
            performance = 'Excellent'
        elif june14 <= (176+target_rev) or june14 >= (target_rev-176):
            performance = 'Satisfactory'
        ind_city.append(performance)

    print('')
    print('==================== REVENUE BY CITY =====================')
    print('City'.ljust(15) , 'Target Revenue'.ljust(15) ,
          'June \'14'.ljust(15), 'Performance'.ljust(15) )
    difference = 0
    for ind_city in revByCity:
        print(ind_city[0].ljust(15), str('$%0.2f'%ind_city[1]).ljust(15),
              str('$%0.2f'%ind_city[2]).ljust(15), ind_city[3].ljust(15))
        difference += (ind_city[1] - ind_city[2])
    print('')
    print('Difference (Target - June): ',str('$%0.2f'%difference))   

def Main():
    target = readTarget("target.txt")
    # printTarget(target)

    revenues = readRevenues("revenue.txt")
    # printRentals(revenues)

    revByCity = revenueByCity(revenues, target)
    
    printRevenueByCity(revByCity)
    
if __name__ == '__main__': Main()
