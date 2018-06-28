n= input("Enter a list of numbers separated by commas") # cue the user to input his or her choice of numbers
n= n.split(',') # retuns a list of substrings broken up at the commas
n= list(map(int,n)) #convert list of numbers into floats
print(min(n)) #finds the smallest number in the list
print(max(n)) #finds the largest number in the list
print(int(sum(n)/len(n))) #finds the mean/average of the numbers in the list
