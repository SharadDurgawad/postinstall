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

def removeEntry(rpmString):
    "This function removes the structure containing the RPM name"

# iterate over the file and as soon as you see 'rpm' in a line(say, index of the line is i),
# then add a set of numbers from i-1 to i+15 to a set

    rpms = [x.strip() for x in rpmString.split(',')]

    # Declare a empty set
    se = set()

    # Loop into each rpm package
    for rpm in rpms:
        #print("\n rpm = %s" %rpm)

        f = open('TS.txt')

        for i,x in enumerate(f):
            if rpm in x:
                se.update(range(i-1,i+15))
    f.close()

    # print("\n se = %s" %se)

    # Now iterate over the file again and skip those indexes that are present in that set
    f = open('TS.txt')
    f1 = open('out.txt', 'w+')
    # write to the out.txt file all the entries from TS.txt file excluding the
    # the entries corresponding to indices in se set
    for i,x in enumerate(f):
        if i not in se:
            f1.write(x)
    f.close()
    f1.close()

#rpmString = raw_input("Enter the RPM to apply to TS.xml: ")
#print("\n %s" %removeEntry.__doc__)


# Function call to removeEntry function
#removeEntry(rpmString)

