# 面试准备资料

### 大厂面经，机经算法题
        
### Java 基础 和 八股文 (JVM原理，JAVA I/O )

    -- Java I/O  https://www.cnblogs.com/CoLo/p/15029877.html
    
    -- Java 常用类 https://www.cnblogs.com/CoLo/p/15029835.html
    
    -- Java Collections 集合 https://www.cnblogs.com/CoLo/p/15029845.html
    
    -- Java 反射
    
    -- Java 垃圾回收
    
    -- Java 网络编程 https://www.cnblogs.com/CoLo/p/15029881.html
    

    
    -- StringUtils
      -- isEmpty/isNotEmpty/isNotBlank/isBlank/isAnyEmpty/isNoneEmpty/isAnyBlank/isNoneBlank 的区别
    -- BigDecimal
    -- 谈一谈Java ClassLoader机制的理解 https://www.cnblogs.com/CoLo/p/15339193.html

### Java 微服务 (Spring, SpringMVC,SpringCloud, Hibernate, ElasticSearch, Mybatis, Redis, Memcache, rmq, RabbitMQ, ActiveMQ, Kafka,Hive, Spark, MongoDB)

    -- ElasticSearch 实现分页的三种方式
      -- from + size 浅分页
      -- scroll 深分页
      -- search_after 深分页
      
    -- Redis 使用场景
      -- Redis 做数据库
      -- Redis 做缓存 Cache
      -- Redis 做计数器
      -- Redis 做排行榜
      -- Redis 做好友关系
      -- Redis 做统计活跃用户数
      -- Redis 做分布式锁
      -- Redis 做分布式限流
      -- Redis 做消息队列
      -- Redis 做LBS 应用


### Java 多线程和高并发 (Hadoop, 高并发分布式, ThreadLocal)
  
    --多线程间通信方法(5种) (代码: comminicate_threads.java )
       -- 使用 volatile 关键字
       -- 使用 class Object中的 wait() 或者 notify()
       -- 使用 JUC 工具类 CountDownLatch
       -- 使用 ReentrantLock 结合 Condition
       -- 基本 LockSupport 实现线程间的阻塞和唤醒

    --多线程保证线程安全(10种)
       -- 无状态
       -- 不可变
       -- 无修改权限
       -- synchronized
       -- Lock
       -- 分布式锁
       -- volatile
       -- ThreadLocal
       -- 线程安全集合
       -- CAS
       -- 数据隔离
       

### Python 微服务 (Flask, Django, FastAPI)

### MYSQL (关系型数据库)

[MYSQL总结](https://github.com/JiahuiZhu1998/Interview-Preparing/blob/master/MYSQL总结1.md)
    
       -- MYSQL 间隙锁死锁问题 https://www.jianshu.com/p/a0aa55e9dce7

-- RPC服务，HTTP服务 (Dubbo, gRPC, Thrift, Netty, Nginx, Tomcat, CDN, 负载均衡 )
