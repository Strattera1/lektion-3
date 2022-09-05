# Lopp 2
# Skapa ett program dör du skriver in två tal
# När de har skrivit in två tal, skriv ut talen mellan de
# tal1 = int (input("skriv in ett tal "))
# tal2 = int (input("skriv in ett tal "))
# if tal1 > tal2:
#     for tal1 in range (0,+1):
#         print (tal1)
# elif tal2 > tal1:
#     for tal2 in range (0, +1):
#      print (tal2)
# print in range (tal1 and tal2)

# tal1 = int(input("tal1 "))
# tal2 = int (input("tal2 "))
# if tal1 > tal2:
#     for tal in range (tal1, tal2, -1):
#         print (tal)
# elif tal1 < tal2:
#     for tal in range (tal1, tal2):
#         print (tal)

tal1 = int(input("skriv in tal1 "))
tal2 = int(input("skriv in tal2 "))
if tal1 > tal2: #10, 2
    start = tal1
    slut = tal2
    supertal = start
    while supertal > slut:
        print (supertal)
        supertal = supertal -1
elif tal1 < tal2: #2,10
    start = tal1
    slut = tal2
    supertal = start
    while supertal < slut:
        print (supertal)
        supertal = supertal +1

