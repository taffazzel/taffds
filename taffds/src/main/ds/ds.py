'''https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/'''

from array import *
import collections
import itertools

class datastructure:
    def fun_topk(self,list1,limit)->list:
        frequency={}
        for item in list1:
            if item in frequency:
                frequency[item]+=1
            else:
                frequency[item]=1
        return sorted(frequency.items(),key=lambda x:x[1],reverse=True)[0:limit]

    def find_highest_lowest(self,list_to_check):
        sorted_list = sorted(list_to_check,key=lambda x:x,reverse=True)
        return sorted_list[0],sorted_list[-1]

    def reverse_array(self,array_object):
        reveresed_array1 = array_object[::-1]
        list_a = list(reveresed_array1)
        return list_a

    def find_kth_largest_smallest(self,list_of_number,k):
        return sorted(list_of_number,key=lambda x:x,reverse=True)[k],sorted(list_of_number, key=lambda x: x, reverse=False)[k]

    def freq_counter1(self,list_of_number):
        freq={}
        for item in list_of_number:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
        return freq

    def freq_counter2(self,list_of_number):
        return dict(collections.Counter(list_of_number))

    def find_Subarray_with_given_sum(self,list_of_number,given_number):
        number_target_list=[]
        '''a = list(map(lambda x:x*2,list_of_number))'''
        number_target_list=[item for item in list_of_number if item > given_number]
        for num in number_target_list:
            if given_number>num:
                number_target_list.append(num)

    def nested_list_comprehension_and_remove_sublist(self,a,b,list_to_substract):
        return [[(i,j) for j in b if (i,j) not in list_to_substract] for i in a]

    '''
    "AABBBCCCD"-> "A2B3C3D1"
    "ABCDE"-> "A1B1C1D1E1",
    "AABBBCCCDAABB"-> "A2B3C3D1A2B2",
    "KKKKK"-> "K5"

    '''
    def compression(self, list_to_compress):
        list_cpmpressed = list()
        [list_cpmpressed.append(k+str(len(list(v)))) for k, v in itertools.groupby(list(list_to_compress))]
        return "".join(list_cpmpressed)

if __name__=='__main__':
    list1 = [1, 2, 3, 4, 1, 3, 5, 2, 3, 5, 6, 1, 2, 3, 5, 5, 2]
    list2 = [5,7,1,0,8,2,3,10,11]
    limit = 3
    '''print(datastructure().find_Subarray_with_given_sum(list2,6))'''
    '''returned_list = datastructure().fun_topk(list1,limit)
    array_object = array('i', [17, 6, 20])
    reveresed_array = datastructure().reverse_array(array_object)
    print(reveresed_array)
    print(datastructure().find_highest_lowest(list1))
    print(datastructure().find_kth_largest_smallest(list2,3))'''
    '''
    multi tenancy cluster
    how the cluster gets chocked and why?
    alternative to if else
    filter vs where comparison
    how can we avoid collecting to driver when only one socket is there to write lets say pgsql. can multiple executor write to the same at the same time
    windowing function
    lambda map
    join strategy and types
    udf
    '''
    print(datastructure().compression("AABBBCCCDAABB"))