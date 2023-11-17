# bubble sort function


def bubble_sort(list1):
    """ 
        iterate through list and bubble sort so that the values are in order
    
        For i in range: Iterate through starting with the last value
        For J in range: iterate through stating with the second last value
        if: compare values
        temp: add to new list
        compare lists and return temp list - or ordered list

    """
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  