# Jangan Di Recode Yaa Bossq :)
# Tools Ini Hanya Untuk Pembelajaran Saja :)
#===========================================
# Author : BL4CK DR460N
# Type : bash
# name : Get Token Facebook
# Team : Woll Cyber Team
cd data
trap ctrl_c INT
ctrl_c() {
echo "\033[31;1m CTRL + C Terdeteksi"
sleep 4
echo "\033[32;1m Keluar Dari Program"
exit
}
python2 logo.py
echo
if [ -z $1 ]; then
	echo "\033[31;1mbash $1 <username> <password>"
	exit
elif [ -z $2 ]; then
	echo "\033[31;1mbash $1 <username> <password>"
	exit
else
	python2 cek_module.py
	if [ -d /data/data/com.termux/files/usr/lib/python2.7/site-packages/requests ]; then
	        echo "\033[32;1m[+] 'requests' terinstall ( installed )"
		sleep 4
		python2 get.py $1 $2
	else
        	echo "\033[31;1m[-] 'requests' belum di install ( not installed )"
	        read -p "\033[37;1m[=] enter untuk menginstall ( to install ) " b
 	      	pip2 install requests
	        sh $0
	fi
#	python2 get.py $1 $2
fi
