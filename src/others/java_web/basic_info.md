# Back

## Contents

- job process

    1、打包本地测试通过后再放入测试环境，修改与最新更新

    2、数据，数据准备与数据备份

    3、修改系统关键配置文件，做数据迁移

- details

    1、System.currentTimeMillis()

    2、String content = new String(file.getBytes(),"utf-8")
        文件一般转化为byte[]类型的，再转String类型，split ——> String[]

    3、jsonString : "[{supplierId:'',supplierName:'',goodsId:'',goodsName:''}]"
        使用 JSON.parseObject(jsonString, Object.class);
        转为 对象Object类型，这里的Object为A、B等model类型

    4、spring框架util包中的StringUtils类主要是处理关于字符串的功能方法
        判断字符串是否为空，如果为nul或者""则返回true，否则返回false
        注意字符串可以有null和""两种empty状态，str == null || "".equals(str)

        ps可以多看看这个类下的其他方法

    5、Collection的基础，多想象，回顾：List(get(0)+add) + 后续处理方式，set，ArrayList，没有Map（回顾方法 get(key)+put++）
    ，更没有Array

    6、使用splitter方法把string转换为list,其中以#做分割
        Splitter.on("#").splitToList()

    7、Shiro
        //login
        import org.apache.shiro.SecurityUtils;
        import org.apache.shiro.authc.*;
        import org.apache.shiro.authz.UnauthorizedException;
        import org.apache.shiro.subject.Subject;
        UsernamePasswordToken token = new UsernamePasswordToken(userName, password);
        subject.login(token);
        if (subject.isAuthenticated()) {
            return "redirect:/";
        } else {
            return "login";
        }
        SecurityUtils.getSubject().logout()注销

    8、java爬虫，具体可见http://blog.csdn.net/jibaole/article/details/52212886

    9、private final static String charset = "UTF-8";
       mysql中charset是UTF8 网页编码
       HttpUtils.getCharSet(content);HTML 标签的 charset 属性，这个是可以获取的

    10、.contains在不清楚，可以使用这个

    11、Tika的API十分便捷，核心是Parser interface，其中定义了一个parse方法：
        public void parse(InputStream stream, ContentHandler handler, Metadata metadata)
        用stream参数传递需要解析的文件流， 文本内容会被传入handler，而元数据会更新至metadata
        使用这个工具进行文本分析

    12、static{}语句块：http://blog.csdn.net/newjerryj/article/details/8650268

    13、static 修饰变量 allFilesPath 统一的，多次使用

    14、File类：http://www.cnblogs.com/alsf/p/5746480.html

    15、文件的读取涉及的类：别忘了Stream

- structure

    1、Tools/Constants
        public final static String/int + UpperCase

    2、user tools parser feature Controller

    3、

- thought
  if这种的需要思维训练变成一个数学图