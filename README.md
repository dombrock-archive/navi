1.) Place your static web files in the "web" directory (or change the code to point to another directory)
2.) Insert the html ```<navigation>navigation<navigation>``` into each page that you want to contain the new navigation
3.) Edit the "pages" dictionary to contain your page names and locations (each page must be added here manually for security)
4.) Edit nav-template.html to suit your needs. This is a the template file that will be used to generate the navigation on all of your pages. Use the syntax: 
```{{Page ID}}``` to tell specify where each link should go in the layout. The rest will be automated. 
5.) Run "nav.py" from the cli to replace the pages.