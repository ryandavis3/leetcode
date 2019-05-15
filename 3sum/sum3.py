def getTwoElementSums(arr):
    two_sums = dict()
    # Iterate over first of three elements
    for i, val1 in enumerate(arr):
        # Iterate over second of three elements
        for j, val2 in enumerate(arr[i+1:]):
            val = val1 + val2
            if val not in two_sums:
                two_sums[val] = list()
            two_sums[val].append(set([i, j+i+1]))
    return two_sums

def getThreeElementSums(arr, two_sums):
    triplets = list()
    for i, val in enumerate(arr):
        need = -val
        if need in two_sums:
            need_couples = two_sums[need]
            for couple in need_couples:
                if i not in couple:
                    triplet = couple.copy()
                    triplet.add(i)
                    triplets.append(frozenset(triplet))
    return triplets

def getTripletsValues(arr, triplets):

    trips = list()
    for triplet in triplets:
        trips.append([arr[i] for i in triplet])
    trips = [tuple(sorted(vals)) for vals in trips]
    trips = list(set(trips))
    trips = [list(vals) for vals in trips]
    return trips

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sums = getTwoElementSums(nums)
        three_sum = getThreeElementSums(nums, two_sums)
        three_vals = getTripletsValues(nums, three_sum)
        return three_vals
'''
