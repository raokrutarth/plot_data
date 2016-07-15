#Krutarth Rao

from readRentals import *
from target import *
from revenueByCity import *
import matplotlib.pyplot as pyplot

def plotBarGraph(revByCity):
    target_pos = [2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20]
    june_pos =  [3.5, 6, 8.5, 11, 13.5, 16, 18.5, 21]
    label_pos = [3,5.5,8,10.5,13,15.5,18,20.5]

    
    target_rev_list = []
    june_rev_list = []
    city_list = []

    for i in range(len(revByCity)):
        target_rev_list.append(revByCity[i][1])
        june_rev_list.append(revByCity[i][2])
        city_list.append(revByCity[i][0])
    #print( target_rev_list, june_rev_list, city_list)       
    

    june_bar = pyplot.bar(target_pos, target_rev_list, width=1,
                          color = 'maroon', align = 'center')
    target_bar = pyplot.bar(june_pos, june_rev_list, width=1,
                            color='orange', align = 'center')
    pyplot.legend((june_bar, target_bar), ('Target Revenue', 'June Revenue'),
                  loc=9)
    pyplot.xticks(label_pos, city_list)

    pyplot.ylabel('US Dollar($)')
    pyplot.setp(pyplot.xticks()[1], rotation=45)
    pyplot.axis([0,25,0,16000])
    pyplot.show()
    
    
    
def Main():
    target = readTarget("target.txt")
    #printTarget(target)
    
    revenues = readRevenues("revenue.txt")
    #printRentals(revenues)
    
    revByCity = revenueByCity(revenues, target)
    #printRevenueByCity(revByCity)
    
    plotBarGraph(revByCity)

if __name__ == '__main__':
    Main()
