function [ X ] = voting( X1,X2,sigma1,sigma2 )
%VOTING Summary of this function goes here
%   Detailed explanation goes here
X=X1;
N1=size(X1,1);
N2=size(X2,1);
for i=1:N1
    flag=1;
    for j=1:N2
        if(X(i,1)==X2(j,1))
            X(i,2)=X(i,2)*sigma1+X2(j,2)*sigma2;
            flag=0;
            break
        end
    end
    if(flag==1)
        X(i,2)=X(i,2)*sigma1;
    end
end

for j=1:N2
    flag=1;
    for i=1:N1
        if(X(i,1)==X2(j,1))
            flag=0;
            break
        end
    end
    if(flag==1)
        X=[X;[X2(j,1),X2(j,2)*sigma2]];
    end
end

end

