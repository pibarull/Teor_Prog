function [otv] = way2 (a,b,c,d,N,f,g)
fmax=0;
n=0;
for i=1:N
    x0=rand(1)*2-1;
    y0=rand(1)*2-1;
    if f(x0,y0)>fmax
        fmax=f(x0,y0);
    end
end
for i=1:N
    x0=rand(1)*2-1;
    y0=rand(1)*2-1;
    z0=rand(1)*fmax;
    if g(x0,y0)<=1
        if z0<=f(x0,y0)
        n=n+1;
        end
    end
end
otv=(b-a)*(d-c)*fmax*n/N;
end