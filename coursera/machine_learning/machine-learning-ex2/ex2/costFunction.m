function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

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
% Note: grad should have the same dimensions as theta
%
% =================== For-loop implementation ====================
##
##% Cost Function loop.
##a_sum = 0;
##for i=1:m
##  h = sigmoid(X(i,:) * theta);
##  a_sum += -y(i)*log(h)-(1-y(i))*log(1-h);
##endfor
##J = a_sum/m;
##
##% Gradient loop.
##n = length(theta);
##for j=1:n  
##  a_sum = 0;
##  
##  for i = 1:m
##    h = sigmoid(X(i,:)*theta);
##    a_sum += (h - y(i)) * X(i,j);
##  endfor
##  
##  grad(j) = a_sum/m;
##endfor

% ======== Vectorization Implementation (no loops). ============

% Cost Function Vectorization.
hy = sigmoid(X* theta);
J = -(y' * log(hy) + (1 - y')*log(1 - hy)) / m;

% Gradient Vectorization.
gradient = X' * (hy - y)/m;

% =============================================================

end
