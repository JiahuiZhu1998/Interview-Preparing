Spring ---- 一个常用的 Java Web开发框架 (核心是 IOC 控制反转 和 AOP 面向切面编程) </br>
Maven ----- 一个Spring 必须使用的 project management tool (主要控制项目和依赖 (又可以叫环境) )

1. 首先用 Maven 构建 JAVA Spring 项目
2. 然后 在 pom.xml 里面配置 各种依赖 <dependency>
3. 然后通过各种 applicationContext.xml 对类进行管理  (IOC 控制翻转 ---- IOC 解决 过耦合问题 ) 这里的 xml 可以将 service, dao，springmvc, mybatis 分别用一个xml配置
    Dependency Injection 依赖注入:
        在 applicationContext中， 使用 <bean><property></property></bean> 进行 依赖注入
        dao层 对 service层进行 DI 依赖注入, service层和dao层 两者均在IOC容器里创建对象，功能层在Spring里面获取 service 和 dao 对象 实现功能
            
            ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
            UserService usImpl = (UserService) ac.getBean("usImpl");
            usImpl.hello();
    
    <img src="https://raw.githubusercontent.com/JiahuiZhu1998/Interview-Preparing/master/spring_pic1.png" alt="image1" width="900px" height="400px">
