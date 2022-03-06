自动转义的概念是自动转义特殊字符。 HTML （或 XML ，因此也有 XHTML ）意义下 的特殊字符是 & ， > ， < ， " 以及 ' 。因为这些字符在 文档中表示它们特定的含义，如果你想在文本中使用它们，应该把它们替换成相应
的“实体”。不这么做不仅会导致用户疲于在文本中使用这些字符，也会导致安全问题。 （见 跨站脚本攻击（XSS） ）

虽然你有时会需要在模板中禁用自动转义，比如在页面中显式地插入 HTML ， 可以是一个来自于 markdown 到 HTML 转换器的安全输出。

我们有三种可行的解决方案:

在传递到模板之前，用 Markup 对象封装 HTML字符串。一般推荐这个方法。 在模板中，使用 |safe 过滤器显式地标记一个字符串为安全的 HTML （ {{ myvariable|safe }} ）。 临时地完全禁用自动转义系统。
在模板中禁用自动转义系统，可以使用 {%autoescape %} 块:

{% autoescape false %}
<p>autoescaping is disabled here
<p>{{ will_not_be_escaped }} {% endautoescape %} 无论何时，都请务必格外小心这里的变量。