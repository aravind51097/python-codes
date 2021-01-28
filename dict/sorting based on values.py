day={ 'monday':'1','tuesday':'2','thursday':'4','saturday':'6','wednesday':'3'}
print("before sorting the div by vallue",day)
dic2={k:v for v,k in sorted(day.items())}
print(dic2)
day1={k:v for v,k in sorted(dic2.items())}

print(day1)
