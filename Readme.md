# 面试准备资料

### 大厂面经，机经算法题

&emsp;&emsp;&emsp;&emsp;[Java 面试问题 1](https://github.com/JiahuiZhu1998/Interview-Preparing/blob/master/Java常见问题1.md)
        
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

&emsp;&emsp;&emsp;&emsp;[MYSQL总结](https://github.com/JiahuiZhu1998/Interview-Preparing/blob/master/MYSQL总结1.md)
    
       -- MYSQL 间隙锁死锁问题 https://www.jianshu.com/p/a0aa55e9dce7

### 大数据相关

       -- MongoDB, Hbase, HiveSQL, Hadoop, Flink, Spark, Doris
       
### NLP相关

       -- 1. 机器学习(12种ML基础算法, 集成学习[随机森林, GBDT,XGB,Stacking], 条件随机场CRF, 贝叶斯网络, 支持向量机, 主题模型)
       -- 2. 深度学习(神经元模型, 多层感知机, BackPropogation, 激活函数, Word2Vec, RNN, CNN, LSTM, BiLSTM-CRF, TextCNN, Attention, Transformer, Bert)
       -- 3. 工具(TensorFlow, Pytorch)
       -- 4. NLP深入 (BERT-based, 模型蒸馏, 抽取式和生成式摘要模型， GPT-3, 文本分类, 序列标注类型, 图神经网络和表示学习)
       -- 5. NLP项目 (中文分词[搜狐新闻场景下的中文分词器], 关键词提取[类新浪门户场景下的关键词提取], 实体识别[类新浪微博下的实体识别], 文本分类[头条新闻标题分类场景下的Bert分类器训练, 优化和蒸馏], 文本摘要[实现一个基于GPT的生成式摘要模型], 对话系统[搭建工业级对话系统, 检索型/任务型/闲聊型], 知识图谱[构建知识图谱])
       -- 6. Prompt Learning 提示学习 (小样本问题，自然文本生成[GPT3, UNiLM, T5, T0], Adapter和 P-tuning， NER和提示学习)
       
### 网络 

-- RPC服务，HTTP服务 (Dubbo, gRPC, Thrift, Netty, Nginx, Tomcat, CDN, 负载均衡 )

### Linux 操作

    --linux ps进程相关操作, 看端口有没有开启, 引用传递和值传递, r,b,u 分别是什么意思
    -- 谈一谈Java ClassLoader机制的理解 https://www.cnblogs.com/CoLo/p/15339193.html
