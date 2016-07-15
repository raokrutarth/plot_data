import matplotlib.pyplot as pyplot

def testplot():
    x = [1,2,3]
    y = [1,2,3]
    names = ['abc', 'def', 'ghi']
    pyplot.bar(x,y,width = 0.5, color = 'blue', align = 'center')
    pyplot.xticks(x,names)
    pyplot.show()
testplot()
    
