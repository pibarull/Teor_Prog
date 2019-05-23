close all; clear all;

 A = [2     1    3
     11     7     5
   9     8     4];
B = [10; 2; 6];

       
disp('A matrix');
disp(A);
disp('B matrix');
disp(B);

gauss_f(A,B);

LU_f(A,B);

A = [3 2 -1
     2 3 1
     -1 1 3];
    
disp('Choletskii');
x = chol(A);
disp(x);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function gauss_f(A,B)
r=size(A,1);
c=size(A,2);

AB=[A,B];
    if (rank(A)==rank(AB))
       
        if (rank(A)==c)
            disp('Solution');   
            
            k=1;
            while k<=r
                if(AB(k,k)~=0)
                    AB(k,:)=AB(k,:)/AB(k,k);
                    for i=k+1:r
                        AB(i,:)=AB(i,:)-AB(k,:)*AB(i,k);
                    end
                    k=k+1;
                else
                    temp=AB(k,:);
                    AB(k,:)=[];
                    AB=[AB;temp];
                end
            end
            for i=r-1:-1:1
                for j=i+1:c
                    AB(i,:)= AB(i,:)-AB(j,:)*AB(i,j);
                end
            end
            disp (AB(:,end));
        else disp('More than 1 solution');
        end
    else
        disp('No solution');
    end
   
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function LU_f(A,B)
k = size(A);
L = zeros(k);
U = eye(k);
if det(A) == 0
    return
else
    for i = 1:k
        for j = 1:k
            if i>=j
                sm1 = 0;
                for s = 1:j-1
                    sm1 = sm1 + L(i,s)*U(s,j);
                end    
                L(i,j) = A(i,j) - sm1;
            else
                sm2 = 0;
                for s = 1:i-1
                    sm2 = sm2 + L(i,s)*U(s,j);
                end
                U(i,j) = (1/L(i,i))*(A(i,j) - sm2);
          end
        end
    end
end

disp('U matrix = ');
disp(U);
disp('L matrix = ');
disp(L);
disp('L*U = ');
x = inv(U)*inv(L)*B;
disp(x);
end