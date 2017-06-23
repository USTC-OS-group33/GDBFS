function [ I_new, loc_new ] = VMM( I, loc, to )
%VMM Summary of this function goes here
%   Detailed explanation goes here
% I: parent, node_name, visited_time, using_flag

I_new=I;
N=size(I,1);
child=0;

    for i=1:N
        if(I(i,1)==loc && I(i,2)==to && I(i,4)==1)
            child=i;
            break;
        end
    end
    if(child ~= 0)
        I_new(child,3)=I_new(child,3)+1;
        loc_new=child;
    else
        for i=1:N
            if(I(i,4)==0)
                I_new(i,1)=loc;
                I_new(i,2)=to;
                I_new(i,3)=1;
                I_new(i,4)=1;
                loc_new=0;
                break;
            end
        end
    end
                
        

end

