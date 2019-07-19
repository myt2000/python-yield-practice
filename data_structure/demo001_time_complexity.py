import time
# def condition_solution():
#     start_time = time.time()
#     for a in range(1001):
#         for b in range(1001):
#             for c in range(1001):
#                 if 1000 == a + b + c and a*a + b*b == c*c:
#                     print("a, b, c: %d, %d, %d" % (a, b, c))
#     end_time = time.time()
#     cost = end_time - start_time
#     print("cost: %f" % cost)

#  时间复杂度T(n) = 10 * n^3  = O(n^3)  大O表示法

def condition_solution():
    start_time = time.time()
    for a in range(1001):
        for b in range(1001):
                c = 1000 - a - b
                if 1000 == a + b + c and a*a + b*b == c*c:
                    print("a, b, c: %d, %d, %d" % (a, b, c))
    end_time = time.time()
    cost = end_time - start_time
    print("cost: %f" % cost)


#  T(n) = 时间复杂度 10 * n^2  = O(n^3)



if __name__ == "__main__":
    condition_solution()

