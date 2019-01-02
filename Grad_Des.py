import math
def Gradient_Descent(initial_learning_rate, x1 ,x2, threshold_value ):

    """
    Finding the minimum the value of the function 1.5x^2 + x2^2 - 2x1x2 + 2x1^3+ 0.5x1^4
    using gradient_descent
    """
    max_no_of_iterations = 10000
    min_no_of_iterations = 500

    iteration = 0
    while(1):
        iteration += 1
        x1_derivative,x2_derivative = CalculateGradientDescent(x1,x2)
        x1_prev = x1
        x2_prev = x2
        x1 = x1 - (initial_learning_rate * x1_derivative)
        x2 = x2 - (initial_learning_rate * x2_derivative)
        f = CalculateFofX(x1,x2)
        print(" %f %f %f %f %f \n" % (x1, x2,f,x1_derivative,x2_derivative))
        if iteration <= min_no_of_iterations:
            continue
        if iteration >= max_no_of_iterations:
            break
        # stop condition 
        if (((x1_derivative ** 2) + (x2_derivative ** 2)) ** 0.5) <= threshold_value:
            break
    return x1,x2,f

def CalculateFofX(x1,x2):
    # find the value of the function with new x1 and x2
    return (1.5*(x1**2))+(x2**2)-(2*x1*x2)+2*(x1**3)+(0.5*(x1**4))


def CalculateGradientDescent(x1,x2):
    # calculate the partial derivatives w.r.t x1 and x2
    x1derivative = (3*x1) -(2*x2)+ (6*(x1**2)) + (2*(x1**3))
    x2derivative = 2*(x2 - x1)
    return [x1derivative,x2derivative]

if __name__ == '__main__':
    learning_rates =  [0.00004, 0.0001, 0.003, 0.04, 0.1]
    #0.00004, 0.0001, 0.003, 0.04,
    x1 = 1
    x2 = -3
    threshold_value = 0.001
    x1_min_arr =[]
    x2_min_arr = []
    f_min_arr = []
    for rate in learning_rates:
        print("learning rate === %f \n" % (rate))
        x1_min,x2_min,f = Gradient_Descent(rate,x1,x2,threshold_value)
        x1_min_arr.append(x1_min)
        x2_min_arr.append(x2_min)
        f_min_arr.append(f)
    for i in range(0,len(learning_rates)):
        print("Learning Rate = %f x1=%f x2=%f f=%f" % (learning_rates[i],x1_min_arr[i],x2_min_arr[i],f_min_arr[i]))
