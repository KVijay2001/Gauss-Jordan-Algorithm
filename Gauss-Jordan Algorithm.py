
#By Kisothan Suthakaran
# DRAFT ALGORITHM
 
def gauss_jordan_three(matrix:list):

    for n in range(1,3):
        i=0
        old=tuple(matrix[n][:])
        for element2 in matrix[n]:
            ratio=old[0]/matrix[0][0]
            matrix[n][i]=(ratio*matrix[0][i])-element2
            i+=1
        
    i=0
    old=tuple(matrix[2][:])
    for element2 in matrix[2]:
        ratio=old[1]/matrix[1][1]
        matrix[2][i]=(ratio*matrix[1][i])-element2
        i+=1 



    for n in range(1,3):
        i=0
        old=tuple(matrix[0][:])
        for element2 in matrix[0]:
            ratio=matrix[n][n]/old[n]
            matrix[0][i]=(ratio*element2)-matrix[n][i]
            i+=1    
        
        
    i=0
    old=tuple(matrix[1][:])
    for element2 in matrix[1]:
        ratio=matrix[2][2]/old[2]
        matrix[1][i]=(ratio*element2)-matrix[2][i]
        i+=1    


    x=[]
    i=0
    for _ in range(3):
        x.append(round(matrix[i][3]/matrix[i][i],3))
        i+=1
    
    return(x)    


#FINAL SIMPLIFIED ALGORITHM
#FOLLOWING ALGORITHM WORKS FOR ANY SQUARE MATRICES


from tabulate import tabulate

def gauss_jordan_nxn(matrix:list):

    for k in range(len(matrix)-1): 
        for n in range(k+1,len(matrix)):      
            i=0
            old=tuple(matrix[n][:])
            for element2 in matrix[n]:
                ratio=old[k]/matrix[k][k]
                matrix[n][i]=round(((ratio*matrix[k][i])-element2),4)
                i+=1
            
    for k in range(1,len(matrix)): 
        for n in range(len(matrix)-k):
            i=0
            old=tuple(matrix[n])
            for element2 in matrix[n]:
                ratio=matrix[len(matrix)-k][len(matrix)-k]/old[abs(k-len(matrix))]
                matrix[n][i]=round(((ratio*element2)-matrix[abs(k-len(matrix))][i]),4)
                i+=1    
    x=[]
    i=0
    for _ in range(len(matrix)):
        x.append(round(matrix[i][len(matrix)]/matrix[i][i],3))
        i+=1
    return(x)    

#TEST

#matrix=[[1,-1,3,1,1],[0,1,7,1,5],[-4,4,1,-2,2],[2,1,0,1,3]]
#matrix=[[1,1,3],[3,-2,4]] 
matrix=[[2,3,13],[4,7,29]]

print(gauss_jordan_nxn(matrix))


















        



        