import math,random
# calculate distance between two points
def distance(a, b):
    sum_ = 0    # avoid duplicate
    for i in range(len(a)):
        sum_ += (a[i] - b[i])**2
    return math.sqrt(sum_)


# brute force algorithm, with time complexity O(N^2)
def brute_force(points):
    N = len(points)
    if N < 2:
        return float('inf')     # error case
    else:
        dm = distance(points[0], points[1])
        pairm = (points[0], points[1])
        for i in range(N-1):
            for j in range(i+1, N):
                new_distance = distance(points[i], points[j])
                if new_distance < dm:
                    dm = new_distance
                    pairm = (points[i], points[j])
        return dm, pairm

if __name__ == '__main__':
    testlist = list()
    for i in range(10):
        testlist.append((random.randrange(10),random.randrange(10),random.randrange(10)))
    print(testlist)
    print(brute_force(testlist))