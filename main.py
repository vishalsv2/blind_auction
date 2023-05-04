from replit import clear
from art import logo
print (logo)

biddict={}

should=True
while should:
  name=input("what is your name? : ")
  amount=int(input("what is your bid amount? : $"))
  
  def bid(name,amount):
     biddict[name]=amount
  
  bid(name,amount)
  # print(biddict)
  next=input("is any other person want to be bid? (yes/no): ").lower()
  if next=="yes":
    should=True
    clear()
  else:
    should=False
    clear()

if should==False:
  bidkey=(max(zip(biddict.values(), biddict.keys())))[1]
  bidvalue=(max(biddict.values()))
  print(f"The Winner of the auction is {bidkey} with a bid of ${bidvalue}.")
  