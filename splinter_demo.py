from splinter import Browser

# use 'global' keyword to access a global variable (see link checker)

executable_path = {'executable_path':'c:\chromedriver.exe'}
browser = Browser('chrome', **executable_path)


def demo():
	# Visit URL
	global browser
	url = "http://www.google.com"
	browser.visit(url)
	browser.fill('q', 'splinter - python acceptance testing for web applications')
	# Find and click the 'search' button
	button = browser.find_by_name('btnG')
	# Interact with elements
	button.click()
	if browser.is_text_present('splinter.readthedocs.io'):
		print("Yes, the official website was found!")
	else:
		print("No, it wasn't found... We need to improve our SEO techniques")

def kbbHomePage():
	global browser
	url = "http://horriblesubs.info/"
	browser.visit(url)
	#$('#parent_id').children(':not(#id_n)').remove();entry-content
	browser.execute_script("var p = document.getElementById('wrapper'); var d = document.getElementsByClassName('entry-content')[0]; p.innerHTML = '';p.appendChild(d);");
	#print(browser.evaluate_script("$('#parent_id').children(':not(#id_n)').remove();"))
	
kbbHomePage()
		