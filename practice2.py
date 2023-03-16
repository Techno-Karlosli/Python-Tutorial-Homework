# 写一个函数，其能够将形如 "12AUG2017"的字符串 转化为 20170812 的整型数字

# day/month/year  year/month/day
# 12082017
# 20/06/2006

Date=str(input())
if len(Date)>8:
    dict={"JAN":"01","Jan":"01","FEB":"02","Feb":"02","MAR":"03","Mar":"03","APR":"04","Apr":"04","MAY":"05","May":"05","JUN":"06","Jun":"06","JUL":"07","Jul":"07","AUG":"08","Aug":"08","SEP":"09","Sep":"09","OCT":"10","Oct":"10","NOV":"11","Nov":"11","DEC":"12","Dec":"12"}
    Month=dict[Date[2:5]]
    Day=Date[0:2]
    Year=Date[5:9]
    print(''.join([Year,Month,Day]))
else:
    print(''.join([Date[4:8],Date[2:4],Date[0:2]]))

input("按任意键退出")