#提示功能列表
def  function():
    print('--->学生管理系统<---')
    print('--------------------')
    print('|-->1.增加学生信息--|')
    print('|-->2.修改学生信息--|')
    print('|-->3.查询学生信息--|')
    print('|-->4.遍历学生信息--|')
    print('|-->5.删除学生信息--|')
    print('|-->6.退出学生系统--|')
    print('---------------------')
#提示用户选择功能
def choice():
    selver=input('请输入您的选项：：')
    return selver
#创建全局列表
list1=[]
StudentSet={}
#获取用户的选择的功能
def fun(num):
   if  num=='1':
       add=input('请输入要添加的学号：（StudentNum）:')
       adds = input('请输入要添加的年龄-学号：（name，age）')
       list1=[adds]
       StudentSet[add]=adds
       return StudentSet
   elif num=='2':
       #修改学生信息
       xiugai=input('请输入要修改的(StudentNum)：')
       xin=input('请输入要更改的元素(name,age)')
       StudentSet[xiugai]=xin
   elif num=='3':
       # 查询学生信息
       chaxun=input("请输入要查询的信息（StudentNum）：")
       print("-----<"+StudentSet[chaxun]+">-----")
   elif num=='4':
       # 遍历学生信息
       for x in StudentSet :
           print("学号-->"+x,StudentSet[x])
   elif num == '5':
       # 删除学生信息
       delect=input('请输入需要删除的信息：（name）')
       print("-----<"+StudentSet.pop(delect)+">-----")
   elif num == '6':
       #退出
       print("-----<退出>-----")
   else:
       #重新输入
       print("-----<输入错误，请重新输入>-----")
#根据用户的选择，执行相应的功能
while True:
    function()
    num=choice()
    fun(num)

