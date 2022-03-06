这些过滤器在 Jinja2 中可用，也是 Jinja2 自带的过滤器:

tojson()
这个函数把给定的对象转换为 JSON 表示，如果你要动态生成 JavaScript 这里有 一个非常有用的例子。

注意 script 标签里的东西不应该被转义，因此如果你想在 script 标签里使用它， 请使用 |safe 来禁用转义，:

<script type=text/javascript>
    doSomethingWith({{ user.username|tojson|safe }});
</script>