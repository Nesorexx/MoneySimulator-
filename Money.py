import time
account_number = input("Please enter your account number: ")
account_name = input("Please enter your account name: ")
bank_name = input("Please enter your bank name: ")
Time = time.ctime()
text = "Transfering...."
currency = input(,"Kindly enter your currency you can use both simple or short name for it: ")
amount =  int(input("Kindly input amout you want to download: "))
num = 1
while num <= amount:
 print(f"{currency}{num:,}")
 num += 1
 time.sleep(0.000000001)
 
print(f"{currency}{num:,} sucessfully downloaded.")
for t in text:
 print(t,end="",flush=True)
 time.sleep(0.09)
print() 
print(f"{currency}{num:,} succesfully transfered from Money download to:")
print(f"Account number: {account_number}")
print(f"Account name: {account_name}") 
print(f"Time: {Time}")
