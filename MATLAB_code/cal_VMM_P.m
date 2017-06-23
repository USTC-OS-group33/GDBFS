function [ node ,p ] = cal_VMM_P( I, loc, total, total_state)
%CAL_VMM_P Summary of this function goes here
%   Detailed explanation goes here

N=size(I,1);
node=[];
p=[];
if(loc==0)
    total_t=total;
else
    total_t=I(loc,3);
end
for i=1:N
    if(I(i,1)==loc && I(i,4)==1)
        node=[node;I(i,2)];
        p=[p;(I(i,3)+total_state)/(total_t+total_state)];
    end
end

    
end

