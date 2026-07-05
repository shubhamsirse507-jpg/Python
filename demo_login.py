import random
import time

class insta:
    def __init__(self,name,username,pwd):
        self.name=name
        self.username=username
        self.pwd=pwd
  #login
    def login(self,username,pwd):
        if self.username==username and self.pwd==pwd:
            print("login successfull")

        #otp
            otp = random.randint(1000, 9999)
            print(f"OTP Send on your mobile no +91 (9167980621)")
            print("Your OTP is:", otp)

            start_time = time.time()

            user_otp = int(input("Enter OTP: "))

            end_time = time.time()

            if end_time - start_time >30:
                print("OTP Expired")

            elif user_otp == otp:
                print("Login Successful")
            else:
                print("Invalid OTP!")
        else:
            print("invalid creditial !")

obj=insta("ram","ram@123",12345)
obj.login("ram@123",12345)