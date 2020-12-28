# The base code was pulled from Kelvin Chu and this article and tweeked for my needs.
# https://dev.to/ragebill/how-to-create-a-self-updating-github-profile-2m22
# https://github.com/RageBill/RageBill

import requests, json, random

f = open("./README.md", "w")
pokemon_id = random.randint(1, 807)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''<img align="right" src="{result['sprites']['front_default']}" width="100" height="100">
<p>I am currently learning FullStack part time, in hopes to change my career.</p>
<h3>🌱 I’m currently learning ...</h3>
<ol>
    <li>CS50 - Intro to Computer Science - Harvard - EdX </li>
</ol>

<h3>🔭 I’m currently working on ...</h3>
<ol>
    <li>See what i am playing with in codepen.io <a target="_blank" href="https://codepen.io/emwiewiora">here</a></li>
    <li>LinkedIn Learning: On Hold</li>
    <li>I have started <a href="https://www.theodinproject.com/">The Odin Project</a></li>
    <li>Developing this page</li>
    <li>Random small projects that look interesting, from around the net.</li>
</ol>

<p>Thanks for visiting.....</p>

<h4>⚡ You can also find me here...</h4>
<ul>
    <li><a href="https://www.linkedin.com/in/ewiewiora">LinkedIn</a></li>
    <li><a href="https://twitter.com/emwiewiora">Twitter</a></li>
    <li><a href="https://www.reddit.com/user/efreaq">Reddit</a>(as efreaq)</li>
</ul> 
''')
f.close()
