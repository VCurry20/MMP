# file with changes made - questions 1-5 


import csv

from Sorting import bubble_sort

def read_scores_from_csv(filename):
    """ 
        take in values from the csv file
    
        : open file as read mode
        : read data as dict save as fiew
        : iterate through and append the scores to a scores lines as intergers
        : return the scores


    """
    scores = []
    with open(filename, mode ='r') as file:   
        csvFile = csv.DictReader(file)
    
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)    
    return scores

def read_all_from_csv(filename):
    # https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
    """read entire file - here we set no header name as above """
    with open(filename, mode ='r') as file:  
        print(file.read()) 



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

def get_median_value(list):
    """ 
        Given a list of numbers as input this function will return the median average.
    
        :list1: make a copy of the list
        :bubble sort: bubble sort this copy
        :median: the number in the middle of the list - list divided by 2
        :return: median value
    """
    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]
    return median

def get_minimum_value(list):
    """
    get minimum value of list

    minimum is first value in list
    iterate through list evaluating if minimum is less than each value
    return minimum value
    """
    minimum = list[0]
    for l in list:
        if minimum < l:
            minimum = l

def get_maximum_value(list):
    """
    get maximum value of list 

    maximum is first value in list
    iterate through list evaluating if maximum is greater than each value
    return maximum value

    """
    maximum = list[0]
    for l in list:
        if maximum > l:
            maximum = l
    return maximum


    

    
def get_mode(list):
    """ 
        get the mode of a list - most frequent value
    
        : set highest freq variable
        : set mode variable - first score / value
        : iterate through all scores
        : iterate comparing scores
        : if function to find greatest frequency
        :return: mode
    """
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


def get_quartiles(nums):
    # https://www.educative.io/answers/basic-statistics-using-python
    # divide the data into 4 parts
    nums=sorted(nums)
    Q1 = get_median_value(nums[:len(nums)//2])
    Q2 = get_median_value(nums)
    if len(nums)%2 == 0:
        Q3 = get_median_value(nums[len(nums)//2:])
    else:
        Q3 = get_median_value(nums[len(nums)//2+1:])
    return Q1,Q2,Q3


def get_standardDeviation(a):
    # https://www.educative.io/answers/basic-statistics-using-python
    # spread of the data
    n = len(a)
    std=(sum(map(lambda x: (x-sum(a)/n)**2,a))/n )**0.5
    return std

    
if __name__ == "__main__":

    scores = read_scores_from_csv('example.csv')
    all = read_all_from_csv('example.csv')
    
    average = get_average(scores)
    minimum = get_minimum_value(scores)   
    maximum = get_maximum_value(scores)
    median = get_median_value(scores)
    mode = get_mode(scores)

    quartiles = get_quartiles(scores)
    standard_Dev = get_standardDeviation(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode} Quartiles: {quartiles} Standard deviation: {standard_Dev}')

    print("All CSV data", all )
    