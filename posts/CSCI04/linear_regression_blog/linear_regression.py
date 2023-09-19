import numpy as np
from numpy import random

class LinearRegression: 
    def __init__(self, w = None, score_history = None):
        self.w = None #random weight vector
        self.score_history = [] #list of the evolution of the score over the training period
        
    #pad
    def pad(self, X):
        #return X padded with a column of 1s 
        return np.append(X, np.ones((X.shape[0], 1)), 1)

    
    def fit_analytical(self, X, y): #analytic
        '''
        This fit method uses the analytical formula for the optimal weight vector w from the "Least-Squares Linear Regression" lecture notes. This formula requires matrix inversion and several matrix multiplications.
        '''
        self.w = np.random.rand(X.shape[1]) #random weight vector
        X = self.pad(X)
        w_hat = np.linalg.inv(X.T@X)@X.T@y
        self.w = w_hat
        return w_hat
    
                
    def fit_gradient(self, X, y, alpha = None, max_iter = None):
        '''
        This fit method uses the formula for the gradient of the loss function to implement gradient descent for linear regression.
        '''
        X = self.pad(X) #100x2
        self.w = np.random.randn(X.shape[1]) #2x_
        P = X.T@X #matrix multiplication #2x2---X.T is 2x100, X is 100x2
        q = X.T@y #matrix vector multiplication #2x_ --- y is 100x_
        done = False
        while not done:
            gradient = P@self.w - q #2x_
            self.w = self.w-alpha*gradient #2x_
            accuracy = self.score(X,y) 
            self.score_history.append(accuracy) #append accuracy to score history list  
            if np.allclose(gradient, np.zeros(len(gradient))) or iter == max_iter:        
                    done = True
                
                
    #predict
    def predict(self, X):
        if X.shape[1] != len(self.w): #allows user to ask for prediction independent of fit function. 
            X = self.pad(X)
        y_hat =  X@self.w #returns predicted label 
        return y_hat

    #score
    def score(self, X, y):
        '''
        Method to compute the coefficient of determination of the predictions.
        The coefficient is always smaller than 1, with a higher value indicating better predictive performance. It can be arbitrarily negative for very bad models. The numerator in the fraction is just the loss function, so a small loss makes the coefficient of determination large.
        '''
        if X.shape[1] != len(self.w): #allows user to ask for score independent of fit function. 
            X = self.pad(X)
        return 1-((((self.predict(X)-y)**2).sum())/(((y.mean()-y)**2).sum()))