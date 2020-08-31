# test_project
about codereview spider
data download from codereview.stackexchange.com


`answer-content`包括获取的回答文本内容。代码部分用`<code>`标签包裹，为便于后续解析此处保留xml格式。

`test_project`下是爬虫源代码。用到了scrapy框架。请求发起过多时导致429（请求过多）因此调整了`test_project>settings.py`中的`CONCURRENT_REQUESTS`。
- `spiders>testspider.py`：包括url处理和html页面的解析路径

- `pipelines.py`：处理数据的管道，处理完成后执行数据库操作

- `sqlutil.py`：数据库相关操作

- `settings.py`：配置文件 包括请求头中的USER_AGENT和PIPLINE模块的设置都在此处

- 其它都是框架自带





 