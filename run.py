print "hello"

first_part = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

div.gallery {
  margin: 5px;
  border: 1px solid #ccc;
  float: left;
  width: 200px;
  height: 200px;
  
}

div.gallery:hover {
  border: 1px solid #777;
}

div.gallery img {
	max-width: 100%;
  max-height: 100%;
  display: block;
}

div.desc {
  padding: 15px;
  text-align: center;
}
</style>
</head>
<body>

<h2>Capsler </h2>
<hr>
<br>

<div id="container">
</div></body><script>
var mybody = document.getElementById("container");
var images = [
'''

second_part = '''
];
var mytext = "<div class='gallery'><a target='_blank' href=''><img src='' width='600' height='400'></a></div>";


for(i=0;i<images.length;i++){

	mybody.innerHTML += "<div class='gallery'><a target='_blank' href='images/" + images[i] + "'><img src='images/" + images[i]+ "' width='600' height='400'></a></div>";
	
}
</script></html>
'''

'''
#open file
with open('index.html', 'a') as myFile:
	myFile.write(second_part)
'''

linelist = list()
filename = 'index.html'
with open(filename) as f:
	for line in f:
		linelist.append(line)
	
#burda bi yerde icerigi silelim
print linelist
	
	
with open('index.html', 'a') as myFile:
	myFile.write(first_part)
	
	for i in linelist:
		i = "'" + i.strip() + "'" +","
		myFile.write(i)
	
	myFile.write(second_part)










