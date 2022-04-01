include Makefile.inc

all:clean mv build run

pip:
	@${py}/get-pip.py

build:
	@${SCRIPTS}/build-tool.sh

run:
	@${SCRIPTS}/run-tool.sh

cp: 
	@find ${CONFIG_DIR} -type f -name "*.sed" | sed s?".sed"?""?g | xargs -I {} cp {}.sed {}

sed:
	@find ${CONFIG_DIR} -type f -name "monitoring_url.js" | xargs sed -i s?"{{.monitoringIP}}"?"${monitoringIP}"?g
	@find ${CONFIG_DIR} -type f -name "monitoring_url.js" | xargs sed -i s?"{{.monitoringPort}}"?"${monitoringPort}"?g
	@find ${CONFIG_DIR} -type f -name "iceConfig.py" | xargs sed -i s?"{{.iceIP}}"?"${iceIP}"?g
	@find ${CONFIG_DIR} -type f -name "iceConfig.py" | xargs sed -i s?"{{.icePort}}"?"${icePort}"?g
	
mv:cp sed
	@${SCRIPTS}/mv.sh

# 删除configtool容器
delct:
	-@docker stop ${Cct_NAME}
	-@docker rm ${Cct_NAME}

clean:delct
	-@rm -f ${CONFIG_DIR}/monitoring_url.js
	-@rm -f ${CONFIG_DIR}/iceConfig.py
	-@rm -f ${ConfigTool_js_DIR}/monitoring_url.js
	-@rm -f ${ConfigTool_DIR}/iceConfig.py