# Optional Assignment: 课程总结

Updated 1640 GMT+8 Dec 28, 2023

2023 fall, Complied by ==苏王捷 工学院==



**说明：**

1）12月28日期末机考： AC6

2）本次作业可选，不计分。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。





## 1. 期末机考题目



### 27273: 简单的数学题

implementation, math, http://cs101.openjudge.cn/practice/27273



思路：就是数学方法了



##### 代码

```python
import math
for _ in range(int(input())):
    n=int(input())
    ans=(n+1)*n//2
    m=int(math.log(n,2))
    ans-=2*(2**(m+1)-1)
    print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20231228220942870](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20231228220942870.png)

### 27301: 给植物浇水

Implementation, two pointers, http://cs101.openjudge.cn/practice/27301



思路：双指针，分情况讨论



##### 代码

```python
n,a,b=map(int,input().split())
line=list(map(int,input().split()))
l,r=0,n-1
t=n
ta,tb=a,b
ans=0
while t>1:
    if ta>=line[l]:
        ta-=line[l]
        l+=1
        t-=1
    else:
        ta=a
        ans+=1
        ta-=line[l]
        l+=1
        t-=1
    if tb>=line[r]:
        tb-=line[r]
        r-=1
        t-=1
    else:
        tb=b
        ans+=1
        tb-=line[r]
        r-=1
        t-=1
if t==1:
    if ta<line[l] and tb<line[r]:
        ans+=1
print(ans)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20231228221022653](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20231228221022653.png)



### 27274: 字符串提炼

implementation, http://cs101.openjudge.cn/practice/27274



思路：同样熟悉的双指针



##### 代码

```python
import math
s=" "+input()
n=len(s)-1
m=int(math.log(n,2))
ans=""
l,r=0,m
m+=1
while m>1:
    ans+=s[2**l]+s[2**r]
    l+=1
    r-=1
    m-=2
if m==1:
    ans+=s[2**l]
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20231228221103543](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20231228221103543.png)



### 27310: 积木

implementation, brute force, http://cs101.openjudge.cn/practice/27310



思路：每个积木只能最多用一次，符合dfs法则，那就开搜！



##### 代码

```python
def dfs(s,num,l):
    if num==l:
        return True
    for i in range(4):
        if i not in vis and s[num] in dic[i]:
            vis.add(i)
            if dfs(s,num+1,l):
                return True
            vis.discard(i)
    return False

n=int(input())
dic=[]
for i in range(4):
    dic.append(set(input()))
for i in range(n):
    s=input()
    l=len(s)
    vis=set()
    flag=dfs(s,0,l)
    print("YES" if flag else "NO")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20231228221155524](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20231228221155524.png)



### 27237: 体育游戏跳房子

bfs, http://cs101.openjudge.cn/practice/27237



思路：heapq的优势正在于此，在保持队列的情况下每次都能找到最短及字典序最小的路径



##### 代码

```python
import heapq
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    fun=["H","O"]
    vis=set()
    vis.add(n)
    heap=[]
    heapq.heappush(heap,(0,"",n))
    while heap:
        step,path,spot=heapq.heappop(heap)
        if spot==m:
            break
        for i in range(2):
            func=fun[i]
            if func=="H":
                dspot=3*spot
            else:
                dspot=spot//2
            if dspot not in vis:
                vis.add(dspot)
                heapq.heappush(heap,(step+1,path+func,dspot))
    print(step)
    print(path)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20231228221306544](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20231228221306544.png)



### 27373: 最大整数

dp, greedy, string, sort, http://cs101.openjudge.cn/practice/27373



思路：这题是被hack了，乐 ：）

一开始的想法是排序后用dfs+greedy查找，时间意外地短，随后被指出应该搜完，那这样时间复杂度就有可能超过了，不如dp的做法

但是dfs搜完不妨作为一种可能做法（不想写了，相信后人的智慧  :））



##### 代码

```python
def dfs(length):
    if length==m:
        return True
    for i in range(n):
        if i not in vis and length+l[i]<=m:
            vis.add(i)
            ans.append(linenew[i])
            if dfs(length+l[i]):
                return True
            ans.pop()
            vis.discard(i)
    return False 
m=int(input())
n=int(input())
line=list(input().split())
l=[len(i) for i in line]
maxl=max(l)*2
linesort=[(line[i]+line[i]+"9"*(maxl-2*l[i]),i) for i in range(n)]
linesort.sort(reverse=True)
linenew=[line[i[1]] for i in linesort]
l=[len(i) for i in linenew]
ans=[]
vis=set()
while True:
    if dfs(0):
        break
    else:
        m-=1
res=""
for i in ans:
    res+=i
print(int(res))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20231228221648496](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20231228221648496.png)







## 2. 课程总结

如果愿意，请同学或多或少做一个本门课程的学习总结。

便于之后师弟师妹跟进学习，也便于教师和助教改进教学。

例如：分享自己的学习心得、笔记。

好好看，好好学，多做题

所有的算法就本质上来说都不过是优化

真正的要点是计算机思维的培养



