import page_list

#where are the files that we are manipulating?
web_root = "../web/"

output = "OUTPUT/"

def Navigation():
	#goes through each page and replaces the marked section with the new navigation  html
	nav_template = open("nav-template.html", 'r').read()
	for nav_id, location in page_list.pages.items():
		print(nav_id+" | "+location)
		if nav_id != "NULL":
			nav_template = nav_template.replace("{{"+nav_id+"}}", "<a href='"+location+"'>"+nav_id+"</a>")
		else:
			print("Skipping Gen due to NULL ID for "+location)
	return nav_template

def Replace(filename, replacement):
	#replaces the actual html with the new navigation
	test = open(web_root+filename, 'r').read()
	tests = test.split("<navigation>")
	tests[1]=replacement
	new = "<navigation>".join(tests)
	return(new)

nav = Navigation()

for nav_id, location in page_list.pages.items():
	file = open(output+location, 'w')
	file.write(Replace(location,nav))
	print(Replace(location,nav))
