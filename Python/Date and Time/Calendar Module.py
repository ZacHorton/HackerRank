import calendar


if __name__ == '__main__':
    date_input = input().split(" ")
    mm = int(date_input[0])
    dd = int(date_input[1])
    yyyy = int(date_input[2])
    my_date = calendar.weekday(yyyy, mm, dd)
    print(calendar.day_name[my_date].upper())
    
