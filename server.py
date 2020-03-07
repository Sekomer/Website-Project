import os

from bottle import route, run, default_app, debug, static_file, request, Bottle
from hashlib import sha256

def hashed_pw(password):
	return sha256(password.encode()).hexdigest()
test_hash = "334156449b80305d5bc4cc3ba03e35bde50394594355d119b316acfc93b9df87"

ipaddresses = []
counter = []
comments = []

def indexpage(table):
	index = """<!DOCTYPE html>

<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" type="text/css" href="/css/style.css">
  <title>Aureliano Russo</title>
</head>

<body
  style="background: url(/images/background.jpg) ; background-size: 100% 100%;">
  <div class="fiction">
    <p>The contents in this page are fictional and are not related to a person or establishment.</p>
  </div>
  <div class="header">
    <h1>Aureliano Russo</h1>

  </div>

  <div class="navbar">

    <a href="index.html" class="active">Me</a>
    <a href="resume.html">Life</a>
    <a href="education.html">Education</a>
    <a href="hobbies.html">Hobbies</a>

  </div>

  <div class="row">
    <div class="leftcolumn">
      <div class="card" style="margin-top:50px;">
        <h2>About me</h2>

        <p>Hi I am Aureliano Russo. I am a Software Engineer. I am currently living on Mars. I own the Intersteller
          Colonization Company. I am the first quintillioner of the Milkyway Galaxy. I was born in 1999 and was
          cryogenicly frozen in 2053 until the discovery of the synthetic organs replacement, which was in 2398.</p>
        <img class="images" src="/images/selfie.jpeg" alt="me-at-my-colony">
        <p>When I was at Mars Union Colony for my researches.</p>
      </div>

    </div>
    <div class="rightcolumn">
      <div class="card" style="margin-top:85px;">
        <h2>My colony</h2>

        <img class="images" src="/images/colony.jpeg" alt="mars-colony">
        <p>A picture of my colony.</p>

      </div>
    </div>
  </div>




  <div class="footer"><div id="contact">
    <h2>Contact</h2>

    <ol>
      <li>Mail
        <ul>
          <li>quintillionsandnukes@spacemail.ar</li>
          <li>aurelianorusso@itu.edu.tr</li>
        </ul>
      </li>
      <li>Address
        <ul>
          <li>Mars Address: Cida Street, No:1C Aureliano Russo Space Center, Tharsis Rise, Mars, Solar System
            (#3b1bexurb1a)
            Milky Way</li>
          <li>Earth Address: Ayazağa Kampüsü 34469
              Maslak-ISTANBUL/TURKEY</li>
        </ul>
      </li>
      <li>Phone
        <ul>
          <li>+04+04#C#28772(Tharsis Rise, Mars)</li>
          <li>+905320000000(TURKEY,Earth)</li>
        </ul>
      </li>

    </ol>
  </div>
  <div id="logo">
    <img class="images" src="/images/logo.png" alt="my-logo">
  </div>
  </div>
  <table>
	<tr>
		<th>IP</th>
		<th>Counter</th>
	</tr>
	%s
  </table>
  <form action="/action.html" method="POST">
  Password: <input type="password" name="password">
  <input type="submit" value="Clear ip table">
  </form>
  <form action="/comments" method="POST">
	Comment: <input type="text" name="entered_comment" />
	Password: <input type="password" name="password" />
	Did you like my page?<select name="likeoption">
		<option value="1">Yes</option>
		<option value="2">No</option>
	</select>
	   <input type="submit" value="Submit" />
	</form>
</body>
</html>"""%(table)
	return index

def ipcounter():
	ip = request.headers.get("X-Forwarded-For","127.0.0.1")
	if ip in ipaddresses:
		counter[ipaddresses.index(ip)] += 1
	else:
		ipaddresses.append(ip)
		counter.append(1)
		
	string = """"""
	x = 0
	for i in ipaddresses:
		string = string + """<tr><td>""" + str(ipaddresses[x]) + """</td><td>""" + str(counter[x]) + """</td></tr>"""
		x+=1
	homepage = indexpage(string)
	return homepage

