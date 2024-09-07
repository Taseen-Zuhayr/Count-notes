cash = int(input("Enter cash amount:"))

note1 = cash//100
note2 = (cash%100)//50
note3 = ((cash%100)%50)//10
note4 = (((cash%100)%50)%10)//1

print("You will get notes of 100takas:",note1)
print("You will get notes of 50takas:",note2)
print("You will get notes of 20takas:",note3)
print("You will get notes of 1taka:",note4)