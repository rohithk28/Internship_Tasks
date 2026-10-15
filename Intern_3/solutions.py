#Q1 :- Q1. Find the Frequency of Each Word in a Sentence
def freq_each_word(s):
    di = {}
    s = s.split()
    for word in s:
        di[word] = di.get(word,0)+1
    return di

#Q2:- Find the Frequency of Each Character in a Word
def freq_each_char(s):
    di={}
    for ch in s:
        di[ch] = di.get(ch,0)+1
    return di

#Q3. Find the First Non-Repeating Character in a Word
def first_non(s):
    di={}
    for ch in s:
        di[ch] = di.get(ch,0)+1
    for ch in s:
        if di[ch] == 1:
            return ch
    return None

#Q4. Check Whether Two Strings Are Anagrams
def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    di={}
    for ch in s1:
        di[ch]= di.get(ch,0)+1
    for ch in s2:
        if ch not in di:
            return False
        di[ch] -= 1
        
        if di[ch] == 0:
            del di[ch]
    return len(di) == 0

#Q5. Find the First Repeating Character in a String

def first_repeat(s):
    di={}
    for ch in s:
        di[ch] = di.get(ch,0)+1
    for ch in s:
        if di[ch] > 1:
            return ch
    return None

#Q6:- Move All Zeros to the End of a List

def move_all_zeroes(l):
    li = [0] * len(l)
    j = 0
    for i in range(len(l)):
        if l[i] != 0:
            li[j] = l[i]
            j += 1
    return li

#Q7 :- Find the Second Highest Distinct Number in a List

def second_highest(l):
    maxi = max(l)
    maxi1 = float('-inf')
    for num in l:
        if num != maxi and num > maxi1:
            maxi1 = num
    return maxi1

#Q8 : Remove Duplicates Without Changing the Original Order

def remove_dupli(l):
    li = []
    for num in l:
        if num not in li:
            li.append(num)
    return li  

#Q9 : Find the Missing Number from 1 to N

def missing_num(l):
    ans = 0
    for i in range(len(l) + 1):
        ans ^= i
    for num in l:
        ans ^= num
    return ans

#Q10: Find Two Numbers Whose Sum Equals a Target

def two_num(l,target):
    i = 0
    j = 1
    while i < j and j < len(l):
        if l[i] + l[j] == target:
            return l[i],l[j]
    return None

#Q11 :- Find the Number Closest to Zero

def num_close_zero(l):
    closest = l[0]
    for num in l:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num
    return closest 

#Q12. Find Common Elements Between Two Lists
def common_ele(l,l1):
    li = []
    for num in l:
        if num in l1 and num not in li:
            li.append(num)
    return li

#Q13. Rotate a List to the Right by K Positions

def rotate_list(l,k):
    k %= len(l)
    l.reverse()
    l[:k] = reversed(l[:k])
    l[k:] = reversed(l[k:])
    
    return l

#Q14. Find the Maximum Sum of Two Consecutive Elements
def maxi_sum(l):
    i = 0
    j = 1
    maxi = 0
    while i < j and j < len(l):
        summ = l[i] + l[j]
        if summ >maxi:
            maxi  = summ
        
        i += 1
        j += 1
    return maxi

#Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def sum_equals_target(l,target):
    li= []
    
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i] + l[j] == target:
                li.append([l[i],l[j]])
    return li