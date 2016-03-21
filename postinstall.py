#-------------------------------------------------------------------------------
# Name:        postinstall
# Purpose:     This program removes the entries of given RPMs in TS.xml
#              and pre_TS.xml files
#
# Author:      sdurgawad
#
# Created:     21/03/2016
# Copyright:   (c) sdurgawad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Function to remove a RPM entry from TS.xml file

def removeEntry(str):
    "This function removes the structure containing the RPM name"

    print("\n The given string parameter is: %s \n" %str)

# iterate over the file and as soon as you see 'str' in a line(say, index of the line is i),
# then add a set of numbers from i-1 to i+15 to a set

    f = open('TS.txt')
    se = set()
    for i,x in enumerate(f):
        if str in x:
            se.update(range(i-1,i+15))
    f.close()

# Now iterate over the file again and skip those indexes that are present in that set

    f = open('TS.txt')
    f1 = open('out.txt', 'w')
    for i,x in enumerate(f):
        if i not in se:
            f1.write(x)
    f.close()
    f1.close()

rpmString = raw_input("Enter the RPM to apply to TS.xml: ")
print("\n %s" %removeEntry.__doc__)
removeEntry(rpmString)
