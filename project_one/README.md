### project one 

#### 项目介绍
* 这是一个demo

#### 运行部署方式（环境依赖等）
* Python版本 3.7
* 所需依赖 ./requirements.txt

#### 工程结构（各模块功能）
* src： 业务代码
    * general模块： 封装当前项目对其他项目的接口依赖
    * item模块： 功能
        * views.py： 定义接口
        * serializers.py： 定义请求body和response data数据校验
        * filters.py： 定义查询校验
        * services.py： 核心业务逻辑
        * storages.py： 实现存储方案
        * modes.py： 存储模型
    * user模块： 功能
    * ping模块： 功能
    * config.py： 配置
    * manage.py： 启动类
* Dockerfile
* README.md
* requirements.txt


#### 技术文档语雀地址

#### 接口文档yapi地址
