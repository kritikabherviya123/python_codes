size=int(input("Enter size: "))
l=list(map(int,input("Enter elements: ").split()))
print("List: ",l)
ch=int(input("Enter number to be count: "))
print("Count of %d: "%ch,l[:size].count(ch))
