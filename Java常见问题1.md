# Java必会基础知识点

## Java 概述

## Java 基础语法

## Java 面向对象
1. 面向对象和面向过程的区别
        
        这个
        
3. 面向对象三大特性
4. 什么是多态？ Java是如何实现多态的？
5. 面向对象5个基本原则是什么？
6. Java重写(Overwrite)和重载(Overload)的区别
7. Java 对象相等判断
8. Java 类和接口 (Class And Interface)
        
        Abstract 和 Interface 都不能被 实例化, 都不能被继承，都包含abstract method, 其他子类都要覆写
        普通类不能包含Abstract, Abstract可以包含普通类
        Abstract 不能用final修饰, 因为Abstract 需要让其他类继承
        

&emsp;&emsp;&emsp;抽象类 Abstract &emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;接口 Interface&emsp;&emsp;&emsp;&emsp;|    
 :---------------------------------------------------: | :------------------------------------:| 
声明用 abstract|声明用 interface|   
子类用 extend |子类用 implement|
有 constructor |没有 constructor| 
可以是public, private, protected |只能是public | 
 最多继承一个 abstract |可以继承多个 interface |
&emsp;&emsp;&emsp;可以任意 declaration &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp; declaration 必须staic并且final &emsp;&emsp;&emsp;&emsp;| 
<br>

8. 对象引用 和 对象实例 有什么不同？


## Java 变量和方法

## Java 内部类

## Java 值传递

## Java 包(Package)

## Java I/O 流

## Java 反射

## Java 常用API

## Java 集合容器概述

## Java Collection 接口

## Java Map 接口 (HashMap)
1. HashMap的底层数据结构是什么？
2. HashMap的特点有哪些？
3. 解决HashMap冲突的方法有哪些？HashMap用的哪一种？
4. 为什么要在数组长度大于64之后, 链表才会进化成红黑树？
5. 为什么加载因子设置为0.75, 初始化临界值是12？
6. 哈希表底层采用那种算法计算hash值？ 还有哪些算法可以计算出hash值？
7. 当两个对象的hashCode相等时会怎样?
8. 何时发生 哈希碰撞？ 什么是哈希碰撞？ 如何解决哈希碰撞？

        只要两个元素的key计算的hashcode相同就会发生hash碰撞
        jdk8之前用linkedlist解决hash碰撞, jdk8之后使用 linkedlist+红黑树解决hash碰撞
    
9. HashMap的put方法流程？
10. HashMap的扩容方式?
11. 一般用什么作为HashMap的key?
12. 为什么Map桶里的节点个数超过8个才转为红黑树？
13. HashMap为什么线程不安全?
14. 计算Hash值时为什么要让 低16bit 和 高16bit 进行 XOR 处理？

## Java 异常 


