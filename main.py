#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(raw_month):
    monthdict = {'January':'01',
                 'February':'02',
                 'March':'03',
                 'April':'04',
                 'May':'05',
                 'June':'06',
                 'July':'07',
                 'August':'08',
                 'September':'09',
                 'October':'10',
                 'November':'11',
                 'December':'12'
                }
    month_num = monthdict[raw_month]
    return month_num

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    token1 = date.split()
    raw_month = token1[0]
    if token1[1][-1] == ',':
        raw_day = token1[1][:-1]
    else:
        raw_day = token1[1]
    if int(raw_day) <= 10:
        day = '0' + str(raw_day[0])
    else:
        day = str(raw_day[0:2])
    
    component_list = []
    component_list.append(parse_month(raw_month))
    component_list.append(day)
    component_list.append(token1[2])
    print('/'.join(component_list))


#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    date = input()
    while date != -1:
        parse_date(date)
        date = input()
        
        
# hereagain
