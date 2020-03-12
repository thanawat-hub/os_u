import sys
class SysArgvToPart:
    # print(sys.argv[1:])
    # print(type(sys.argv[:]))
    @property
    def from_sys_list_to_str(self):
        count = 0
        self.ret_sys_argv = ''
        for v in sys.argv[1:]:
            count += 1
            if (v == sys.argv[-1]):
                self.ret_sys_argv += v
            else :
                self.ret_sys_argv += v+"/"

            # self.ret_sys_argv +="{:/<{}}".format("".join(v),self.c_1+self.c_0)    #
            #จัดการตั้งแต่ในนี้ให้เสด
            #%(c+1) ใส่เลข ที่ n(3)  หรือ lengthของการนับอย่างไร
        print("They are %d word"%(count))    
        print(self.ret_sys_argv)
        print(type(self.ret_sys_argv))
        return self.ret_sys_argv 


if __name__ == "__main__":
    if (sys.argv[0] == 'sys_oo.py'):
            
        to = SysArgvToPart()
        print(to.from_sys_list_to_str)
    else :
        print(">>>>>>>>>>> Enter file name After test_3.py(name file.py at run) <<<<<<<<<<<<<<<")

########## for from #######
# display_width = 50
# # print('\n{:^{display_width}}'.format('some text here', display_width=display_width))
# print('{:<{}}'.format('some text here', display_width))
# name ='giacomo'
# number = 4.3
# print('%s %s %d %f %g' % (name, number, number, number, number))

# class Default(dict):
#     def __missing__(self, key):
#         return key
# # c = Default()
# print('{name} was born in {country}'.format_map(Default(name='GuidoO')))
# # 'Guido was born in country'




# a = 'T'
# print('{:_<{}}'.format(a,3+1))
