dic={'cars':['bmw','suziki','ford','audi'],'phones':['apple','samsung','nokia']}

dic1 = sum(map(len, dic.values())) #maping through the dict values upto len and adding the length
print(dic1)
