from copy import deepcopy

intial=[] 
final= []

class Cell():
    value='_'
    taken=False
    arrValue =[] 
    
    def __init__ (self,val):
        if val!='_':
            self.value=val
            self.taken=True
            self.arrValue=[False,True,True,True,True,True,True,True,True,True]
        else:
            self.value='_'
            self.arrValue=[False,True,True,True,True,True,True,True,True,True]
def takeInputFromFile():
    path = raw_input ("Enter the path of the input file : ")
    
    for line in open(path):
        row=[]
        for i in range(len(line)):
          if line[i] == '[' or line[i] == ']' or line[i] == ',' or line[i] == ' ':
              continue
          elif line[i]=='\n':
            intial.append(row)
            final.append(row)
          else:
            cell = Cell(line[i])
            row.append(cell)
    
    intial.append(row)
    final.append(row)

def Mark_unMark(x,y,val,mark):

    value = int(val)
    
    for i in range (9):
        if mark == True:
           final[x][i].arrValue[value]=False
           final[i][y].arrValue[value]=False
           
        else:
           final[x][i].arrValue[value]=True
           final[i][y].arrValue[value]=True
           
        
    for i in range ((x / 3) * 3,(x / 3) * 3 + 2+1):
        for j in range ((y / 3) * 3,(y / 3) * 3 + 2+1):
            if mark==True:
                final[i][j].arrValue[value]=False
            else:
                final[i][j].arrValue[value]=True 
                
def prepareBoard():
    for i in range (9):
        for j in range (9):
            if final[i][j].value!='_':
                Mark_unMark(i, j,final[i][j].value,True)

def showResults():

    for i in range(len(final)):
        row=[]
        for j in range(len(final[i])):
            row.append(final[i][j].value)
        print(row)
    print('======================================')



def main():
    takeInputFromFile()
    prepareBoard()
    solve(0, 0)
    showResults()

main()