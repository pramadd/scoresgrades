# Pick a random number between 60 and 100 and grade the score
#print x
import random
for x in range(10):
    score = random.randint(60,100)
    print score
    if score>90 :
        print "Score : {} ; Grade - A".format(score)
    elif score>80 :
        print "Score : {} ; Grade - B".format(score)
    elif score>70:
        print "Score : {} ; Grade - C".format(score)   
    elif score>60:
        print "Score : {} ; Grade - D".format(score)
