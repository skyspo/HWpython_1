from adress import Address
from mail import Mailing


add = Address('000000', 'Minsk', 'Mira', '8', '16')
add1 = Address('000001', 'Minsk', 'Okulova', '18', '26')


mail1 = Mailing(add, add1, 100, "10")
mail2 = Mailing(add1, add, 200, "20")

print(mail1)
print(mail2)




