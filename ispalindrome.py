# A palidrome isa word spelt ths same froward and backward
def ispalindrome(s):

    #create a variable that will become the answer
    ans = True

    #loop over the length of the string
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            ans = False
    return ans
# test from question
print(ispalindrome("radar"))
print(ispalindrome("radars"))