def actionpage():
	password = request.forms.get("password")
	hash = hashed_pw(password)
	if hash == test_hash:
		del ipaddresses[:]
		del counter[:]
		return template("<p>Access granted,correct password</p>")
	else:
		return template("<p>Access denied,wrong password</p>")

def template(string):
	mypage = """<!DOCTYPE html>

<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" type="text/css" href="/css/style.css">
  <title>Aureliano Russo</title>
</head>

<body style="background: url(/images/background.jpg) ; background-size: 100% 100%;">
%s
<a href="index.html">Home page</a>
</body>
</html>"""%(string)
	return mypage
	
def listToString(s):
	str1 = ""
	for i in s:
		str1 += i
	return str1
	
def commentpage():
	password = request.forms.get("password")
	comment = request.forms.get("entered_comment")
	like = request.forms.get("likeoption")
	hash = hashed_pw(password)
	if hash == test_hash:
		global comments
		comments += comment
		if like == 1:
			str2 = listToString(comments)
			return template(str2 + "<p>thank you</p>")
		else:
			str2 = listToString(comments)
			return template(str2 + "<p>Thanks.</p>")
	else:
		return template("wrong password")

def resumepage():
	resume = """<!DOCTYPE html>

<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" type="text/css" href="/css/style.css">
  <title>Aureliano Russo</title>
</head>

<body
  style="background: url(/images/background.jpg) ; background-size: 100% 100%;">
  <div class="fiction">
    <p>The contents in this page are fictional and are not related to a person or establishment.</p>
  </div>
  <div class="header">
    <h1>Aureliano Russo</h1>

  </div>

  <div class="navbar">

    <a href="index.html" >Me</a>
    <a href="resume.html" class="active">Life</a>
    <a href="education.html">Education</a>
    <a href="hobbies.html">Hobbies</a>

  </div>

  <div class="row">
    <div class="leftcolumn">
      <div class="card" style="margin-top:150px;">
        <h2>My Life</h2>
        <p>I was born in Earth on 4 April, 1999. I was a very hyperactive and curious boy whose conducting experiments
          on everything I could. In my school years I was successful even though I didn’t like school and didn’t study
          for it. After high school I studied Computer Engineering at ITU which changed my life completely. I had a
          great college life and I got double major in physics(i love physics and math). After master, phd etc. Me and
          my cousin started up a software company. Our company did well then we changed our route to our true passion,
          space. First we started affordable space traveling. Then we established our space city on “Tharsis Rise”. Our
          company grew steadily. We opened thousands of departments in our company and became worlds first
          quadrillionaires. Our scientists discovered cryogenic freezing and I had my body frozen until I opened my eyes
          in Ceres, on 1st of January, 2397. Our company had reached quintillions while I was cryogenically frozen. They
          had discovered synthetic organs and telomerese technology and the people would not die anymore. After all of
          these , I started to create living holograms in a tiny universe that I created. In the year 3019, I completed
          my project. In this simulated universe I created everything about Earth in 2019, as you understand all of the
          world. I gave people emotions, they weren’t machine codes at all. Then one day I came up with an idea. I
          wanted to tell them what I had achieved. I settled on an assignment homework. Then I chose a kid. I whispered
          this idea in his ear. If you're reading his text, you're probably living in a simulation.</p>

      </div>
    </div>
    <div class="rightcolumn">
      <div class="card">
        <h2>My Projects</h2>
        <table style="width:100%">
            <tr>
              <th>Name</th>
              <th>Year</th> 
              <th>Description</th>
            </tr>
            <tr>
              <td>Website Design</td>
              <td>2019</td> 
              <td>I designed my personal web-page including my future</td>
            </tr>
            <tr>
              <td>Time Travel</td>
              <td>N/A</td> 
              <td>Travelling in time</td>
            </tr>
            <tr>
                <td>AI Person Bot</td>
                <td>2401</td> 
                <td>Injected my brain to an AI, making myself immortal</td>
              </tr>
          </table>

        

      </div>
    </div>
  </div>




  <div class="footer"><div id="contact">
      <h2>Contact</h2>
  
      <ol>
        <li>Mail
          <ul>
            <li>quintillionsandnukes@spacemail.ar</li>
            <li>aurelianorusso@itu.edu.tr</li>
          </ul>
        </li>
        <li>Address
          <ul>
            <li>Mars Address: Cida Street, No:1C Aureliano Russo Space Center, Tharsis Rise, Mars, Solar System
              (#3b1bexurb1a)
              Milky Way</li>
            <li>Earth Address: Ayazağa Kampüsü 34469
                Maslak-ISTANBUL/TURKEY</li>
          </ul>
        </li>
        <li>Phone
          <ul>
            <li>+04+04#C#28772(Tharsis Rise, Mars)</li>
            <li>+905320000000(TURKEY,Earth)</li>
          </ul>
        </li>
  
      </ol>
    </div>
    <div id="logo">
      <img class="images" src="/images/logo.png" alt="my-logo">
    </div>
    </div>
</body>

</html>"""
	return resume
	
