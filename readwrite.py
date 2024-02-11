# months = open('months.txt')

# print(months.mode)

# print(months.readable())

# print(months.read())

# print(months.readline())
# print(months.readline())

# print(months.readlines())
# months.seek(0)
# print(months.readlines())

# for month in months:
#     print(month.strip())

# months.close()

# =========================================

# days = open('days.txt', 'w')
days = open('days.txt', 'a')

# print(days.mode)
# print(days)

# days.write('Monday\n')
# days.write('Tuesday\n')
days.write('Wednesday\n')
# days.write('Thursday\n')
# days.write('Friday\n')
# days.write('Saturday\n')
# days.write('Sunday\n')

days.close()