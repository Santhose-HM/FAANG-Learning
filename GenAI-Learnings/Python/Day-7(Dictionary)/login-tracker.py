users = ['John','Bob','Alex','Alice','Charlie','John','Alex','Alice','John','Alex']

login = {}

for userName in users:
    if userName in login:
        login[userName]+=1
    else:
        login[userName] = 1
for user,loginCount in login.items():
    print(f"{user:8}:{loginCount}")