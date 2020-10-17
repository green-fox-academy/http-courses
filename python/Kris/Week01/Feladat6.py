
# def rotate_matrix( m ): return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#print (matrix[0][0])
def transzponal(matrix):      
    szeles=len(matrix[0])
    magas=len(matrix)    
    cm = [ [0]*3 for i in range(3)]
    for i in range(szeles-1,-1,-1):
        sor=""
        for j in range(0,magas,1):
            cm[i][j]=matrix[j][i]
            sor=sor+str(matrix[j][i])+" "            
        print(sor)
    return cm
#transzponal(matrix)
celmatrix=transzponal(matrix)
print(celmatrix)
