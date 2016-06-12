from copy import deepcopy

intial = [] 
final = []
class Cell():
    value = '_'
    taken = False
    arrValue = [] 
    
    def __init__ (self, val):
        if val != '_':
            self.value = val
            self.taken = True
            self.arrValue = [False, True, True, True, True, True, True, True, True, True]
        else:
            self.value = '_'
            self.arrValue = [False, True, True, True, True, True, True, True, True, True]
            

def prepareBoard():
    for i in range (9):
        for j in range (9):
            if final[i][j].value != '_':
                Mark_unMark(i, j, final[i][j].value, True)

def showResultsForward():

    for i in range(len(final)):
        row = []
        for j in range(len(final[i])):
            row.append(final[i][j].value)
        print(row)
    print('======================================')
                    
def showResultsBackTracking():
    for i in range(len(final)):
        print(final[i])
    print('======================================')

def takeInputFromFileForwardCheck():
    path = raw_input ("Enter the path of the input file : ")
    
    for line in open(path):
        row = []
        for i in range(len(line)):
          if line[i] == '[' or line[i] == ']' or line[i] == ',' or line[i] == ' ':
              continue
          elif line[i] == '\n':
            intial.append(row)
            final.append(row)
          else:
            cell = Cell(line[i])
            row.append(cell)
    
    intial.append(row)
    final.append(row)
                   
def takeInputFromFileBackTracking():
    path = raw_input ("Enter the path of the input file : ")
    
    for line in open(path):
        row = []
        for i in range(len(line)):
          if line[i] == '[' or line[i] == ']' or line[i] == ',' or line[i] == ' ':
              continue
          elif line[i] == '\n':
            intial.append(row)
            final.append(row)
          else:
            row.append(line[i])
    
    intial.append(row)
    final.append(row)
    
def Mark_unMark(x, y, val, mark):

    value = int(val)
    
    for i in range (9):
        if mark == True:
           final[x][i].arrValue[value] = False
           final[i][y].arrValue[value] = False
           
        else:
           final[x][i].arrValue[value] = True
           final[i][y].arrValue[value] = True
           
        
    for i in range ((x / 3) * 3, (x / 3) * 3 + 2 + 1):
        for j in range ((y / 3) * 3, (y / 3) * 3 + 2 + 1):
            if mark == True:
                final[i][j].arrValue[value] = False
            else:
                final[i][j].arrValue[value] = True 
                
def checkCell(x, y, value):
    
    val = chr(value + 48)
    # First search if the value is already in this row or column
    for i in range (9):
        if (val == final[x][i] and y!=i) or (val == final[i][y] and x!=i):
            return False;
        
    # Search its square
    for i in range (int(int(x / 3) * 3), int(int(x / 3) * 3) + 3):
        for j in range (int(int(y / 3) * 3), int(int(y / 3) * 3) + 3):
            if (final[i][j] == val) and (i!=x and j!=y):
                return False;
            
    return True;

def solveForward(x, y):
    
    if x > 8 or y > 8:
        return 0
    check = 1;
    # showResults()
    if final[x][y].value == '_': 
        for i in range (1, 10):
            check = check + 1   

            if final[x][y].arrValue[i] == False :
                continue

            temp = chr(i + 48)
            Mark_unMark(x, y, i, True)
            if temp > 0:
                final[x][y].value = temp;
                if x == 8 and y == 8:
                    return 1;
                elif x == 8 and solveForward(0, y + 1) == 1:
                    return 1;
                elif solveForward(x + 1, y) == 1:
                    return 1;
                
            Mark_unMark(x, y, i, False)
            
        
        if check >= 10:
            if final[x][y].value != intial[x][y].value:
                    final[x][y].value = '_'
                    Mark_unMark(x, y, i, False)
            return 0
            
        
    if x == 8 and y == 8:
        return 1
    elif x == 8 and solveForward(0, y + 1) == 1:
        return 1
    elif solveForward(x + 1, y) == 1:
        return 1
        
    return 0;

def solveBackTracking(x, y):
    
    
    if x == 9:
        return 1
    
    if final[x][y] == '_': 
        for i in range (1, 10): 
            if checkCell(x, y, i) == False:
                continue
            
            final[x][y] = chr(i+48)        
            if y == 8:
                if solveBackTracking(x + 1, 0):
                    return 1;
            elif solveBackTracking(x, y + 1) == 1:
                return 1;
            final[x][y] = '_'
            
        return 0     
        
  
    if y==8:
        if solveBackTracking(x + 1, 0) == 1:
            return 1;
    elif solveBackTracking(x, y + 1) == 1:
        return 1
        
    return 0;

def main():
    choice = input("Enter 1 for forward checking or 2 for backward checking : ")
    if choice == 1:
        takeInputFromFileForwardCheck()
        prepareBoard()
        solveForward(0, 0)
        showResultsForward()
       
    else:
        takeInputFromFileBackTracking()
        showResultsBackTracking()

        solveBackTracking(0, 0)
        showResultsBackTracking()

main()
