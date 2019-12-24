#########################################################################
# File Name: setup.sh
# Created Time: 2018年07月27日 星期五 10时25分24秒
#########################################################################
#!/bin/bash


function proxy() {

	export http_proxy=http://lw.taobao.com:102/
	export HTTP_PROXY=http://lw.taobao.com:102/
	export ftp_proxy=http://lw.taobao.com:102
	export all_proxy=http://lw.taobao.com:102
	export rsync_proxy=http://lw.taobao.com:102
	export https_proxy=http://lw.taobao.com:102/
	export HTTPS_PROXY=http://lw.taobao.com:102/
	export no_proxy=localhost,127.0.0.1,localaddress,.localdomain.com,10.*,192.168.*
}


function network() {
	echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

}


proxy
#network
