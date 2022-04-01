#!/usr/bin/bash
# author：yyr

cd /etc/yum.repos.d
# wget https://zeroc.com/download/rpm/zeroc-ice-el6.repo
wget https://zeroc.com/download/Ice/3.7/el7/zeroc-ice3.7.repo
yum install -y ice-all-runtime ice-all-devel
icebox -v
# 卸载
# yum remove -y ice*