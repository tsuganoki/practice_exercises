"""n → n/2 (n is even)
n → 3n + 1 (n is odd)"""


def get_longest_seq(starting_num):

    longest_seq = 0
    ans = 0
    for i in range(starting_num,1,-1):
        seq = 0
        result = i
        print("i is: ", i)
        while result > 1:
            if result % 2 == 0:
                result = int(result/2)
            else:
                result = (3*result)+1
            seq +=1

        if seq > longest_seq:
                longest_seq = seq
                ans = i
                print(ans)
    return [ans,longest_seq]


print(get_longest_seq(1000000))
print("done")
