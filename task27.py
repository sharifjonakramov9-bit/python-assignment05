### 27. **Pulni to‘lov birliklariga ajratish**
pul = 38500
#“3 dona 10000 so‘mlik, 1 dona 5000 so‘mlik, 1 dona 2000 so‘mlik, 3 dona 500 so‘mlik”
x = pul // 10_000
y = pul % 10_000
z = y // 1_000 
a = pul % 1_000
b = a //100
result = f'''{x} dona 10000 so'mlik, {z} dona 1000 so'mlik, {b} dona 100 so'mlik'''
# sharti xato ketgan yoki man tushunmadim va xato bajardim.
print(result)
# o'ylaymanki hammasini to'g'ri qildim TUGADI!!!!!!!!!!
