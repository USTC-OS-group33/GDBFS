
alpha=0.009;

A=zeros(10);
I=zeros(100,4);
loc=0;
total=0;
to=1;

sigmaMM=0.6;
sigmaVMM=0.4;

eff_MM=[];
eff_VMM=[];
eff_vote=[];
X_MM=[0,0];
X_VMM=[0,0];
X_vote=[0,0];


while(1)
source=to;%input('input source: ')
to=input('input to: ');
%rate=input('input rate: 0.05')

% check
rank=find_loc(X_MM,to);
if(rank==0)
    eff_MM=[eff_MM,0]
else
    eff_MM=[eff_MM,1/rank]
end

rank=find_loc(X_VMM,to);
if(rank==0)
    eff_VMM=[eff_VMM,0]
else
    eff_VMM=[eff_VMM,1/rank]
end

rank=find_loc(X_vote,to);
if(rank==0)
    eff_vote=[eff_vote,0]
else
    eff_vote=[eff_vote,1/rank]
end


[I,loc]=VMM(I,loc,to);
A=learn(A,source,to,0.05);
%sprintf('MM predict:\n')
[node,p]=cal_MM_P(A,to);
X_MM=[node,p];

total=total+1;
%sprintf('VMM predict:\n')
[node,p]=cal_VMM_P(I,loc,total,0);
X_VMM=[node,p];

X_vote=voting(X_MM,X_VMM,sigmaMM,sigmaVMM);

end