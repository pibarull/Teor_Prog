function [otv] = way1 (a,b,c,d,N,f,g)
fk=0;
for i=1:N
    x0=rand(1)*2-1;
    y0=rand(1)*2-1;
    if g(x0,y0)<=1
        fk=fk+f(x0,y0);
    end
end
otv=(b-a)*(d-c)*fk/N;
end