# 以下均是面试常遇到的问题(八股文)

### HashMap

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
