revisions = [0,3,'*',9]
minors = [3,6,'*',8]
majors = [3,4,5]

installed = '4.6.3'

total = 0
for mj in majors:
    for mn in minors:
        for r in revisions:
            print (mj,mn,r)
            total += 1

print total
