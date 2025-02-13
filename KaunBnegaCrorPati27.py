# l=[["Capital of India","Delhi","Lucknow","Mumbai","Pakistan"],
#    ["Capital of UP","Lucknow","Dlehi","Gujrat","Monkey"],
#    ["Which is fruit","Mango","Carrot","Suger","Anamika"]]
# for i in range(len(l)):
#     print(l[i])
#     ans=input("ENter your answer:")
#     for j in l[i]:
#         if i==0:
#             if i==0 and ans=="Delhi":
#                 print("Yes Right Ans and you won 1000")
#                 break
#             else:
#                 print("Sorry! You can go home no win")
#                 break
#             break
#         if i==1:
#             if i==1 and ans=="Lucknow":
#                 print("Yes Right Ans and you won 5000")
#                 break
#             else:
#                 print("Sorry! You can go home with 1000")
#                 break
#             break
#         if i==2:
#             if i==2 and ans=="Mango":
#                 print("Yes Right Ans and you won 10000")
#                 break
#             else:
#                 print("Sorry! You can go home 5000  money")
#                 break
#             break




questions=[["Capital of India","Delhi","Lucknow","Mumbai","Pakistan",1],
    ["Capital of UP","Lucknow","Dlehi","Gujrat","Monkey",1],
    ["Which is fruit","Mango","Carrot","Suger","Anamika",4]]
level=[1000,5000,10000]
for i in range(0,len(questions)):
    question=questions[i]
    print(f"this question is for RS.{level[i]}")
    print(question[0])
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    ans=int(input("Enter your answer: "))
    if ans==question[-1]:
        print(f" You have won RS. {level[i]}")
    else:
        print("Sorry wrong answer")
        break
    