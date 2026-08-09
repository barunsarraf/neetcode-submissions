class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]


        for i in range(len(matrix)):
            current_position = i
            j=0
            k = len(matrix[0])-1

            while j<k:
                print(current_position,j,k)
                matrix[current_position][j],matrix[current_position][k]=matrix[current_position][k],matrix[current_position][j]
                j+=1
                k-=1
            
