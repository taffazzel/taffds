import logging
def add_element_list_end(list_received,item_to_be_added):
    '''
    This function will return an item added to an existing python mutable list
    :param list_received:
    :return:
    '''
    print("List received for add",list_received)
    list_returned=list_received.append(item_to_be_added)
    return list_returned

def remove_element_list(list_received,item_to_be_removed):
    '''
    This function will return an item removed to an existing python mutable list
    :param list_received:
    :return:
    '''
    print("List received for remove", list_received)
    list_returned = list_received.remove(item_to_be_removed)
    return list_returned