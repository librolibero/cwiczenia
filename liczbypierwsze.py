# Program, któy sprawdza czy wpisana liczba jest pierwsza, czy nie

num = 34634374

# liczba pierwsze musi być większa od 1
if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"To nie jest liczba pierwsza.")
           
           break
   else:
       print(num,"jest liczba pierwsza")

else:
   print(num,"nie jest liczba pierwsza")
   main()