function [ A_new ] = learn( A, source, to ,LEARNING_RATE)
%LEARN Summary of this function goes here
%   Detailed explanation goes here
N=size(A,1);
A_new=A;
ls_of_adj=[];

for i=1:N
    if(A(source,i)~=0)
        ls_of_adj=[ls_of_adj,i];
    end
end
    
    t=find(ls_of_adj==to);
    t=size(t);
    if t(2)~=0
            for i=1:length(ls_of_adj)
                tar=ls_of_adj(i);
                l=A(source,tar);
                if(tar == to)
                    l=1.0/(1.0/l-LEARNING_RATE*(1.0/l-1));

                else
                    l=1.0/(1.0/l-LEARNING_RATE/l);
                end
                A_new(source,tar)=l;
                
            end
    
    else
            delta=0;
            for i=1:length(ls_of_adj)
                tar=ls_of_adj(i);
                l=A(source,tar);
                delta=delta+LEARNING_RATE/l;
                l=1.0/(1.0/l-LEARNING_RATE/l);
                A_new(source,tar)=l;
            end
            l=1/delta;
            if(length(ls_of_adj)==0)
                l=1;
            end
            A_new(source,to)=l;
    end
    

end

