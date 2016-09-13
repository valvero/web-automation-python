#response = input("Please enter your name: ")
#print(response)
#response = input("Press any key to continue.")
#python -m pip install SomePackage
#print("This link is ok: %s" % link)
import requests
import threading
import os
from joblib import Parallel, delayed
import multiprocessing
import time

lock = threading.Lock()

def url_ok(url):
	url = url.rstrip()
	r = requests.get(url)
	return r.status_code == 200

def processInput(link):
	global lock
	#link = link.replace("www.","me.")
	if(url_ok(link)):
		with lock:
			# with open("success.txt", "a") as myfile:
				# myfile.write("{}".format(link))
			print("LINK OK - {}".format(link))
	else:
		with lock:
			with open("failed.txt", "a") as myfile:
				myfile.write("{}".format(link))
			print("LINK OK - {}".format(link))

if __name__ == '__main__':
	#os.remove("success.txt")
	#os.remove("failed.txt")
	with open('AwardsUrls.txt') as f:
		inputs = f.readlines()
	num_cores = multiprocessing.cpu_count()*3
	start = time.time()
	Parallel(n_jobs=num_cores, backend="threading")(delayed(processInput)(i) for i in inputs)
	end = time.time()
	elapsed_time = end - start
	print(elapsed_time)
	
	
	
	
	
	
	
	
### single threaded 
# with open('links.txt') as f:
	# content = f.readlines()

# for link in content:
	# if(url_ok(link)):
		# with open("success.txt", "a") as myfile:
			# myfile.write("{}".format(link))
		# print("link ok: %s" % link)
	# else:
		# with open("failedurls.txt", "a") as myfile:
			# myfile.write("{}".format(link))
		# print("link fail: %s" % link)