#No ascending using function
def numsort(numsort_asscending):
    return sorted(numsort_asscending)

#String asccending using function
def strsort(strsort_asscending):
    return sorted(strsort_asscending)

#No descending using function
def numsort1(numsort_desscending):
    return sorted(numsort_desscending,reverse=True)

#string descending using function
def str_desc(strsort_desscending):
    return sorted(strsort_desscending,reverse=True)

nos=[2,3,5,23,7,43,5]
sorted_ans= numsort(nos)
print(sorted_ans)
sorted_ans1=numsort1(nos)
print(sorted_ans1)

strngs=['R','S','T','Y']
strng_ans1=strsort(strngs)
print(strng_ans1)
strng_ans2=str_desc(strngs)
print(strng_ans2)