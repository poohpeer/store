from admin import Admin

user1 = Admin("Puper", "puper", "1234", "admin")
user2 = Admin("Puper", "puper", "1234", "admin")

comp = user1 == user2
print comp
