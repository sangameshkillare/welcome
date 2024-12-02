# i=0
# n=5

# while i<n:
#     j=0
#     bg=''
#     while j<n:
#         bg+='0'
#         j+=1
#     print(bg)
#     i+=1


# i=0
# n=5

# while i<n:
#     j=0
#     bg=''
#     while j<=i:
#         bg+='0'
#         j+=1
#     print(bg)
#     i+=1


# i=5
# n=5

# while i<=n and i>=0:
#     j=1
#     bg=''
#     while j<=i:
#         bg+='0'
#         j+=1
#     print(bg)
#     i-=1


# i=5
# n=5
# while i>0:
#     j=0
#     bg=''
#     while j<i:
#         bg+='0'
#         j+=1
#     print(bg)
#     i-=1


# i=1
# n=5
# while i<=n:

#     #loop for dash
#     j=1
#     dash="-"
#     num=""
#     while j<=(n-i):
#         dash+="-"
#         j+=1
#         k=1
#     while k<=i:
#         num+=str(k)
#         k+=1
#         print(dash+num)
#     i+=1

# for i in range(1,5):
#     for k in range(1,5-i):
#         print("-", end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print("\n")


# i=5
# n=5
# while i>0:
#     j=1
#     bg=''
#     while j<=i:
#         bg+='0'
#         j+=1
#     print(bg)
#     i-=1


# i=0
# n=5
# while i<n:
#     print("-" * i + "*" *(n-i) )
#     i+=1


# i=0
# n=5
# while i<n:
#     j=0
#     star="*"
#     space="-"
#     while j<i:
#         space+="-"
#         j+=1
#     k=0
#     while k< (n-i):
#         star+="*"
#         k+=1
#     print(space+star)
#     i+=1

# i=1
# n=5
# while i<n:
#     star="*"*i
#     print(star)
#     i+=1

# num=int(input("enter the nuber:"))
# if num % 2==0 :
#     print("even nuber")
# else:
#     print("odd nuber:")

# num = int(input("enter the nmuber :"))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"The {num} is not prime ")
#             break
#     else:
#         print("It is prime")
# else:
#     print("It is not prime num")


# l=int(input("Enter the length :"))
# b=int(input("Enter the Breadth :"))
# if l and b  > 1:
#     area=l*b
#     print(f"The area of rectangle is : {area}")

#factorial

# fact=int(input("enter the nuber :"))
# factorial=1
# if fact>1:
#     for i in range(1,fact+1):
#         factorial*=i
#     print(factorial)


#SUM OF 1 TO N

# num=int(input("Enter the number:"))
# if num >1:
#     sum=0
#     for i in range(1,num+1):
#         sum += i
#     print(sum)

#even nuber from i nto n
# num=int(input("Enter the number:"))
# if num >1:
#     for i in range (1,num+1):
#        if i %2==0:
#         print(i)


#Swap 2 numbers

# a=5
# b=6
# print(f"a={a},b={b}")
# temp=a
# a=b
# b=temp
# print(f"a={a},b={b}")

#teprature to celcius

# temp=int(input("what is the temprature="))
# print(temp)
# F=temp*9/5+32
# print(f"Farenhite={F}")
