from smartphone import Smartphone
iphone_14 = Smartphone("apple","iphone 14", "+79999999999" )
iphone_13 = Smartphone("apple","iphone 13", "+79998999989" )
iphone_12 = Smartphone("apple","iphone 12", "+79169999999" )
iphone_11 = Smartphone("apple","iphone 11", "+79997309999" )
iphone_x = Smartphone("apple","iphone x", "+79999991059" )
catalog = ([
    iphone_14,
    iphone_13,
    iphone_12,
    iphone_11,
    iphone_x
    ])

for phone in catalog:
    print(phone.Name, "-", phone.Model, ".", phone.t_num)