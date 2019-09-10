import time,sys
def run(arg,waktu):
	for h in arg+"\n":
		sys.stdout.write(h)
		sys.stdout.flush()
		time.sleep(waktu)
if __name__ == '__main__':
	run("\033[33m[#] Mengecek Module ( checking module )",0.1)
