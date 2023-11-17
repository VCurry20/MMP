# question 6 - procedural program with import changes

import csv
import statistics

#def get_maximum_value(list):
#    maximum = list[0]
#    for l in list:
#        if maximum > l:
#            maximum = l
#    return maximum

#def get_minimum_value(list):
#    minimum = list[0]
#    for l in list:
#        if minimum < l:
#            minimum = l
            
def get_average(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.
    
        :param list: the list of numbers given as input
        :return: the numerical average of the list
    """
    total = 0
    for l in list:
        total += l
        
    average = total / len(list)
    return average

def get_average_2(list):
    # https://www.geeksforgeeks.org/find-average-list-python/
    return sum(list) / len(list) 



def get_median_value(list):
    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]
    return median


def median_2(list):
    res = statistics.median(list)
    return res
    
def bubble_sort(list1):
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    
def get_mode(list):
    highest_freq = 0
    mode = scores[0]
    for score in scores:
        frequency = 0
        for score2 in scores:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode

def read_scores_from_csv(filename):
    scores = []
    with open(filename, mode ='r') as file:   
        csvFile = csv.DictReader(file)
    
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)    
    return scores
    
if __name__ == "__main__":

    scores = read_scores_from_csv('example.csv')
    
    #average = get_average(scores)
    average = get_average_2(scores)
    #minimum = get_minimum_value(scores) 
    # https://www.tutorialspoint.com/python/list_min.htm  
    minimum = min(scores)
    #maximum = get_maximum_value(scores)
    # https://www.tutorialspoint.com/python/list_max.htm
    maximum = max(scores)
    median = get_median_value(scores)
    # https://www.geeksforgeeks.org/find-median-of-list-in-python/
    median2 = median_2(scores)
    mode = get_mode(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}')

    print (median2)
    