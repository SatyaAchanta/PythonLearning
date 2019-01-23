import math

#  Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
def computepay(hours, rate):
    actualPay = 0.0;
    if (hours > 40):
        actualPay = (40 * rate) + ( hours - 40) * 1.5 * rate
    else:
        actualPay = (40 * rate)
    return actualPay

print(computepay(45, 10))

# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
def computegrade(score):
    actualGrade = 'F'
    try:
        if score >= 10.0:
            actualGrade = 'Bad score'
        elif score >= 0.9:
            actualGrade = 'A'
        elif score >= 0.8:
            actualGrade = 'B'
        elif score >= 0.7:
            actualGrade = 'C'
        elif score >= 0.6:
            actualGrade = 'D'
        else:
            actualGrade = 'F'
    except Exception as e:
        actualGrade = 'Bad score'

    return actualGrade

print(computegrade(0.75))
