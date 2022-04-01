### 配置工具部署说明

1. 到 github 克隆程序源码
``` bash
git clone --depth=1 https://github.com/yuanyaru/deploy-configTool.git
```
2.根据实际情况修改 监控界面 和 ice接口 对应的 IP、port
``` bash
cd /usr/dynas/deploy-configTool
vim Makefile.inc
```
3.安装 docker，如果已安装，跳过此步骤
``` bash
cd /usr/dynas/deploy-configTool/scripts
./docker_install.sh
```
4.启动程序
``` bash
cd /usr/dynas/deploy-configTool
make pip
make
```
稍等片刻，看到程序成功启动，Ctrl+c关闭即可。

5. 验证
``` bash
[root@localhost deploy-configTool]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
48279a1aa533        configtool          "python /code/tool/c…"   10 minutes ago      Up 9 minutes        0.0.0.0:5000->5000/tcp              configtool
```
看到容器启动，则完成配置工具的部署。
通过浏览器访问ip:5000 进入配置页面。(访问之前，先启动服务端程序，否则无法访问。)