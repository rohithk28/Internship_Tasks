import solutions

sentence = input("Enter the sentence: ")
word = input("Enter a word: ")
print(solutions.freq_each_word(sentence))
print(solutions.freq_each_char(word))

print(solutions.anagram('hello','world'))

print(solutions.move_all_zeroes([0,3,0,1,2,0,4]))
print(solutions.second_highest([10,20,40,30,40,20]))
print(solutions.remove_dupli([4,2,4,5,2,7,5]))
print(solutions.missing_num([1,2,4,5]))
print(solutions.two_num([2,7,11,15],9))
print(solutions.num_close_zero([-8,-3,2,5,-2]))
print(solutions.common_ele([1,2,3,4,5],[3,4,5,6,7]))
print(solutions.rotate_list([1,2,3,4,5],2))
print(solutions.maxi_sum([4,7,2,9,5]))
print(solutions.sum_equals_target([2,4,3,5,7,8,1],9))