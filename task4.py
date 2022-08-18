


def cube(number):
    return number**3


def factorial(num):
    factorial = 1
    for i in range(1 , num + 1):
        factorial *= i
    return factorial
    

def count_pattern(pattern, lst):
    lenP = len(pattern)
    #print("lenP",lenP)
    lenL = len(lst)
    #print("lenL",lenL)
    total = 0
    if(lenL >= lenP):
        for i in range(0, lenL):
            #print("repetition #:"+str(i))
            match = False
            if(pattern[0]==lst[i]):
                #print("-"+pattern[0]+"- matches in position "+str(i))
                #print(str(lenP+i-1))
                if((lenP+i-1)<lenL):
                    #print("inside the if statement lol")
                    for j in range(0,lenP):
                        #print("inside the for lol")
                        if(pattern[j]==lst[j+i]):
                            #print("inside the second if lol")
                            if(j == (lenP-1)):
                                match = True
                            continue
                        else:
                            break
            if(match==True):
                total +=1
    else:
        total = 0
    return total
    
# program For table
# num = 12
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)


# number_1 = int(input('Please enter the first number: '))
# operation = input('Please enter the operation: ')
# number_2 = int(input('Please enter the second number: '))

# if operation == '+':
#     print('{} + {} = '.format(number_1, number_2))
#     print(number_1 + number_2)

# elif operation == '-':
#     print('{} - {} = '.format(number_1, number_2))
#     print(number_1 - number_2)

# elif operation == '*':
#     print('{} * {} = '.format(number_1, number_2))
#     print(number_1 * number_2)

# elif operation == '/':
#     print('{} / {} = '.format(number_1, number_2))
#     print(number_1 / number_2)

# else:
#     print('You have not typed a valid operator, please run the program again.')
    

sentence = input("Enter a english sentence: ")

words = sentence.split()
words.sort()

newSentence = ""
for x in words:
    newSentence += x + " "
    
print(newSentence)


# print(cube(3))
# print(factorial(5))

# print(count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')))

