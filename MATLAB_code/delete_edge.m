function [ A_new ] = delete_edge( A, source, to )
%DELETE_EDGE Summary of this function goes here
%   Detailed explanation goes here
N=size(A,1);
A_new=A;
ls_of_adj=[];

for i=1:N
    if(A(source,i)~=0)
        ls_of_adj=[ls_of_adj,i];
    end
end
l_del=A(source,to);
n=length(ls_of_adj);
for i=1:n
        tar=ls_of_adj(i);
        l=A(source,tar);
        if(tar~=to)
            A_new(source,tar)=1.0/(1.0/l+1.0/l_del/(n-1));
        end
end
A_new(source,to)=0;

end

