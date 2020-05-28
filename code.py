# --------------
# Smallest Palindrome
# Create a function called palindrome(num) that given a number 'num', finds the next smallest palindrome and returns it

# Note : A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar or the number 10201.


#Code starts here

def palindrome(num):
    num += 1
    while (str(num) != str(num)[::-1]):
        num += 1
    return num
    


print("Palindrome of (13456) is : - " , palindrome(13456))


print("Palindrome of (123) is : - " , palindrome(123))


print("Palindrome of (1331) is :- " , palindrome(1331))


#def palindrome(num):
#    num=num+1
#    num=str(num)
#    if num==num[::-1]:
#        return int(num)
#    else:
#        while num != num[::-1]:
#            num=int(num)+1
#            num=str(num)
#        return int(num)



# --------------
# Anagram Scramble
# Create a function called 'a_scramble(str_1, str_2)' that given the strings'str_1','str_2' returns True if a portion of 'str_1' characters can be scrambled to match 'str2', else return False

#Code starts here

def a_scramble(str_1, str_2):
    str_1, str_2 = str_1.lower(), str_2.lower()
    str_1_list = list(str_1)
    for i in range(len(str_2)):
        if(str_2[i] not in str_1_list):
            return False
        else:
            str_1_list.remove(str_2[i])
    return True


print(a_scramble("Tom Marvolo Riddle" , "Voldemort"))

print(a_scramble("pani puri" , "chat"))

print(a_scramble("INDIA" , "INDIANA"))

print(a_scramble("INDIA" , "INDIA"))

print(a_scramble("Tom Cruise" , "Cruise"))

print(a_scramble("Tom Cruise" , "cruise"))


# --------------
# Fibonacci Check
# Create a function called check_fib(num) that checks if the given number 'num' is part of the fibonacci sequence and returns True if it is, else False

#Code starts here


def check_fib(num):
    num_1, num_2 = 0, 1
    while(num_2 < num):
        sum = num_1 + num_2
        num_1 = num_2
        num_2 = sum
        if(num_2 == num):
            return True
    return False

print("fibonacci sequence of (145) is :- " , check_fib(145))

print("fibonacci sequence of (377) is :- " , check_fib(377))

print("fibonacci sequence of (505) is :- " , check_fib(505))

print("fibonacci sequence of (121) is :- " , check_fib(121))

print("fibonacci sequence of (808) is :- " , check_fib(808))





# --------------
# String Compression
# Write a function compress(word) that given a word word returns the string with it's letters and how many times they occur continously together.


#Code starts here


def compress(word):
    word=word.lower()
    newStr=word[0]+"1"
    for char in word[1:]:
        if newStr[-2]==char:
            newStr = newStr[:-1]+str(int(newStr[-1])+1)
        else:
            newStr=newStr+char+"1"
    return  newStr



print("compress form of a word (nitesh) is : - " , compress("nitesh"))

print("compress form of a word (xxcccdex) is : - " , compress("xxcccdex"))

print("compress form of a word (DATA SCIENCE) is : - " , compress("DATA SCIENCE"))

print("compress form of a word (Machine Learning) is : - " , compress("Machine Learning"))

print("compress form of a word (Compress) is : - " , compress("Compress"))






# --------------
# K-Distinct
# Write a function k_distinct(string,k) that given a string 'string' and number 'k', it checks whether the 'string' has 'k' distinct characters


#Code starts here


def k_distinct(string,k):
    string = string.lower()
    str_2=""
    for i in string:
        if i not in str_2:
            str_2=str_2+i
    return k==len(str_2)


print("k_distinct of ('Messoptamia',8) is :- " , k_distinct('Messoptamia',8))

print("k_distinct of ('apple',5) is :- " , k_distinct('apple',5))

print("k_distinct of ('Missisipe',5) is :- " , k_distinct('Missisipe',5))

print("k_distinct of ('Tenanace',6) is :- " , k_distinct('Tenanace',6))

print("k_distinct of ('Tolorado',6) is :- " , k_distinct('Tolorado',6))





