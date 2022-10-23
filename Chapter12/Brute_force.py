import timeit as tmt

def brute_force(text, pattern):
    l1 = len(text)      # The text which is to be checked for the existence of the pattern
    l2 = len(pattern)   # The pattern to be determined in the text
    i= 0
    j=0          
 # looping variables are set to 0

    flag = False        # If the pattern doesn't appear at all, then set this to false and execute the last if statement
    while i < l1:       # iterating from the 0th index of text
        j = 0
        count = 0       # Count stores the length upto which the pattern and the text have matched
        while j < l2:
            if i+j<l1 and text[i+j] == pattern[j]:  # statement to check if a match has occoured or not
                count += 1                          # if the statement evaluates to true, then update count
            j += 1
        if count == l2:                             # if total number of successful matches is equal to count of the array  # print the starting index of the successful match
            flag = True                             # Even if the matching occours once, set this flag to True
            break
        i += 1
    if not flag:                                    # If the pattern doesn't occours even once, this statement gets executed
        return

#brute_force('acbcabccababcaacbcaabacbbc','cabcca')       
def brute_time():
    setup_bin = '''
from __main__ import brute_force
    '''
    test_bin = '''
line ='acbcabccababcaacbcaabacbbc'
check = 'cabcca'
brute_force(line,check)    
    '''
    times = tmt.repeat(setup = setup_bin,stmt = test_bin,repeat=10,number=10000)
    print('brute_time: {}'.format(min(times)))

if __name__ == '__main__':
    brute_time()