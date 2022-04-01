# 基础镜像
FROM python:2.7
# 作者
MAINTAINER yuanyr <398916756@qq.com>

RUN mkdir -p /code/tool
COPY configTool /code/tool
COPY requirements.txt /code/tool
RUN pip install -r /code/tool/requirements.txt
# CMD python /code/tool/configTool/data.py
ENTRYPOINT [ "python" ]
CMD [ "/code/tool/configTool/data.py" ] 
