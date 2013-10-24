#Copyright (c) 2013 Akrita Agarwal
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import sys
from copy import deepcopy

def readfile(filename):
    matrix = []
    text_file = open(filename, "r")
    lines = text_file.readlines()
    for l in lines:
        row = [l[i:i+1] for i in range(0, len(l), 1)]
        for r in row:
            if r == "\n":
                row = row[0:-1]
        matrix.append(row)

    return matrix

def blankstates(matrix):
    blank = []
    length = len(matrix)
    for i in range(0,length):
        for j in range(0,length):
            if(matrix[i][j] == '.'):
                temp = [i,j]
                blank.append(temp)
    return blank

def checkrowcol(b,matrix):
    row = b[0]
    inrow = []
    blankrow = matrix[row][:]
    val = [i+1 for i in range(0,9)]
    inrow = val
    for bl in blankrow:
        for v in inrow:
            if(str(v) == bl):
                inrow.remove(v)
    col = b[1]
    for row in range(0,9):
        h = matrix[row][col]
        for i in inrow:
            if str(i)==h:
                inrow.remove(i)
    return inrow

def makebox(row,col):
    b = []
    for r in row:
        for c in col:
            t = [r,c]
            b.append(t)
    return b
    
def getboxes(i,matrix):
    row = [[0,1,2],[3,4,5],[6,7,8]]
    col = [[0,1,2],[3,4,5],[6,7,8]]
    if i in row[0]:
        r = row[0]
        c = col[i]
    elif i in row[1]:
        r = row[1]
        c = col[i-3]
    elif i in row[2]:
        r = row[2]
        c = col[i-6]
    mb = makebox(r,c)
    return mb

box = dict()
def checkbox(b,matrix,inrowcol):
    blankrow = []
    for bo in box:
        if b in box[bo]:
            for col in box[bo]:
                r = col[0]
                c = col[1]
                blankrow.append(matrix[r][c])
            break
    for bl in blankrow:
        for i in inrowcol:
            if (str(i)==bl):
                inrowcol.remove(i)
    return inrowcol
        
def check(b,matrix):
    inrowcol = checkrowcol(b,matrix)
    inrowcol = checkbox(b,matrix,inrowcol)
    return inrowcol

def solver(matrix,blank,level):
 if (matrix!= 'not a solution'):
   satisfy = 0
   if(len(blank)>0):
       for b in blank:
           valids = check(b,matrix)
           if (len(valids) == 1):
               satisfy = 1
               r = int(b[0])
               c = int(b[1])
               matrix[r][c] = str(int(valids[0]))
           elif (len(valids)== 0):
               return 'not a solution'
       if satisfy==0:
           b = blankstates(matrix)
           values = check(b[0],matrix)
           for v in values:
               if v in check(b[0],matrix):
                r = b[0][0]
                c = b[0][1]
                matrix[r][c] = str(v)
                mat = solver(deepcopy(matrix),blankstates(matrix),level+1)
            
                if (mat!='not a solution'):
                   matrix = mat
                   b = blankstates(matrix)  
                   if (len(b)==0):
                       return matrix
                   
       
   b = blankstates(matrix)
  # print('len:',b)
   if (len(b)==0):
       return matrix
   else:
       return solver(matrix,blankstates(matrix),level)    
    
def main(arg):
   # mat = readfile(arg)
   matrix = readfile('state6-4sol.txt')
   blank = blankstates(matrix)

   for i in range(0,9):
            box[i] = getboxes(i,matrix)

   print('-----------')
   v = 0         
   for m in matrix:
       print(str(m[0])+str(m[1])+str(m[2])+'|'+str(m[3])+str(m[4])+str(m[5])+'|'+str(m[6])+str(m[7])+str(m[8]))
       v = v+1
       if (v==3):
               print('-----------')
               v = 0
       
   matrix = solver(matrix,blank,1)
   if (matrix == 'not a solution'):
       print('Solution not found!')
       print('Num Solutions: 0')
   else:
       print('Found Solution!')
       print('Num Solutions: 1')
       print('-----------')
       v = 0
       for m in matrix:
           a = int(m[0])*100+int(m[1])*10+int(m[2])
           b = int(m[3])*100+int(m[4])*10+int(m[5])
           c = int(m[6])*100+int(m[7])*10+int(m[8])
           print(str(a)+'|'+str(b)+'|'+str(c))
           v = v+1
           if (v==3):
               print('-----------')
               v = 0
    
if __name__ == "__main__": main(sys.argv)
    
