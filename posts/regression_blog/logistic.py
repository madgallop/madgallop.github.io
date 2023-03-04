import numpy as np
from numpy import random

class LogisticRegression: 
    def __init__(self, w = None, loss_history = None, score_history = None, prev_loss = None, prev_loss_stochastic = None):
        self.w = np.zeros(3) #vector of weights, including the bias term (b intercept)
        self.loss_history = [] #list of the evolution of the loss over the training period
        self.score_history = [] #list of the evolution of the score over the training period
        self.prev_loss = np.inf #good way to start off loss
        self.prev_loss_stochastic = np.inf 
        
    def pad(self, X): 
        #return X padded with a column of 1s 
        return np.append(X, np.ones((X.shape[0], 1)), 1) 
    
    def predict(self, X): #makes a prediction on all the training data at once. 
        #from lecture on Convex Linear Models and Logistic Regression
        return np.dot(X,self.w) #returns predicted label 
    
    def fit(self, X, y, alpha = None, max_epochs = None):
        '''
        fit(X,y) is the primary method of my logistic regression implementation. it takes in X, a features matrix of n observations (rows), and p features (cols) as well as y, a target vector of labels for each observation, performing gradient descent 
        there is no return value, but after the function is called, LR will have an instance vector w of weights (including the bias term b) a list loss_history (evolution of loss over the training period), and score_history (evolution of accuracy over the training period). 
        '''
        y = y[:,np.newaxis] #restructure
        X_tilde = self.pad(X) #make 3 dimensional 
        self.w = np.random.randn(X_tilde.shape[1], 1) #this is a 3x1 vector 
        for step in range(max_epochs):
            gradient = ((self.sigmoid(X_tilde@self.w)-y)*X_tilde).mean(axis=0, keepdims = True).T #gradient is 3x1
            self.w = self.w-alpha*gradient
            new_loss = self.loss(X_tilde,y)
            self.loss_history.append(new_loss) #append loss to loss history list
            accuracy = self.score(X_tilde,y) 
            self.score_history.append(accuracy) #append accuracy to score history list 

            if np.isclose(new_loss, self.prev_loss): # break loop if diffrence in loss between 2 steps is small enough
                break
            else:
                self.prev_loss = new_loss
                
    def fit_stochastic(self, X, y, alpha = None, batch_size = None, m_epochs = None):
        '''
        fit_stochastic(X,y) implements stochastic gradient descent. the method picks a random subset of the data and computed the gradient of this "batch."  
        similarly, the method takes in X, a features matrix of n observations (rows), and p features (cols) as well as y, a target vector of labels for each observation. 
        there is no return value, but after the function is called, LR will have an instance vector w of weights and lists loss_history and score_history. 
        '''
        y = y[:,np.newaxis] #restructure
        X_tilde = self.pad(X) #make 3 dimensional 
        self.w = np.random.randn(X_tilde.shape[1], 1)
        n = X.shape[0]
        for j in np.arange(m_epochs):
            order = np.arange(n)
            np.random.shuffle(order)
            for batch in np.array_split(order, n // batch_size + 1):
                x_batch = X_tilde[batch,:]
                y_batch = y[batch]
                #print(self.w.shape,"wshape")
                gradient = ((self.sigmoid(x_batch@self.w)-y_batch)*x_batch).mean(axis=0, keepdims = True).T #without this, the gradient has shape 1. we want it to have shape 3. so we want to sum down the columns. axis = 0 does this.
                self.w = self.w-alpha*gradient
            new_loss = self.loss(x_batch,y_batch)
            self.loss_history.append(new_loss) #append to history list
            accuracy = self.score(X_tilde,y) 
            self.score_history.append(accuracy) #append accuracy to score history list 
              
    def sigmoid(self, z):
        #from lecture on Convex Linear Models and Logistic Regression
        return 1 / (1 + np.exp(-z)) #sigmoid function to assist with other methods 

    def loss(self, X, y): #return overall loss (empiraical risk) of the current weights on X and y 
        #from lecture on Convex Linear Models and Logistic Regression
        y_hat = self.predict(X)
        loss = (-y*np.log(self.sigmoid(y_hat)) - (1-y)*np.log(1-self.sigmoid(y_hat))).mean() #logisitic loss
        return loss #empirical risk of current weights on X,y
                
    def score(self, X, y): 
        if X.shape[1] != len(self.w): #allows user to ask for score independent of fit function. 
            X = self.pad(X)
        y_hat = self.predict(X)
        y = y[:,np.newaxis] #restructure
        y_tilde = 1*(y_hat>0)
        accuracy = (y_tilde==y).mean() #how often, on average, predicted label equals true label
        self.score_history.append(accuracy)
        return accuracy