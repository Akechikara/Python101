Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
box = []
box.append('ปากกา')
box.append('ดินสอง')
box.append('ยางลบ')
print(box)
['ปากกา', 'ดินสอง', 'ยางลบ']
print(box[1])
ดินสอง
print(box[0])
ปากกา
print(box[-1])
ยางลบ
print(box[-2])
ดินสอง
print(box[-3])
ปากกา
brand = {'pen':['Lamy','Pentel','Fiber-castel'],'pencil':['horse','staedtler'],'eraser':'ยางลบ2สี'}
print(pen)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(pen)
NameError: name 'pen' is not defined. Did you mean: 'len'?
print(brand['pen'])
['Lamy', 'Pentel', 'Fiber-castel']
print(brand['pen'][1])
Pentel
print(brand['pencil'][0])
horse
print(brand['eraser'])
ยางลบ2สี