def hobbiespage():
	hobbies = """<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Aureliano Russo</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/hobbies.css">
</head>
<body
  style="background: url(/images/background.jpg) ; background-size: 100% 100%;">
  <div class="fiction">
    <p>The contents in this page are fictional and are not related to a person or establishment.</p>
  </div>
<div class="header">
  <h1>Aureliano Russo</h1>
</div>

<div class="navbar">
  <a href="index.html" >Me</a>
  <a href="resume.html">Life</a>
  <a href="education.html">Education</a>
  <a href="hobbies.html" class="active" >Hobbies</a>
</div>

<div class="row">
  <div class="leftColHob">
    <div class="card" style="margin-top:50px;">
      
      <ul style="list-style: none;">
        <li><h2>Regular Hobbies</h2></li>
      </ul>
      
      <ul style="list-style: none;">
        <li>Playing guitar</li>
        <li>Listening to music.</li>
        <li>Making the best websites in Mars.</li>
        <li>Reading articles.</li>
        <li>Watching sunset in Mars.</li>
      </ul>

    </div>
  </div>

  <div class="rightColHob">
    <div class="card" style="margin-top:50px;">
      <h2>Making Magic Shows</h2>
      <p>Some films and magicians affected me deeply and I started making magic!</p>
    </div>
  </div>

  <div class="leftColHob">
    <div class="card" style="margin-top:50px;">
      <h2>Space Traveling</h2>
      <p>Its nice when you are traveling at 1/3 of lightspeed.</p>
    </div>
  </div>

  <div class="rightColHob">
    <div class="card" style="margin-top:50px;">
      <h2>Sending Nukes to Kuiper Belt</h2>
      <p>Its nice to watch them blowing up when you are angry.</p>
    </div>
  </div>

  <div class="leftColHob">
    <div class="card" style="margin-top:50px;">
      <h2>Being Immortal</h2>
      <p>Its just awesome!</p>
    </div>
  </div>



</div>

<div class="footer"><div id="contact">
  <h2>Contact</h2>

  <ol>
    <li>Mail
      <ul>
        <li>quintillionsandnukes@spacemail.ar</li>
        <li>aurelianorusso@itu.edu.tr</li>
      </ul>
    </li>
    <li>Address
      <ul>
        <li>Mars Address: Cida Street, No:1C Aureliano Russo Space Center, Tharsis Rise, Mars, Solar System
          (#3b1bexurb1a)
          Milky Way</li>
        <li>Earth Address: Ayazağa Kampüsü 34469
            Maslak-ISTANBUL/TURKEY</li>
      </ul>
    </li>
    <li>Phone
      <ul>
        <li>+04+04#C#28772(Tharsis Rise, Mars)</li>
        <li>+905320000000(TURKEY,Earth)</li>
      </ul>
    </li>

  </ol>
</div>
<div id="logo">
  <img class="images" src="/images/logo.png" alt="my-logo">
</div>
</div>

</body>
</html>"""
	return hobbies
	
