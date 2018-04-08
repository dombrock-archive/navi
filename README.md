# Navi [ALPHA]

## A minimal navigation generator script for static sites written in Python3.

1.) Place your static web files in the "web" directory (or change the "web_root" variable to point to another directory).

2.) Modify each page to contain the html ```<navigation>navigation<navigation>``` in the location that you want the navigation to be generated.

3.) Edit the "pages" dictionary in "navi/page_list.py" to contain your page names and locations (each page must be added here manually for security). Use the Python syntax ```pages.update({"Page ID (Name/Title)":"path/to/file.html"})``` to add a new page where the KEY is the page ID (the link text as a string) and the VALUE is the file location as a sting. **NOTE:** the ```web_root``` is automatically prepended to the path. This script assumes that all files that it needs to work with are in ```web_root```.  

4.) Edit "navi/nav-template.html" to suit your needs. This is the template file that will be used to generate the navigation on all of your pages. You can use any HTML/CSS/JS here that you need. Use the syntax: ```{{Page ID}}``` to specify where each link should go in the layout. The rest will be automated. 

5.) Run "navi/navi.py" from the CLI to replace the pages. Something like ```python3 navi.py```.
