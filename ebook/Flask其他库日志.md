Flask 其他的库
2021-08-10 17:44 更新
至此，我们只配置了应用自己建立的日志记录器。其它的库也可以记录它们。例如， SQLAlchemy 在它的核心中大量地使用日志。而在 logging 包中有一个方法 可以一次性配置所有的日志记录器，我不推荐使用它。可能存在一种情况，当你想 要在同一个 Python 解释器中并排运行多个独立的应用时，则不可能对它们的日志 记录器做不同的设置。

作为替代，我推荐你找出你有兴趣的日志记录器，用 getLogger() 函数来获取日志记录器，并且遍历它们来附加处理程序:

from logging import getLogger
loggers = [app.logger, getLogger('sqlalchemy'),
           getLogger('otherlibrary')]
for logger in loggers:
    logger.addHandler(mail_handler)
    logger.addHandler(file_handler)