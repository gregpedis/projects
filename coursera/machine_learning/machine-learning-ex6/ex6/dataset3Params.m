function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 0.01;
sigma = 0.01;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

C_values = [];
sigma_values = [];
min_error = 1e+100;  


while (C <= 30)
  C_values(end+1) = C;
  C *= 3;
endwhile

while (sigma <= 30)
  sigma_values(end+1) = sigma;
  sigma *= 3;
endwhile


 for i = 1:numel(C_values)
   for j = 1:numel(sigma_values)
        
    model = svmTrain(X, y, C_values(i), @(x1,x2) gaussianKernel(x1, x2, sigma_values(j)), 1e-3, 20);
    predictions = svmPredict(model,Xval);
    min_error_temp = mean(double(predictions ~= yval));
    
    if( min_error_temp < min_error )    
      min_error = min_error_temp;
      C = C_values(i);    
      sigma = sigma_values(j);  
    endif
    
   endfor    
 endfor
 

% =========================================================================

end
