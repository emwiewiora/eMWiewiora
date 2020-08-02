import requests, json, random

f = open("./README.md", "w")
pokemon_id = random.randint(1, 151)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''<img align="right" src="{result['sprites']['front_default']}" width="100" height="100">
<p>I am currently learning FullStack part time, in hopes to change my career.</p>
<h2>🌱 I’m currently learning ...</h2>
<ol>
    <li>1. More indepth HTML</li>
    <li>2. More indepth CSS</li>
    <li>3. The basics of JavaScript</li>
</ol>

<h2>🔭 I’m currently working on ...</h2>
<ol>
    <li>1. see what i am playing with in codepen.io <a target="_blank" href="https://codepen.io/emwiewiora">here</a></li>
    <li>2. I have started <a href="https://www.theodinproject.com/">The Odin Project</a></li>
</ol>
<p>This page is a work in progress.</p>

<p>Thanks for visiting.....</p>

<h3>⚡ You can also find me here...</h3>
<ul>
    <li><a href="https://www.linkedin.com/in/ewiewiora">LinkedIn</a></li>
    <li><a href="https://twitter.com/emwiewiora">Twitter</a></li>
    <li><a href="https://www.reddit.com/user/efreaq">Reddit</a>(as efreaq)</li>
</ul> 
''')
f.close()
