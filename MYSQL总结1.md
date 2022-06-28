MYSQL 基本问题以及调优方法
===

## 数据库基础

  1. 事务的ACID特性是什么
  2. ACID特性靠什么保证？
  3. SQL语句主要分为哪几类 
  4. 事务的隔离级别有哪些？MYSQL默认隔离级别是什么？
  5. 事务的每个隔离级别都是如何实现的？
  6. 什么是脏读，幻读，不可重复读？
  7. 视图有哪些特点？
  8. SQL的生命周期
  9. Primary Key 使用自增ID还是UUID? 
  10. MYSQL主从复制解决了哪些问题？
  11. 什么是MYSQL的GTID?
  12. MYSQL常用的备份工具有哪些？
  13. MYSQL备份计划如何制定？
  14. MYSQL事务的默认隔离级别是什么？可以解决幻读问题吗？
  15. MyISAM 和 Innodb 的区别是什么？
  16. MYSQL的内连接，外连接，交叉连接，笛卡尔积分别是什么？
  17. MYSQL的内连接，外连接，左连接，右连接有什么区别？
  18. MYSQL中 varchar 和 char 的区别？
  19. MYSQL中 blob 和 text 的区别？
  20. MYSQL中 Datetime 和 timestamp 的异同？
  21. MYSQL中 in 和 exists的区别？
  22. MYSQL中记录货币用什么字段类型比较好
  23. MYSQL怎么储存emoji?
  24. MYSQL中 drop，delete, truncate的区别？
  25. MYSQL中 UNION 和 UNION ALL的区别？
  26. MYSQL中 count(1), count(1) 和 count(column_name) 的区别？

 
## 数据库架构

  1. 一条SQL查询语句的执行顺序？
  2. MyISAM 和 Innodb 的区别是什么？
  3. MYSQL的基础架构？
  4. 一条SQL查询语句在MYSQL中如何执行？
  5. MYSQL有哪些常见的存储引擎？
  6. 存储引擎应该如何选择？

## 数据库日志

  1. MYSQL的日志文件有哪些？ 作用分别是什么？
  2. MYSQL中 binlog 和 redo log有什么区别？
  3. 一条update语句是如何执行的？
  4. 为什么要两阶段提交？
  5. redo log怎么刷入磁盘的？

## 数据库优化
  1. 数据库的三大范式是什么
    
    第一范式: 每个列不可以再拆分
    第二范式:
    第三范式:
    
  2. 慢SQL是什么? 如何定位？
  3. 有哪些方法优化慢SQL?
  4. MYSQL 有关权限的表有哪几个
  5. 怎么看执行计划(explain), 如何理解其中各个字段的含义？
  6. 简单说一下索引的分类？
  7. 为什么使用索引会加快查询？
  8. 创建索引有哪些注意点？
  9. 索引在哪些情况下会失效？
  10. 索引不适合哪些场景？
  11. 索引是不是越多越好？
  12. MYSQL索引用的什么数据结构？
  13. MYSQL中一颗B+ Tree能存储多少条数据呢？
  14. 为什么要用B+树，而不用普通二叉树？
  15. 为什么用B+树，而不用B树？
  16. Hash索引和B+树索引区别是什么？
  17. Cluster Index 和 Non-Cluster Index的区别？
  18. 回表了解吗？
  19. 覆盖索引了解吗？
  20. 什么是最左前缀原则 和 最左匹配原则？
  21. 什么是索引下推优化？
  22. MYSQl有哪些锁？列举一下
  23. 表级锁和行级锁的区别？
  24. InnoDB里的行锁实现
  25. 意向锁是什么？
  26. MYSQL里的乐观锁和悲观锁了解吗？
  27. MYSQL遇到过死锁吗？如何解决的？
  28. MVCC了解吗？怎么实现的？
  29. MYSQL间隙锁问题

## 数据库高可用/性能

  1. MYSQL分库分表的目的是什么？
  2. 数据库读写分离了解吗？
  3. 读写分离的分配如何实现？
  4. 主从复制原理了解吗？
  5. 主从同步延迟如何处理？
  6. 一般如何分库分表
  7. 水平分表有哪几种路由方式？
  8. 不停机扩容如何实现？
  9. 常见的分库分表中间件有哪些？
  10. 分库分表会带来哪些问题？
  11. 百万级别以上的数据如何删除？
  12. MYSQL数据库CPU飙升到100%的时候怎么处理？
  13. 百万千万级大表如何添加字段？

## MYSQL 优化的12种考量
  1. 尽量避免使用子查询，将嵌套查询换成join表。在使用join时，mysql不需要在内存中使用临时表
  2. 用 IN 来替换 OR
        `<Select * where id=10 or id=20 换成 select * where id IN (10,20)>`
  3. 多用limit, 不要读取多余的无用记录(分页查询 limit M,N)
  4. 禁止不必要的 Order By 排序
  5. 多用union all 而不是union 因为union需要合并数据再排序，费时费力
  6. 尽量避免用到 Rand()随机数 因为随机数没法用到索引
  7. 将多次插入换成一次插入但插入一些数据
      ```
        Insert into t(id,name) VALUES(2,'bbb');
        Insert into t(id,name) VALUES(3,'ccc');
        
        Insert into t(id,name) VALUES(2,'bbb'),(3,'ccc');
      ```
  8. 少用 select * 而是用select 变量名，并且只返回需要的列
  9. 外表小内表大 用 exist, 外表大内表小用 in做查询
  10. 优化 group by
      ```
      低效:   select job, avg(sal) from emp group by job having job='president' or job='manager'
      高效:   select job, avg(sal) from emp where job='president' or job='manager' group by job
      ```
      
  11. 尽量使用数字字段而不是字符
  12. 优化join
      ```
      当连接查询没有 where条件时:
          left join   前面是驱动表, 后面是被驱动表
          right join  后面是被驱动表, 前面是驱动表
          inner join/join 会自动选择表数据比较少的作为驱动表
          straight_join 直接选择左边的表作为驱动表
          
      当连接查询有 where 条件时:
          带 where 条件的是驱动表, 否则是被驱动表
      ```

  



  
  
  

    
