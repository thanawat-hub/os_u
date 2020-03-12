#mv เหมือนย้ายไฟล์ และสามารถเปลี่ยนชื่อได้
#tor@ubuntu:~/Desktop$ mv 123.py sys_argv.py
#tor@ubuntu:~/Desktop$ mv sys_argv.py overall/learn_/
#tor@ubuntu:~/Desktop$ mv overall/learn_/sys_argv.py .

import sys
print(sys.argv[1:])#ไม่เอาตัวแรกของ อากิวเม้น(same mean )
a = 3
print("I'm In folder (current) %d"%(a))
