function [ A_new ] = trim( A, source ,MAX_LENGTH, D)
%TRIM Summary of this function goes here
%   Detailed explanation goes here

N=size(A,1);
A_new=A;
ls_of_adj=[];

for i=1:N
    if(A(source,i)~=0)
        ls_of_adj=[ls_of_adj,i];
    end
end
for i=1:length(ls_of_adj)
                tar=ls_of_adj(i);
                l=A_new(source,tar);
                if(l>MAX_LENGTH)
                    if(D(source,tar))
                        A_new=delete_edge(A_new,source,tar);
                    end
                end
end
end

