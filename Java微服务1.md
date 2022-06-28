Spring ---- 一个常用的 Java Web开发框架 (核心是 IOC 控制反转 和 AOP 面向切面编程)</br>
Maven ----- 一个Spring 必须使用的 project management tool (主要控制项目和依赖 (又可以叫环境) )

1. 首先用 Maven 构建 JAVA Spring 项目
2. 然后 在 pom.xml 里面配置 各种依赖 <dependency>
3. 然后通过各种 applicationContext.xml 对类进行管理  (IOC 控制翻转 ---- IOC 解决 过耦合问题 ) 这里的 xml 可以将 service, dao，springmvc, mybatis 分别用一个xml配置
    (Inverse Of Control)
    Dependency Injection 依赖注入:
        在 applicationContext中， 使用 <bean><property></property></bean> 进行 依赖注入
        dao层 对 service层进行 DI 依赖注入, service层和dao层 两者均在IOC容器里创建对象，功能层在Spring里面获取 service 和 dao 对象 实现功能
            
            ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
            UserService usImpl = (UserService) ac.getBean("usImpl");
            usImpl.hello();
    
    <img src="https://raw.githubusercontent.com/JiahuiZhu1998/Interview-Preparing/master/spring_pic1.png" alt="image1" width="800px" height="300px">
    
    <h2>Spring IOC DI 常用注解</h2>
    
        IOC 管理常用注解
        @Component:  把注解的类加入IOC容器管理
        @Repository: 在持久层使用此类  @Service: 在业务层使用此类  @Controller: 在控制层使用此类
        @Configuration: 声明配置
        @ComponentScan: 扫描包结构
        @Import:     引用新的配置
        @Bean:       将对象存入IOC
    
        DI 常用注解 
        @ Value:     注入普通类型 (String, int, Double 等)
        @ Autowired: 注入引用类型
        @ Qualified: 按id名称注入, 与 @Autowired一起使用
        @ Resource:  Java原生注解
 
4. Spring AOP (4.1使用 JDK动态代理[有接口]: 调用Java反射中的Proxy 和 InvocationHandler 两个类) (Aspect Oriented Programming)
              (4.2使用 CGLIB动态代理[无接口]) 
    
    <h2>Spring AOP 术语</h2>
    
        Joinpoint(连接点):
        Pointcut(切入点):
        Advice(通知):
        Target(目标对象):     Proxy(代理对象):
        Aspect(切面):        Weaving(织入):
    
    <h2>Spring AOP 通知</h2>
    
        aop:before 执行前通知                         aop:after:执行后通知; 
        aop:after-returning: 执行成功后通知            aop:after-throwing: 执行失败后通知
        aop:around: 执行前后通知，目标对象要手动执行
    
    <h2>Spring AOP 常用注解</h2>
        
        @Aspect:
        @Before:                                    @After:
        @AfterReturning:                            @Around:
        @AfterThrowing:                             @EnableAspectJAutoProxy:
    
    <h2>Spring 声明式事务管理</h2>
    
        PlatformTransactionManager 平台事务管理器
        TransactionDefinition      事务定义类
        TransactionStatus:         事务状态
    
    
    

       
