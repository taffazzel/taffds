from taffds import ds
import sys
'''ds.add_element_list_end([1,2,3,4],6)'''

def list_test(value,list1=None):
    '''print("address:", id(list1))
    print("before size of list:",sys.getsizeof(list1))
    list1.append(value)
    print("updated list:", list1)
    print("address remains the same:", id(list1))
    print("after sizes of list:", sys.getsizeof(list1))'''

def list_test2(list1):
    return list1.append(6)


if __name__=='__main__':
    '''for item in [5,6,7,8,"yhah"]:
    list_test(5,[4,6])
    list_test(88)
    list_test(68)'''
    list1=[1,2,3]
    print(list1)
    list_test2(list1)
    print(list1)