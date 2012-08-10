import subprocess
from subprocess import Popen, PIPE
def test(file2, input1, expout):
    cmd = ['python', file2]
    p1 = Popen(cmd, stdin=PIPE, stdout=PIPE)
    (so, se) = p1.communicate(input=input1)
    if expout in so:
        return True
    else:
        return False
def tester(file1):
    t1 = test(file1, "3", "Prime")
    t2 = test(file1, "10", "Composite")
    t3 = test(file1, "127", "Prime")
    if t1 == True & t2 == True & t3 == True:
        return True
    else:
        return False