def educationpage():
	education = """<!DOCTYPE html>
<html lang="en">
    
<head>
    <meta charset="UTF-8">
    <title>Aureliano Russo</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
    <link rel="stylesheet" type="text/css" href="/css/education.css">
</head>

<body
  style="background: url(/images/background.jpg) ; background-size: 100% 100%;">
  <div class="fiction">
    <p>The contents in this page are fictional and are not related to a person or establishment.</p>
  </div>
<div class="header">
  <h1>Aureliano Russo</h1>
</div>

<div class="navbar">
  <a href="index.html" >Me</a>
  <a href="resume.html">Life</a>
  <a href="education.html" class="active">Education</a>
  <a href="hobbies.html">Hobbies</a>
</div>

<div class="row">
  <div class="leftColEdu">
    <div class="card">
      <h2>Haydarpasa Lisesi</h2>
      <h5>High School Education</h5>
      <img class="images" src="/images/haydarpasa.jpg" alt="photo-of-haydarpasa">
      <p>I graduated with the score of 100 out of 100 from my high school, Haydarpasa High School, in 2018.</p>
    </div>
  </div>

  <div class="rightColEdu">
    <div class="card">
      <h2>ITU Computer Engineering and Physics</h2>
      <h5>College Education</h5>
      <img class="images" src="/images/itu.jpg" alt="photo-of-itu">
      <p>I studied Computer Engineering in ITU. Since I love physics, I did a double major with physics and graduated with a score of 3.98/4.00 in 2022.</p>
    </div>
  </div>

  <div class="leftColEdu">
    <div class="card">
      <h2>MIT, Quantum Computing</h2>
      <h5>Master's Degree</h5>
      <img class="images" src="/images/mit.jpg" alt="photo-of-mit">
      <p>I got accepted to MIT, for the Quantum Computing Master's program. I wrote many theses during my masters program. Meanwhile me and my cousin were also thinking to start a software company.</p>
    </div>
  </div>

  <div class="rightColEdu">
    <div class="card">
      <h2>Caltech, Quantum Computing and Algorithms</h2>
      <h5>PhD Degree</h5>
      <img class="images" src="/images/caltech.jpg" alt="photo-of-caltech">
      <p>After my masters degree, I got accepted to Caltech in the area of Quantum Computing and Algorithms. I also studied on astrophysics during my PhD. After my PhD is complete, we founded the Interstellar Colonization Company.</p>
    </div>
  </div>
</div>

<div class="footer"><div id="contact">
  <h2>Contact</h2>

  <ol>
    <li>Mail
      <ul>
        <li>quintillionsandnukes@spacemail.ar</li>
        <li>aurelianorusso@itu.edu.tr</li>
      </ul>
    </li>
    <li>Address
      <ul>
        <li>Mars Address: Cida Street, No:1C Aureliano Russo Space Center, Tharsis Rise, Mars, Solar System
          (#3b1bexurb1a)
          Milky Way</li>
        <li>Earth Address: Ayazağa Kampüsü 34469
            Maslak-ISTANBUL/TURKEY</li>
      </ul>
    </li>
    <li>Phone
      <ul>
        <li>+04+04#C#28772(Tharsis Rise, Mars)</li>
        <li>+905320000000(TURKEY,Earth)</li>
      </ul>
    </li>

  </ol>
</div>
<div id="logo">
  <img class="images" src="/images/logo.png" alt="my-logo">
</div>
</div>

</body>
</html>"""
	return education

def css(cpath):
	return static_file(cpath, root="./css")

def img(path):
	return static_file(path, root="./images")
	
def create_app():
	app = Bottle()
	app.route('/', 'GET', ipcounter)
	app.route('/index.html', 'GET', ipcounter)
	app.route('/resume.html', 'GET', resumepage)
	app.route('/hobbies.html', 'GET', hobbiespage)
	app.route('/education.html', 'GET', educationpage)
	app.route('/action.html', 'POST', actionpage)
	app.route('/comments','POST', commentpage)
	app.route('/images/<path>', 'GET', img)
	app.route('/css/<cpath>', 'GET' , css)
	return app
	
application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))



