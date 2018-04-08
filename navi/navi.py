import page_list
import config
import os, sys
def Navigation():
	print(">>Generating Navigation<<")
	global config
	#goes through each page and replaces the marked section with the new navigation  html
	nav_template = open("nav-template.html", 'r').read()
	for nav_id, location in page_list.pages.items():
		print(nav_id+" | "+location)
		if nav_id != "NULL":
			nav_template = nav_template.replace("{{"+nav_id+"}}", "<a href='"+config.url+location+"'>"+nav_id+"</a>")
		else:
			print("Skipping Gen due to NULL ID for "+location)
	return nav_template

def Replace(filename, replacement):
	global config
	#replaces the actual html with the new navigation
	test = open(config.web_root+filename, 'r').read()
	tests = test.split("<navigation>")
	tests[1]=replacement
	new = "<navigation>".join(tests)
	return(new)

nav = Navigation()
print(">>Starting Write<<")
for nav_id, location in page_list.pages.items():
	print("WRITING: "+nav_id+" | "+location)
	parts = os.path.split(config.output+location)
	if not os.path.isdir(parts[0]):
		os.mkdir(parts[0])
	file = open(config.output+location, 'w')
	file.write(Replace(location,nav))
	#print(Replace(location,nav))
