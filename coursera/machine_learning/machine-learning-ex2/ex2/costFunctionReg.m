function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% =================== For-loop implementation ====================
##
##% Cost Function loop.
##a_sum = 0;
##for i=1:m
##  h = sigmoid(X(i,:) * theta);
##  a_sum += -y(i)*log(h)-(1-y(i))*log(1-h);
##endfor
##
##reg_sum = sum(theta.^2) - theta(1)^2;
##J = a_sum/m + reg_sum * lambda / (2*m);
##
##% Gradient loop.
##
##% The bias term, which is the first theta variable is not regularized.
##a_sum = 0;
##
##for i = 1:m
##  h = sigmoid(X(i,:)*theta);
##  a_sum += (h - y(i)) * X(i,1);
##endfor
##    
##grad(1) = a_sum/m;
##
##% Rest of the terms 2 to j are regularized.
##n = length(theta);
##for j=2:n  
##  a_sum = 0;
## 
##  for i = 1:m
##    h = sigmoid(X(i,:)*theta);
##    a_sum += (h - y(i)) * X(i,j);
##  endfor
##   
##  a_sum += lambda * theta(j); 
##  grad(j) = a_sum/m;
##endfor

% ======== Vectorization Implementation (no loops). ============

% Cost Function Vectorization.
theta_for_reg = theta;
theta_for_reg(1) = 0;

hy = sigmoid(X* theta);

J = -(y' * log(hy) + (1 - y')*log(1 - hy)) / m + sum(sum(theta_for_reg.^2)) * lambda/(2*m);

% Gradient Vectorization.
grad = X' * (hy - y)/m + theta_for_reg * lambda/m;

% =============================================================

end
