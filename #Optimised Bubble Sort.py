#Optimised Bubble Sort
import random
def BubbleSort(List):
    Comparison_counter = 0
    Swapped_counter = 0
    for i in range(len(List)):
        for j in range(len(List)-1-i):   #We can do -i, because we know that after each time the j loop ends, the highest number is at the end
            Comparison_counter+= 1
            
            if List[j] > List[j+1]:
                
                List[j] , List[j+1] = List[j+1] , List[j]
                Swapped_counter += 1
                
    print("[Comparsons Total]: ",Comparison_counter )
    print("[Swapped Total]:  ",Swapped_counter)
    return List

List = []
for i in range(10):
    List.append(random.randint(0,10))

print(BubbleSort(List))