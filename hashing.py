from collections import Counter

import bcrypt
# password = '1234'
# bytes = password
#
# a = 'ab'
# print (a.encode('utf-8'))


#
# password = '1234'
# bytes = password.encode('utf-8')
# salt = bcrypt.gensalt()
# hash = bcrypt.hashpw(bytes, salt)
#
# new_pass = '1234'
# bytes_pass = new_pass.encode('utf-8')
# print (bcrypt.checkpw(bytes, hash))




'''
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/secde1/test.git
git push -u origin main'''
'''



git config --global user.name "Isomiddin21"
    git config --global user.email "isomiddinwtu@gmail.com"

    ssh -T git@github.com


    
    


    cat ~/.ssh/id_rsa.pub
'''







# import smtplib
# from email.message import EmailMessage
# arr = ["donyorbek068@gmail.com",
# "saidakbaruraimov7@gmail.com",
# "isomiddinwtu@gmail.com",
# "mohirmirahmadov@gmail.com",
# "zoirbekergashev4567@gmail.com",
# "khayrullo.devs@gmail.com",
# "imonqulovf1234@gmail.com",
# "samidilloravshanov13@gmail.com",
# "shahrizodaxakimova12@gmail.com",
# "9140380@gmail.com",
# "shohjahonobruyev3@gmail.com",
# "diyorbekdilmurodov1@gmail.com",
# "suratovdoniyor@gmail.com",
# "dilshodbekakhmatov@gmail.com",
# "nurillayevezozbek@gmail.com",
# "saidakbaruraimov7@gmail.com",
# "mohirmirahmadov@gmail.com",
# "fazliddinovzokirjon001@gmail.com",
# "zoirbekergashev4567@gmail.com",
# "azamovshahboz06082001@gmail.com",]
# # set your email and password
# # please use App Password
# import time
# start = time.time()
#
# for i in arr:
#     email_address = "isomiddinwtu@gmail.com"
#     email_password = "itxjlxzummnahsid"
#
#     # create email
#     msg = EmailMessage()
#     msg['Subject'] = "Friendship"
#     msg['From'] = email_address
#     msg['To'] = f'{i}'
#     msg.set_content("Boldi otiruramizda mnde bir gaplashib")
#
#     # send email
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(email_address, email_password)
#         smtp.send_message(msg)
# print (time.time() - start)
#
#
#

# grid = [
#     [1,2,4],
#     [3,3,1]
#     ]
#
# r = []
# for i in grid:
#     i.sort()
# for i in zip(*grid):
#     r+=max(i)
# print (r)


# grid = [
#     [1, 2, 4 , 8],
#     [1, 3, 3 , 9]
# ]
# for i in zip(*grid):
#     print(*i[::-1])


# names = ["Isomiddin","Muminov","Davron"]
# heights = [180,165,170]

# l = list(zip(names,heights))
# print (l)
#
# names = ["Mary","John","Emma"]
# heights = [180,165,170]
#
# l = list(zip(names, heights))
# sorted_l = sorted(l , key=lambda x : x[1] , reverse=True)
# re = []
# for i in sorted_l:
#     re.append(i[0])
# print(re)



# print(list(map(lambda x : x[0],sorted(zip(names , heights) , key=lambda x: x[1], reverse=True))))
















# """
# sudo apt-get install get
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Isomiddin21/Test.git
# git push -u origin main"""


# s = []
# for i in words[0]:
#     for j in range(len(words)):
#         if words[0][i] in words[j+1][i]:
#             if words[0][i] in words[j+2][j]:
#                 s.append(words[i])
# print(s)
#         if words[0][i] in words[i+2][i]:
#     if words[0][i] in words[i+1][i]:
#             s.append(words[i])
# print(s)
s = []
# for i in words[0]:
#     for j in range(1, 2):
#         if i in words[j]:
#            if i in words[j+1]:
#               s.append(i)
#
# words = ["bella","label","roller"]

nums = [3,2,1,4]
if len(nums) < 3:
else:
    sorted(nums[:3])[1]
print(-1)














































