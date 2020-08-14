# 修订记录
```
1. 2020-08-13 @王启航 添加了项目，增加了烘丝模型的reset控制
```

# 软件环境
```
Python>=3.X
flask==1.1.2
```

# 项目说明
本项目提供了一个REST Ful的API（端口8888），主要提供机器学习反向控制的恢复流程(reset)

因为存在测试环境，生产环境等，所以首先定义了如下的配置
```
class Environment:
    TEST = 'test'  # 输出到物理测试点位
    PROD = 'prod'  # 输出到生产环境点位
    NONE = 'none'  # 不输出到任何点位
```
在进行reset的操作的时候，需要携带 environment 字段。


`PythonDeviceControlLib`这个文件夹为IoT同事提供的包，如有疑问请移步。


# 规范
各个模型的接口都以`/api/模型名字/操作`来进行命名。比如 `/api/hs/reset`。


然后可以自己在`model`文件夹里面写自己的业务逻辑，不要都写在 `app.py` 这个controller里面
