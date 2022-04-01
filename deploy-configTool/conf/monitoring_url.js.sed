function setURL(){
    var globalConfig = {
        monitoring_IP : "{{.monitoringIP}}",
        monitoring_port: {{.monitoringPort}},
    }
    return globalConfig;
}
