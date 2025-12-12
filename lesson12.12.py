torque = int(input("Введите параметр крутящего момента : "))
rpm = int(input("Введите параметр оборота в минуту : "))

horse_power = ((torque * rpm)/(5252))

print(horse_power)