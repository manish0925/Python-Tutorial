def code():
    send=input("Enter your code: ")
    if len(send)<=4:
        new_str=""
        new_str+=send[-1]
        for i in range(1,len(send)-1):
            new_str+=send[i]
        new_str+=send[0]
        return new_str
    else:
        li=list(send.split(" "))
        new_li=[]
        for i in li:
            i=i[::-1]
            new_li.append(i)
        
        st=""
        ans=" ".join(new_li)
        return ans
        
        
def decode():
    recieve=code()
    if len(recieve)<=4:
        new_str=""
        new_str+=recieve[-1]
        for i in range(1,len(recieve)-1):
            new_str+=recieve[i]
        new_str+=recieve[0]
        return new_str
    else:
        li=list(recieve.split(" "))
        new_li=[]
        for i in li:
            i=i[::-1]
            new_li.append(i)
        
        st=""
        ans=" ".join(new_li)
        return ans
while True:
    choice=int(input("Enter 1 for code, 2 for decode, 0 for exit: "))
    if choice==1:
        ans=code()
        print(ans)
    elif choice==2:
        ans=decode()
        print(ans)
    elif choice==0:
        break
    else:
        print("Wrong choice")
        break



# send=input("Enter your code: ")
# li=list(send.split(" "))
# new_li=[]
# for i in li:
#     i=i[::-1]
#     new_li.append(i)
# st=""
# ans=" ".join(new_li)
# print(ans)





