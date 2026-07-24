from pathlib import Path

SVG = """<svg width="1000" height="420" xmlns="http://www.w3.org/2000/svg">

<rect
    width="1000"
    height="420"
    rx="18"
    fill="#0d1117"
    stroke="#30363d"
    stroke-width="2"/>

<text
    x="40"
    y="55"
    fill="#58a6ff"
    font-family="Consolas, monospace"
    font-size="30"
    font-weight="bold">

Vedant Vyas

</text>

<text
    x="40"
    y="90"
    fill="#8b949e"
    font-family="Consolas, monospace"
    font-size="18">

Full Stack Developer | AI/ML Engineer

</text>

<line
    x1="40"
    y1="115"
    x2="960"
    y2="115"
    stroke="#30363d"/>

<text
    x="40"
    y="160"
    fill="#f0883e"
    font-size="18"
    font-family="Consolas">

Role

</text>

<text
    x="240"
    y="160"
    fill="#c9d1d9"
    font-size="18"
    font-family="Consolas">

Full Stack Developer

</text>

<text
    x="40"
    y="195"
    fill="#f0883e"
    font-size="18"
    font-family="Consolas">

University

</text>

<text
    x="240"
    y="195"
    fill="#c9d1d9"
    font-size="18"
    font-family="Consolas">

VIT Bhopal

</text>

<text
    x="40"
    y="230"
    fill="#f0883e"
    font-size="18"
    font-family="Consolas">

Company

</text>

<text
    x="240"
    y="230"
    fill="#c9d1d9"
    font-size="18"
    font-family="Consolas">

Entertainment Technologists

</text>

<text
    x="40"
    y="265"
    fill="#f0883e"
    font-size="18"
    font-family="Consolas">

Focus

</text>

<text
    x="240"
    y="265"
    fill="#c9d1d9"
    font-size="18"
    font-family="Consolas">

AI • ML • Full Stack

</text>

<line
    x1="40"
    y1="295"
    x2="960"
    y2="295"
    stroke="#30363d"/>

<text
    x="40"
    y="340"
    fill="#58a6ff"
    font-size="18"
    font-family="Consolas">

Python • React • FastAPI • MongoDB • AWS

</text>

<text
    x="40"
    y="385"
    fill="#8b949e"
    font-size="16"
    font-family="Consolas">

Dynamic GitHub stats will appear here...

</text>

</svg>
"""

Path("assets/hero.svg").write_text(SVG, encoding="utf-8")

print("hero.svg generated successfully!")
