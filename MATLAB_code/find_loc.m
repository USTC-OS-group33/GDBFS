function [ rank ] = find_loc( X, tar )
%FIND_LOC Summary of this function goes here
%   Detailed explanation goes here

% ??X?????????tar????
N=size(X,1);
if(N==0)
    rank=0;
else
    
    i=find(X(:,1)==tar);
    if(size(i,1)==0)
        rank=0;
    else
        rank=1;
        for j=1:N
            if(X(j,2)>X(i,2))
                rank=rank+1;
            end
        end
    end
end
end

