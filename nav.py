#where are the files that we are manipulating?
web_root = "web/"

#dict of navigation IDs and actual page location on the server
#used for generating (filling in) the navigation template and also to rewrite the page html
pages = {}
pages.update({"test":"test.html"})
pages.update({"Some Page":"somePage.html"})


def Navigation():
	#goes through each page and replaces the marked section with the new navigation  html
	nav_template = open("nav-template.html", 'r').read()
	for nav_id, location in pages.items():
		print(nav_id+" | "+location)
		nav_template = nav_template.replace("{{"+nav_id+"}}", "<a href='"+location+"'>"+nav_id+"</a>")
	return nav_template

def Replace(filename, replacement):
	#replaces the actual html with the new navigation
	test = open(web_root+filename, 'r').read()
	tests = test.split("<navigation>")
	tests[1]=replacement
	new = "<navigation>".join(tests)
	return(new)

nav = Navigation()

for nav_id, location in pages.items():
	print(Replace(location,nav))
