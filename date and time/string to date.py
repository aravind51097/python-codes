


from datetime import datetime
date_string="21 oct, 2018"
print(date_string)

date_object=datetime.strptime(date_string,"%d %b, %Y")

print('date is' ,date_object)
