import numpy as np
import matplotlib.pyplot as plt
import math

grades = {"elmag": "A",
       "faststoff": "B",
       "matte 4": "A",
       "elsysprosjekt":"B",
       "datdig":"C",
       "fysikk":"C",
       "matte 3":"C",
       "esda2":"A",
       "c++":"C",
       "matte 2":"B",
       "statistikk":"E",
       "esda1":"A",
       "itgk":"A",
       "matte1":"A",
       "ade":"C"
}

scale = {"A": 5,
         "B": 4,
         "C": 3,
         "D": 2,
         "E": 1}


gpa = sum([scale[grades[subject]] for subject in grades])/len(grades)
print(gpa)