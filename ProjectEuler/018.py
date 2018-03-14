
main_array =[
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

wrong_answers = [794, 992, ]

bb_array = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],

]


def condense_pyramid(array):
    level_sum = []
    for cur_level in array:
        print(level_sum)
        prev_level_sum = level_sum
        level_sum = []

        for j in range(len(cur_level)):

            if len(cur_level) == 1:
                level_sum = cur_level
                print(level_sum)
                break
            if j == 0:
                print("appending: ",prev_level_sum[0],"+",cur_level[j])
                level_sum.append(prev_level_sum[0]+cur_level[j])
            elif j < (len(cur_level)-1):
                print("Iamapotato",prev_level_sum[j])
                print("appending the higher of : ",cur_level[j])
                print(prev_level_sum[j],cur_level[j])
                print(" ")
                print(prev_level_sum[j-1], cur_level[j])
                level_sum.append(max(prev_level_sum[j]+cur_level[j],prev_level_sum[j-1]+cur_level[j]))
            else:
                print("appending(e): ")
                print(prev_level_sum[j-1])
                print("+")
                print(cur_level[j])
                level_sum.append(prev_level_sum[j-1]+cur_level[j])
            print(level_sum)
    return level_sum





"""

            if cur_level.index(j) == 0:
                print("Iamapotato",prev_level_sum[0],"+",cur_level[j])
                #level_sum.append(prev_level_sum[0]+array[i][j])
           try:

                level_sum.append(array[i][j]+(max(prev_level_sum[j-1],prev_level_sum[j])))

            except:
                level_sum.append("array[i][j]+")
            print("level_sum: ",level_sum)
        print("level_sum: ",level_sum)
    return level_sum

"""



def sum_path(array):
    totals = []
    total = 0
    level_index = 0
    path_taken = []
    all_paths = []
    n = 0
    while n < 20:
        steps = len(path_taken)


        for i in range(len(array)):
            try:
                #print("options are: ",array[i][level_index],array[i][level_index+1])
                if array[i][level_index] < array[i][level_index+1]:
                    print("winner: ",array[i][level_index+1])
                    winner = array[i][level_index+1]
                    level_index +=1
                    path_taken.append(i,level_index)
                else:
                    print("winner: ",array[i][level_index])
                    winner = array[i][level_index]
            except:
                winner = array[i][level_index]
            total += winner
            #print("Winner is: ",winner,".. Total is: ",total)

        all_paths.append(path_taken)
        n += 1



def run_it_three():
    return sum_path(main_array)

#print(sum_path(main_array))

#print(run_it_three())
print(condense_pyramid(main_array))
