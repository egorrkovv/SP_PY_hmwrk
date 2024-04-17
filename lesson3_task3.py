from adress import address
from mailing import mailing

to_address = address("1111111", "moscow", "novie_cheremushki", "50", "10")
from_address = address("0000000", "china", "xiao8", "322", "100")
Mailing = mailing(to_address, from_address, 0, "zxc322")

print("Отправление", Mailing.track, "из", from_address.index, from_address.city, from_address.street, from_address.house, from_address.flat, "в", to_address.index, to_address.city, to_address.street, to_address.house, to_address.flat)