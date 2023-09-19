import numpy as np
from numpy import random

class Perceptron: 
    def __init__(self, history = None, w = None):
        self.history = [] #will be a list of the evolution of accuracy over training period
        self.w = np.zeros(3) #zero array in 3 dimensions
        
    def fit(self, X, y, max_steps = None):
        self.w = np.random.rand(3) #initialize random weight vector 
        for step in range(max_steps):
            i = np.random.randint(0,100) #pick a random data point 
            X_tilde = np.append(X, np.ones((X.shape[0], 1)), 1) #make 3 dimensional 
            y_tilde = 2*(y)-1 #for -1 and 1s 
            self.w = self.w+(y_tilde[i]*(np.dot(self.w,X_tilde[i]))<0)*1*y_tilde[i]*X_tilde[i] #update function
            if self.score(X_tilde, y) == 1.0: #if a perfect score is achieved 
                break
                
    def predict(self, X): 
        return np.sign(X@self.w) #returns predicted label 

     
    def score(self, X, y): 
        if X.shape[1] != len(self.w): #allows user to ask for score independent of fit function. 
            X = np.append(X, np.ones((X.shape[0], 1)), 1)
        y_tilde = 2*(y)-1 #makes array of -1 and 1s 
        accuracy = (self.predict(X)==y_tilde).mean() #how often, on average, predicted label equals true label
        self.history.append(accuracy)
        return accuracy 
    