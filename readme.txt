exercise里的learn_selenium4.py（要记住代码在自己电脑的路径，第6步有用）可以预约设备，如果想要在自己的电脑运行代码需要如下步骤：

1.安装python：在官网下载即可：https://www.python.org/downloads/windows/，
推荐安装3.7.3，之前没安装过可以参照安装教程
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000（记住自己的python安装在哪里，第6步用）

2.安装selenium：安装教程：https://www.cnblogs.com/sandysun/p/7838113.html

3.安装chrome浏览器：官网下载地址：https://www.google.cn/chrome/index.html

4.安装chromedriver：下载地址（注意选择相应的版本）：https://sites.google.com/a/chromium.org/chromedriver/，下载之后解压到一个自己能记住的文件夹里（记住完整的路径，第5步用）

5.修改代码：第5行的路径修改成自己的chromedriver路径，第53，54行修改成自己在仪器预约网站的名字和密码

6.定时运行python程序：https://cloud.tencent.com/developer/article/1200423，按照此教程把运行时间设置成00：00：01，learn_selenium4.py就会在那时自己运行啦！

PS：下载之后如果不知道能不能预约，可以试运行一下，把25行的路径里的"....../13.html"修改成"....../16.html"，就会自动预约x射线衍射仪，这样可以看看程序是否成功运行，（别忘了之后取消x射线的预约，再把代码改回去）。



为了学习爬虫，代码使用python语言。对于想要学习爬虫的同学，推荐这两本书：《Python编程：从入门到实践》、《Python网络爬虫从入门到实践》。
但是这两本书上有一些代码有点坑，比如作者用的是macOS，我们用的是win10等等。需要大家上网或者问问别人来避免代码无法运行。
练习爬虫的话，最好实践，只看书是不能学会爬虫的。

其实爬虫也是可以进阶的，不要拘泥于爬虫。以下是一些进阶方向：

1.多线程爬虫：书上的多线程讲的很浅，但是如果没学过《操作系统》，第一次可能会看不懂。可以看看：http://pages.cs.wisc.edu/~remzi/OSTEP/#book-chapters的第二大章：concurrency，那里讲了多线程的原理，我大概用了3周看了第二大章，之后多线程就容易理解了。

2.处理验证码：处理验证码可以用别人的代码，但是想要进一步了解的话，需要一点点计算机视觉的知识（很少），如果对计算机视觉感兴趣的话，可以慢慢入门计算机视觉。不妨从《数字图像处理》开始，一点一点学习，每学期学一门课。

3.从python入门：如果爬虫之后对计算机更有兴趣了，可以从python入门学习cs61a，上网就能搜到，一门非常棒的课程，加深对计算机的理解。