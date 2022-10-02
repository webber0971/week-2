

# 要求一：函式與流程控制
# 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可
# 以假設 max 一定大於 min 且為整數，step 為正整數。

# python

from math import fabs
from symbol import return_stmt

print("第一題----------------")

def calculate(min,max,step):
    total = min
    temp=min
    while temp+step <= max:
        temp=temp+step
        total = total + temp
    return(total)
print(calculate(1,3,1))
print(calculate(4,8,2))
print(calculate(-1,2,2))


print("第二題----------------")

# 要求二：Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
# manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
# 不定的情況。

# python
def avg(data):
    employeesList = data["employees"]
    x=0
    count=0
    allSalary=0
    for x in range(len(employeesList)):
        tempEmploy = employeesList[x]
        if(tempEmploy["manager"]==False):
            count=count+1
            allSalary=allSalary+tempEmploy["salary"]
    print(allSalary//count)

# 請用你的程式補完這個函式的區塊


avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式


# 要求三：
# 完成以下函式，最後能印出程式中註解所描述的結果。


print("第三題----------------")


def func(a):
    def f(b,c):
        print(a+b*c)
        return a+b*c
    return f

# # 請用你的程式補完這個函式的區塊
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# # 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果




print("第四題----------------")
# 要求四：
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
    max=nums[0]*nums[1]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]*nums[j]>max):
                max=nums[i]*nums[j]
    print(max)


# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10


print("第五題----------------")
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.

def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if((nums[i]+nums[j])==target):
                ans=[i,j]
                return ans

# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

print("第六題----------------")
def maxZeros(nums):
    max=0
    for i in range(0,len(nums)):
        if(nums[i]==0):
            temp=1
            for j in range(i+1,len(nums)):
                if(nums[j]==0):
                    temp=temp+1
                else:
                    break
            if(temp>max):
                max=temp
    print(max)


# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
