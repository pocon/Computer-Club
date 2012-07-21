'''

An Introduction to If Statements

if statements evaluate a boolean expression and if the expression is true, that block of code is executed

'''

a = 10

if a > 5:
    print "a is greater than 5"

else: # regardless of the result of a > 5, whether a is less than 5 or equal to, this code is run.
    print "a is not greater than 5"


# Note that above, one of the branches must run. It can't just be "skipped over" as the else catches anything. You don't need else:

if a == 11:
    print "a is 11"


# You can also use elif to try other statements:

if a > 10:
    print "a is greater than 10"

elif a == 10:
    print "a is 10"

elif a < 10:
    print "a is less than 10"

else:
    print "Something went seriously wrong... this should never be executed"

# Note that using elif is different to using multiple if statements. If you use multiple if statements, regardless of whether or not the first statement is correct, the second one will be executed. But, with elif, the first correct if statement is branched into and it ignores any other elif statements, regardless of whether they're correct or not.
