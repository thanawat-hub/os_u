# asd = '124'
# print(len(asd))

# var = '123'
# a ='print %s'%(var)
# exec(a)
# var = 456
# exec(a)

# import os 

# print(os.name)#/เป็นคำสั่งสำหรับแสดงชื่อระบบปฏิบัติการ
# print(os.getcwd())
# os.chdir("overall")#('ตำแหน่งโฟลเลอร์')
# print(os.getcwd())

# #os.system เป็นการสั่งคอมานด์ไลน์
# os.system('mkdi8') #ลองพิมพ์คำสั่งมั่ว ๆ ลงไป
# # return1 #คำสั่งทำงานไม่ถูกต้อง

# # เป็นคำสั่งที่ใช้ในการตรวจสอบสถานะ server ปลายทาง โดยทำการส่งสัญญาณ ICMP ECHO_REQUEST 
# # ผ่าน network ไปยังปลายทาง ถ้าสัญญาณตอบกลับมา ใช้ในการตรวจสอบ connection, ip ,port
# #  และ response time ของ server ปลายทางว่าปกติไหม
# # os.system('ping google.com') #สั่งให้ ping กูเกิล
# # return 0 #คำสั่งทำงานถูกต้อง

# print(os.listdir("/home/tor/Desktop"))#(path)
# # เป็นคำสั่งสำหรับแสดงรายชื่อไฟล์ที่อยู่ใน path ที่กำหนดโดยแสดงผลลัพธ์ออกมาเป็นชนิดข้อมูลแบบ list


class ComplexDict:
  def __init__(self, key):
    self.__list__ = []
    key = str(key)
    self.__list__.append([key,[]])

  def add_key(self, key):
    if not self.has_key(key):
      self.__list__.append([key,[]])

  def __repr__(self):
    return repr(dict(self.__list__))

  def __getitem__(self, key):
    _keys = self.keys()
    if key in _keys:
      index = _keys.index(key)
      return self.__list__[index][1]

  def __delitem__(self, key):
    if self.has_key(key):
      self[key] = []
      self.__list__.remove([key,[]])

  def __setitem__(self, key, val):
    self.add_key(key)
    index = self.keys().index(key)
    self.__list__[index][1] = [val]

  def keys(self):
    return [i[0] for i in self.__list__]

  def values(self):
    return [i[1] for i in self.__list__]

  def has_key(self, key):
    if key in self.keys():
      return True
    else:
      return False

s = ComplexDict('a')
print(s)
s.add_key('b')
print(s)
s['a'] = 1,3,4,5
print(s)

# https://www.thaitux.info/book/export/html/184