function [ node,p ] = cal_MM_P( A,source )
%CAL_MM_P Summary of this function goes here
%   Detailed explanation goes here
p=[];
node=[];
N=size(A,1);

for i=1:N
    if(A(source,i)~=0)
        node=[node;i];
        p=[p;1/A(source,i)];
    end
end


end

