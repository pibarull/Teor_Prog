f=@(x,y)4*(x).^2+1*(y).^2;
g=@(x,y)x^2+y^2; %<=1

n=0;
N=1000000;
fk=0;
R = 1
a=-R;
b=R;
c=-R;
d=R;
verh=@(x)sqrt(1-x.^2);
niz=@(x)-sqrt(1-x.^2);
tochn = quad2d(f,a,b,niz,verh)
tsr = way1(a,b,c,d,N,f,g)
MK = way2(a,b,c,d,N,f,g)
