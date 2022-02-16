import b_InsectClass as I

misquito = I.insect(2, 4)
housefly = I.Insect(3, 6)

misquito = I.Insect()
housefly = I.Insect()

misquito.flight_time()
housefly.flight_length()

print("The misquito can fly up to", misquito.flight_time(), "miles")
print("The housefly can fly up to", housefly.flight_time(), "miles")
