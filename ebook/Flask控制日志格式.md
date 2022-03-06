Flask 控制日志格式
2021-08-10 17:43 更新
默认情况下，错误处理只会把消息字符串记录到文件或邮件发送给你。一个日志记 录应存储更多的信息，这使得配置你的日志记录器包含那些信息很重要，如此你会 对错误发生的原因，还有更重要的——错误在哪发生，有更好的了解。

格式可以从一个格式化字符串实例化。注意回溯（tracebacks）会被自动加入到日 志条目后，你不需要在日志格式的格式化字符串中这么做。

这里有一些配置实例:

邮件
from logging import Formatter
mail_handler.setFormatter(Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s

Message:

%(message)s
'''))
日志文件
from logging import Formatter
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
复杂日志格式
这里给出一个用于格式化字符串的格式变量列表。注意这个列表并不完整，完整的列 表请翻阅 logging 包的官方文档。

格式	描述
%(levelname)s	消息文本的记录等级 ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
%(pathname)s	发起日志记录调用的源文件的完整路径（如果可用）
%(filename)s	路径中的文件名部分
%(module)s	模块（文件名的名称部分）
%(funcName)s	包含日志调用的函数名
%(lineno)d	日志记录调用所在的源文件行的行号（如果可用）
%(asctime)s	LogRecord 创建时的人类可读的时间。默认情况下，格 式为 "2003-07-08 16:49:45,896" （逗号后的数字 时间的毫秒部分）。这可以通过继承 :class:~logging.Formatter，并 重载 formatTime() 改变。
%(message)s	记录的消息，视为 msg % args
如果你想深度定制日志格式，你可以继承 Formatter 。 Formatter 有三个需要关注的方法:

format():
处理实际上的格式。需要一个 LogRecord 对象作为参数，并
必须返回一个格式化字符串。
formatTime():
控制 asctime 格式。如果你需要不同的时间格式，可以重载这个函数。
formatException()
控制异常的格式。需要一个 exc_info 元组作为参数，并必须返 回一个字符串。默认的通常足够好，你不需要重载它。