# Jangan Di Recode Yaa Bossq :)
# Tools Ini Hanya Untuk Pembelajaran Saja :)
#===========================================
# Author : BL4CK DR460N
# Type : bash
# name : Get Token Facebook
# Team : Woll Cyber Team
import requests,json,sys,time,os
def run(arg,waktu):
	for b in arg+"\n":
		sys.stdout.write(b)
		sys.stdout.flush()
		time.sleep(waktu)
#class cek:
def main(u,p):
	os.system('python2 logo.py')
	print ("")
	run("\033[33m[+] Sedang Mengambil Token ( gettings token ) ",0.1)
	try:
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+u+"&locale=en_US&password="+p+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		r = requests.get(url).text
		j = json.loads(r)
#		error = j['error_msg']
		if 'access_token' in j:
			run("\033[32m[+] \033[37mSukses Login ( Success Login )",0.2)			
			print ("")
			print ("\033[34m[*] Access Token Kamu ( Your Access Token )\n\033[32m[\033[35m>\033[32m] \033[36m"+j['access_token'])
			sys.exit()
		elif 'www.facebook.com' in j["error_msg"]:
			run("\033[32m[+] \033[37mSukses Login ( Success Login )",0.2)
			print ("\033[33m[*] Akun Kena Sesi ( Account Checkpoint )")
			sys.exit()
		else:
			print ("\033[31m[*] Login Gagal ( Login Failed )")
			sys.exit()
	except requests.exceptions.ConnectionError:
		print ("\033[31m[!] Tidak Ada Koneksi ( No Connection )")
		sys.exit()
#if __name__ == '__main_':
#	print ("bd")
if len(sys.argv) < 2:
	print ("\033[31m[ERROR]: \033[37m"+sys.argv[0]+" <username> <password>")
	sys.exit()
else:
	main(sys.argv[1],sys.argv[2])
