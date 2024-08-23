#Bank System:



#1.create account
#2.Deposit
#3.Withdraw
#4.Exit

#თქვენი დავალება იქნება გააკეთოთ ბანკის სისტემა მოცემული სექციებით პითონში,რაც აქამდე ისწავლეთ გააკეთეთ იმ მასალით გამოიყენეთ თქვენი მაქსიმალური ცოდნა,მერე კი ჩვენ შევამოწმეთ თუ რა დონის ცოდნა გამოიყენეთ და იმის მიხედვით შეიგიმოწმებთ!!!
#მისალმება
print("mogesalmebit chven bankshi")

#ბარატის მოთავსება ბანკომატში
print("")
print("Please show us ur card")

#პინკოდი
print("Please enter ur code for card")
print("")
print(input("please enter pincode:"))
print("")

#ბალანსი
print("on balance u have 2000L")


#თანხის შეტანა
print("")
Deposit =int(input('Deposit money: '))



num=2000




print(num+Deposit,"gela")
print("")
Withdraw=int(input('withdraw money: '))#withdraw
print(num + Deposit - Withdraw, "lari")
print("")

#Balance
balance= num + Deposit - Withdraw

balansi=(input("if u want to know ur balance type 'Know' "))
print(balance, "lari")

#Exit
print("")
Exit="thank u for usin our service bye"
print("")

print (input("if u want to end this type 'end' "))
print("")
print("thanks for using our services we are delighted")
print("end")