import matplotlib.pyplot as plt
import math

def value_generator(num_from, num_to):
    x_val = []
    y_val = []
    for x in range(num_from, num_to+1):
        try:
            res = 1 - (1/365**x)*(math.factorial(365)/math.factorial(365-x))
        except OverflowError:
            break
        else:    
            res = round(res, 4)

            x_val.append(x)
            y_val.append(res)
    
# if num_people > 124, the probability is approx. 1.0
    if num_to > 124:
        for i in range(125, num_to+1):
            x_val.append(i)
            y_val.append(1.0)
    #print(len(x_val), len(y_val))
    return x_val, y_val

x_test, y_test = value_generator(1, 125)

plt.ylabel('The probability')
plt.xlabel('The number of people')
plt.suptitle('Visualization for the probability of no one shares a birthday')
plt.plot(x_test, y_test)
   
