import html, os, re, shutil, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out")
SITE = "https://boomboomstunes.com"

YT = "https://www.youtube.com/@BoomBoomstunes"
SOCIAL = [
    ("YouTube", YT),
    ("Instagram", "https://www.instagram.com/boomboomstunes/"),
    ("TikTok", "https://www.tiktok.com/@boomboomstunes"),
    ("Facebook", "https://www.facebook.com/profile.php?id=61583342697741"),
    ("Spotify", "https://open.spotify.com/artist/3LVAZaWsdE5i31Ikjvlwl0"),
    ("Apple Music", "https://music.apple.com/us/album/playful-tunes/1848632387"),
    ("Etsy", "https://www.etsy.com/shop/BoomBoomsTunes"),
]
ETSY = "https://www.etsy.com/shop/BoomBoomsTunes"
NAV = [("Home", "/"), ("Books", "/books"), ("Videos", "/videos"), ("Shop", "/store"),
       ("Free Goodies", "/free-toddler-coloring-pages"), ("Blog", "/blog/"),
       ("About", "/about-us"), ("Contact", "/contact-us")]

AMZ_IMG = "https://m.media-amazon.com/images/I/"
BOOKS = [
    ("Wally, Wait!", "/img/wally.jpg", "B0HLXQG1D8",
     "Baby brother Wally gets into everything! A funny big-brother story with lines kids love to shout along with. Ages 2-6."),
    ("How A Best Friend Was Born", "/img/best-friend.jpg", "B0GP6SK5KN",
     "A stormy night fills the house with spooky shadows, and BoomBoom wishes for a friend to help him feel brave. A gentle story about big fears and best friends. Ages 2-6."),
    ("It Still Fits!", "/img/still-fits.jpg", "B0HNHMRCST",
     "BoomBoom’s favourite red sweater is getting much too small, but he insists it still fits! A cozy autumn story about growing up and sharing. Ages 2-6."),
]
ACTIVITY_BOOKS = [
    ("Christmas With BoomBoom and Fuzz!", AMZ_IMG + "71gEsQxkuGL._SL800_.jpg", "B0G6CZ8WM7",
     "A festive coloring book packed with cozy winter moments, playful adventures and cheerful Christmas fun with BoomBoom and Fuzz. A perfect stocking stuffer."),
    ("Halloween Fun Coloring Book", AMZ_IMG + "71s4PhU4aXL._SL800_.jpg", "B0HL5RH9CX",
     "47 big, bold, spooky-silly (never scary!) Halloween pictures with BoomBoom, Fuzz and the clumsy Zombie King. Made for little hands, ages 2-6."),
    ("ABC Winter Fun with BoomBoom and Fuzz", AMZ_IMG + "71uiO1d4VDL._SL800_.jpg", "B0GFN9WT7G",
     "Bundle up for snowy fun! An easy winter alphabet coloring book for toddlers and preschoolers, ages 2-5."),
    ("BoomBoom & Fuzz’s Valentine Counting Coloring Book", AMZ_IMG + "71CU0uKL+qL._SL800_.jpg", "B0GJSMZLP8",
     "Learn numbers 1 to 20 with BoomBoom and Fuzz while coloring sweet Valentine pages. Ages 2-5."),
]

PACKS = [
    ("Zombies in the Neighbourhood Song & Movement Pack", "/img/pack-zombies.jpg", "https://www.etsy.com/listing/4602409949",
     "Our spooky-silly zombie song plus 8 movement cards, a lyrics poster, a move-along sheet, 4 movement games and 3 coloring pages. Instant download for ages 2-6.", "CA$3.99"),
]

def pack_cards():
    return "".join(
        f'<div class="card"><img src="{i}" alt="{html.escape(t)}" loading="lazy" style="aspect-ratio:4/3;object-fit:cover"><div class="body"><span class="date">New · Instant download · {p}</span><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p>'
        f'<a class="btn" href="{u}" target="_blank" rel="noopener">Get it on Etsy</a></div></div>'
        for t, i, u, d, p in PACKS)

def pack_promo(heading="New! Song &amp; Movement Activity Packs", sub="Turn BoomBoom songs into brain breaks, circle time and party fun."):
    return f'''<section class="section" style="background:#3b2a6b;color:#fff"><div class="wrap"><h2 class="center" style="font-size:36px;margin-top:0;color:#b6f05a">{heading}</h2><p class="center" style="margin:-6px auto 26px;max-width:640px;font-size:19px">{sub}</p><div class="grid" style="max-width:760px;margin:auto;color:var(--ink)">{pack_cards()}</div></div></section>'''

def book_cards(items, kind):
    return "".join(
        f'<div class="card book"><img src="{i}" alt="{html.escape(t)} {kind} cover" loading="lazy"><div class="body"><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p>'
        f'<div class="btns"><a class="btn" href="https://www.amazon.com/dp/{a}" target="_blank" rel="noopener">Amazon.com</a>'
        f'<a class="btn alt2" href="https://www.amazon.ca/dp/{a}" target="_blank" rel="noopener">Amazon.ca</a></div></div></div>'
        for t, i, a, d in items)
PLAYLISTS = [
    ("Halloween Specials", "PLsqumUrD9vh1eFEC-TdUNGjjJjTIOo38C", "#ff7a2f"),
    ("Fun Songs & Cartoons", "PLsqumUrD9vh0mV5N47EUCbsNTYQBM8vmA", "#3d9bff"),
    ("Halloween Favorites", "PLsqumUrD9vh3Nvo0wooasmgFM_VflmqdS", "#8a5cf6"),
    ("Singalong Songs", "PLsqumUrD9vh09xViHjX-9NtopKuzlxa9K", "#22b573"),
    ("Halloween Meets Christmas", "PLsqumUrD9vh0phmviMxZBhrjGyj6AYZ5q", "#e5484d"),
    ("Snowy Winter Adventures", "PLsqumUrD9vh2GuokIFlXnEVK0doA11d4b", "#0ea5c6"),
    ("Sing, Dance, Learn!", "PLsqumUrD9vh1J62eVKTy_tzOMJsnyLh9_", "#f5a524"),
]
FEATURED_VIDEO = "zXRkuAOpa60"

CSS = """
:root{--orange:#ff5f1f;--orange-d:#e24d10;--sky:#7dbfff;--sky-l:#e8f4ff;--ink:#1f2a44;--muted:#54607a;--card:#fff;--bg:#fffaf3}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Nunito,system-ui,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6;font-size:17px}
h1,h2,h3,.brand,.btn,nav a{font-family:Fredoka,Nunito,sans-serif}
a{color:var(--orange-d)}img{max-width:100%;display:block}
header{background:var(--orange);position:sticky;top:0;z-index:10;box-shadow:0 2px 10px #0002}
.bar{max-width:1150px;margin:auto;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 16px;flex-wrap:wrap}
.brand{color:#fff;font-weight:700;font-size:28px;text-decoration:none;letter-spacing:.5px}
nav{display:flex;flex-wrap:wrap;gap:4px 18px}nav a{color:#fff;text-decoration:none;font-weight:600;font-size:17px;padding:2px 0;border-bottom:2px solid transparent}
nav a.on,nav a:hover{border-color:#fff}
.menu{display:none;background:none;border:2px solid #fff;color:#fff;border-radius:10px;font:600 16px Fredoka,sans-serif;padding:4px 12px}
@media(max-width:820px){.menu{display:block}nav{display:none;width:100%;flex-direction:column;gap:8px;padding:8px 0}nav.open{display:flex}.brand{font-size:24px}}
.hero{background:var(--orange);color:#fff;text-align:center;padding:24px 16px 90px;position:relative;overflow:hidden}
.hero img{width:min(320px,70vw);margin:0 auto}
.hero h1{font-size:clamp(36px,7vw,64px);margin:8px 0 0;line-height:1.1}.hero p{font-size:clamp(18px,3vw,26px);font-family:Fredoka,sans-serif;font-weight:600;margin:6px 0 18px}
.wave{position:absolute;left:-5%;right:-5%;bottom:-60px;height:120px;background:var(--sky);border-radius:50% 50% 0 0}
.blue{background:var(--sky);padding:24px 16px 56px}
.wrap{max-width:1100px;margin:auto}
.section{padding:48px 16px}.center{text-align:center}
.page-title{background:var(--sky);text-align:center;padding:40px 16px 34px}.page-title h1{margin:0;font-size:clamp(32px,6vw,52px);color:#fff;text-shadow:0 2px 0 #0002}
.page-title p{margin:6px 0 0;color:#fff;font-weight:700;font-size:19px}
.grid{display:grid;gap:22px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.card{background:var(--card);border-radius:22px;overflow:hidden;box-shadow:0 6px 20px #1f2a4415;display:flex;flex-direction:column}
.card .body{padding:18px 20px 22px;display:flex;flex-direction:column;gap:10px;flex:1}.card h3{margin:0;font-size:22px}
.card p{margin:0;color:var(--muted)}
.tile{display:block;text-align:center;text-decoration:none;color:#fff}.tile img{border-radius:26px;box-shadow:0 6px 20px #0002;aspect-ratio:16/10;object-fit:cover;width:100%;background:#fff}
.tile span{display:block;font:700 30px Fredoka,sans-serif;margin-bottom:8px;text-shadow:0 2px 0 #0002}
.btn{display:inline-block;background:var(--orange);color:#fff;text-decoration:none;font-weight:600;padding:12px 24px;border-radius:999px;font-size:17px;box-shadow:0 4px 0 var(--orange-d);transition:transform .1s}
.btn:hover{transform:translateY(-2px)}.btn.alt{background:#fff;color:var(--orange-d);box-shadow:0 4px 0 #0002}
.card .btn{align-self:flex-start;margin-top:auto}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:auto}.btns .btn{margin-top:0;padding:8px 14px;font-size:15px}
.btn.alt2{background:#fff;color:var(--orange-d);border:2px solid var(--orange);box-shadow:0 4px 0 #ffd2bd}
.book img{aspect-ratio:1/1;object-fit:cover;background:var(--sky-l)}
.pl{padding:26px 20px;color:#fff;border-radius:22px;text-decoration:none;display:flex;flex-direction:column;gap:14px;min-height:150px;justify-content:space-between;box-shadow:0 6px 20px #1f2a4420}
.pl h3{margin:0;font-size:24px}.pl .btn{background:#fff;color:var(--ink);box-shadow:0 4px 0 #0002;align-self:flex-start}
.video{position:relative;padding-top:56.25%;border-radius:22px;overflow:hidden;box-shadow:0 6px 20px #0002;background:#000}
.video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.post-list .card img{aspect-ratio:16/10;object-fit:cover}
.date{font-size:14px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.5px}
article.post{max-width:760px;margin:auto;padding:40px 16px 60px}
article.post h1{font-size:clamp(30px,5vw,44px);line-height:1.15;margin:6px 0 18px}
article.post img.cover{border-radius:22px;margin:0 0 26px;width:100%}
article.post h2{font-size:26px;margin:32px 0 8px}article.post p{margin:0 0 16px}
.postnav{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:40px;border-top:2px dashed #ffd2bd;padding-top:20px}
.join{background:var(--orange);color:#fff;text-align:center;padding:48px 16px}.join h2{margin:0 0 8px;font-size:34px}
.socials{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:16px}
.socials a{background:#fff;color:var(--ink);text-decoration:none;font:600 15px Fredoka,sans-serif;padding:8px 16px;border-radius:999px}
footer{background:var(--ink);color:#c9d2e6;text-align:center;padding:28px 16px;font-size:15px}footer a{color:#fff}
.note{background:#fff;border-radius:22px;padding:24px;box-shadow:0 6px 20px #1f2a4415}
ul.bul{padding-left:0;list-style:none}ul.bul li{margin:8px 0}
"""

def page(title, desc, path, body, og_img="img/hero.png"):
    nav = "".join(f'<a href="{h}"{" class=on" if (h == path or (h != "/" and path.startswith(h))) else ""}>{n}</a>' for n, h in NAV)
    socials = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{path}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/{og_img}"><meta property="og:type" content="website"><link rel="icon" href="/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v=2"></head><body>
<header><div class="bar"><a class="brand" href="/">BoomBooms Tunes</a><button class="menu" onclick="document.querySelector('nav').classList.toggle('open')">Menu</button><nav>{nav}</nav></div></header>
<main>{body}</main>
<section class="join"><h2>Join the BoomBoom Family!</h2><p>New songs, videos, books and free printables. Follow along wherever you watch and listen.</p><div class="socials">{socials}</div></section>
<footer>© {datetime.date.today().year} BoomBooms Tunes · Home of BoomBoom and Fuzz · <a href="/contact-us">Contact</a></footer>
</body></html>"""

def write(path, content):
    if path == "/": rel = "index.html"
    elif path == "/blog/": rel = "blog/index.html"
    elif path.endswith(".html"): rel = path.strip("/")
    else: rel = path.strip("/") + ".html"
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(content)

def fmt_date(d):
    return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")

def md(text):
    out, lst = [], []
    def flush():
        if lst:
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in lst) + "</ul>"); lst.clear()
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = block.split("\n")
        if all(l.startswith("- ") for l in lines):
            lst.extend(html.escape(l[2:]) for l in lines); continue
        flush()
        if block.startswith("## "):
            out.append(f"<h2>{html.escape(block[3:])}</h2>")
        else:
            out.append("<p>" + "<br>".join(html.escape(l) for l in lines) + "</p>")
    flush()
    return "\n".join(out)

def load_posts():
    raw = open(os.path.join(ROOT, "posts.txt")).read()
    posts = []
    for chunk in raw.split("=== ")[1:]:
        head, body = chunk.split("\n", 1)
        slug, title, date, img = [x.strip() for x in head.split("|")]
        plain = re.sub(r"\s+", " ", re.sub(r"^## |^- ", "", body, flags=re.M)).strip()
        posts.append(dict(slug=slug, title=title, date=date, img=img, body=body, excerpt=plain[:150].rsplit(" ", 1)[0] + "…"))
    return posts

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    if os.path.isdir(os.path.join(ROOT, "img")):
        shutil.copytree(os.path.join(ROOT, "img"), os.path.join(OUT, "img"))
    open(os.path.join(OUT, "style.css"), "w").write(CSS)
    open(os.path.join(OUT, "CNAME"), "w").write("boomboomstunes.com\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    os.makedirs(os.path.join(OUT, "downloads"), exist_ok=True)
    posts = load_posts()

    # Home
    books = book_cards(BOOKS, "picture book")
    activity = book_cards(ACTIVITY_BOOKS, "coloring book")
    home = f"""<section class="hero"><img src="/img/hero.png" alt="BoomBoom and Fuzz waving hello"><h1>Tiny Adventures</h1><p>With BoomBoom and Fuzz!</p><a class="btn alt" href="{YT}" target="_blank" rel="noopener">Watch on YouTube</a><div class="wave"></div></section>
<section class="blue"><div class="wrap"><h2 class="center" style="color:#fff;font-size:clamp(28px,5vw,42px);margin:0 0 24px;text-shadow:0 2px 0 #0002">Sing! Dance! Adventure!</h2>
<div class="grid"><a class="tile" href="/store"><span>Shop</span><img src="/img/shop.jpg" alt="BoomBoom and Fuzz shop" loading="lazy"></a>
<a class="tile" href="/videos"><span>Watch</span><img src="/img/watch.png" alt="Watch BoomBoom and Fuzz videos" loading="lazy"></a>
<a class="tile" href="https://open.spotify.com/artist/3LVAZaWsdE5i31Ikjvlwl0" target="_blank" rel="noopener"><span>Listen</span><img src="/img/listen.jpg" alt="Listen to BoomBooms Tunes songs" loading="lazy"></a></div></div></section>
<section class="section"><div class="wrap"><h2 class="center" style="font-size:36px;margin-top:0">BoomBoom &amp; Fuzz Picture Books</h2><div class="grid">{books}</div>
<h2 class="center" style="font-size:32px;margin-top:48px">Coloring &amp; Activity Books</h2><div class="grid">{activity}</div></div></section>
<section class="section" style="background:var(--sky-l)"><div class="wrap center"><h2 style="font-size:36px;margin-top:0">Free Printable Coloring Pages</h2><p>Free BoomBoom and Fuzz coloring sheets for little hands.</p><a class="btn" href="/free-toddler-coloring-pages">Get Free Goodies</a></div></section>""" + pack_promo()
    write("/", page("BoomBooms Tunes | Adventures with BoomBoom and Fuzz", "Kids songs, videos, picture books and free printables starring BoomBoom and Fuzz. Fun for toddlers and preschoolers.", "/", home))

    # Books
    write("/books", page("Children's Picture Books & Coloring Books for Toddlers | BoomBooms Tunes", "BoomBoom and Fuzz picture books and coloring books for ages 2-6: Wally, Wait!, It Still Fits!, Christmas, Halloween, ABC Winter and Valentine coloring books.", "/books",
        f'<div class="page-title"><h1>BoomBoom &amp; Fuzz Books</h1><p>Funny, cozy stories and coloring fun for ages 2 to 6</p></div><section class="section"><div class="wrap"><h2 class="center" style="font-size:32px;margin-top:0">Picture Books</h2><div class="grid">{books}</div><h2 class="center" style="font-size:32px;margin-top:48px">Coloring &amp; Activity Books</h2><div class="grid">{activity}</div></div></section>', "img/wally.jpg"))

    # Videos
    pls = "".join(f'<a class="pl" style="background:{c}" href="https://www.youtube.com/playlist?list={i}" target="_blank" rel="noopener"><h3>{html.escape(n)}</h3><span class="btn">Watch now</span></a>' for n, i, c in PLAYLISTS)
    write("/videos", page("Kids Videos for Toddlers & Preschoolers | BoomBooms Tunes", "Watch BoomBoom and Fuzz kids songs and cartoons on YouTube: Halloween specials, singalongs, winter adventures and more.", "/videos",
        f"""<div class="page-title"><h1>Watch BoomBoom &amp; Fuzz</h1><p>New songs and adventures on YouTube</p></div>
<section class="section"><div class="wrap"><h2 class="center" style="margin-top:0;font-size:32px">Featured Video</h2><div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{FEATURED_VIDEO}" title="BoomBooms Tunes featured video" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>
<p class="center" style="margin-top:22px"><a class="btn" href="{YT}" target="_blank" rel="noopener">Visit our YouTube channel</a></p>
<h2 class="center" style="font-size:32px;margin-top:48px">Our Playlists</h2><div class="grid">{pls}</div></div></section>""", "img/watch.png"))

    # Store
    write("/store", page("Shop BoomBoom & Fuzz Kids Clothes and Gifts | BoomBooms Tunes", "Shop BoomBoom and Fuzz printables, flash cards, coloring books, toddler tees and gifts on our Etsy shop.", "/store",
        f"""<div class="page-title"><h1>Shop BoomBoom &amp; Fuzz</h1><p>Printables, flash cards, toddler tees and gifts</p></div>
<section class="section"><div class="wrap center"><img src="/img/shop.jpg" alt="BoomBoom and Fuzz products" style="max-width:520px;width:100%;margin:0 auto 24px;border-radius:26px" loading="lazy">
</div></section>""" + pack_promo("Song &amp; Activity Packs", "Printable music and movement packs made from our songs.") + f"""<section class="section"><div class="wrap center"><p style="font-size:19px;max-width:620px;margin:0 auto 22px">Our shop now lives on Etsy! Find printable coloring books, action and yoga flash cards for toddlers, and BoomBoom and Fuzz clothing and gifts.</p>
<a class="btn" href="{ETSY}" target="_blank" rel="noopener">Visit our Etsy shop</a>
<h2 style="font-size:30px;margin-top:48px">Picture books</h2><p>Our BoomBoom and Fuzz books are on Amazon.</p><a class="btn alt" style="box-shadow:0 4px 0 #ffd2bd" href="/books">See the books</a></div></section>"""))

    # Free goodies
    pages = [("Trick-or-Treat Friends", "color-trick.jpg"), ("Giant Pumpkin Hug", "color-pumpkin.jpg"), ("Silly Skeleton Pals", "color-skeleton.jpg")]
    cards = "".join(f'<div class="card"><img src="/img/{i}" alt="{n} free Halloween coloring page for toddlers" loading="lazy" style="aspect-ratio:3/4;object-fit:cover"><div class="body"><h3>{n}</h3></div></div>' for n, i in pages)
    write("/free-toddler-coloring-pages", page("Free Toddler Coloring Pages | Printable Halloween Coloring Sheets | BoomBooms Tunes", "Free printable Halloween coloring pages for toddlers and preschoolers with BoomBoom and Fuzz. Download the free PDF.", "/free-toddler-coloring-pages",
        f"""<div class="page-title"><h1>Free BoomBoom &amp; Fuzz Goodies!</h1><p>Free printable coloring pages for little hands</p></div>
<section class="section"><div class="wrap"><h2 class="center" style="margin-top:0;font-size:32px">Free Halloween Coloring Pages</h2><div class="grid">{cards}</div>
<p class="center" style="margin-top:30px"><a class="btn" href="/downloads/BoomBoom-Halloween-Coloring-Pages.pdf" download>Download &amp; print (free PDF)</a></p></div></section>""" + pack_promo("Want More Halloween Fun?", "Get the full zombie song pack: the song, movement cards, a lyrics poster and 3 more coloring pages."), "img/color-pumpkin.jpg"))

    # About
    write("/about-us", page("About BoomBoom & Fuzz: Kids Songs, Videos & Books | BoomBooms Tunes", "Meet BoomBoom and his silly sidekick Fuzz. Original kids songs, 3D cartoons and picture books for toddlers and preschoolers.", "/about-us",
        f"""<div class="page-title"><h1>About BoomBoom &amp; Fuzz</h1><p>Welcome to BoomBooms Tunes</p></div>
<section class="section"><div class="wrap" style="max-width:780px"><div class="note"><img src="/img/hero.png" alt="BoomBoom and Fuzz" style="width:220px;margin:0 auto 10px" loading="lazy">
<p>Here, music and adventure come together in colorful, fun, and safe 3D cartoons for kids. Follow BoomBoom and his silly sidekick Fuzz as they explore giant cities, spooky-but-funny monsters, dinosaurs, vehicles, and magical places, turning everyday life into a big adventure.</p>
<p>Our catchy, upbeat songs and stories are designed to spark imagination, encourage movement, and make learning fun through:</p>
<ul class="bul"><li>🎶 Original kids songs with a spooky &amp; silly twist</li><li>🌈 Early learning woven into adventures (ABCs, numbers, colors)</li><li>🦖 Exciting adventures with dinosaurs, giants, and monsters</li><li>🤝 Lessons about friendship, bravery, and kindness</li><li>🌍 Imaginative journeys where anything can happen!</li><li>✨ New songs and adventures every week!</li></ul>
<p>Join BoomBoom, Fuzz, and friends in a world where music, learning, and laughter come together, perfect for toddlers, preschoolers, and early learners.</p>
<p><a class="btn" href="/videos">Watch our videos</a></p></div></div></section>"""))

    # Contact
    socials = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)
    write("/contact-us", page("Contact Us | BoomBooms Tunes", "Get in touch with BoomBooms Tunes, home of BoomBoom and Fuzz.", "/contact-us",
        f"""<div class="page-title"><h1>Contact Us</h1><p>Comments &amp; questions</p></div>
<section class="section"><div class="wrap center" style="max-width:700px"><div class="note"><p style="font-size:19px">We'd love to hear from you! Send us a message on any of our pages and we'll get back to you within 48 hours.</p>
<div class="socials">{socials.replace('<a ', '<a style="background:var(--sky-l)" ')}</div></div></div></section>"""))

    # Blog
    cards = "".join(f'<a class="card" style="text-decoration:none;color:inherit" href="/blog/{p["slug"]}"><img src="/img/blog/{p["img"]}" alt="{html.escape(p["title"])}" loading="lazy"><div class="body"><span class="date">{fmt_date(p["date"])}</span><h3>{html.escape(p["title"])}</h3><p>{html.escape(p["excerpt"])}</p></div></a>' for p in posts)
    write("/blog/", page("Toddler Parenting Blog: Real Life with Little Kids | BoomBooms Tunes", "Funny, honest stories about real life with toddlers and babies from the family behind BoomBooms Tunes.", "/blog/",
        f'<div class="page-title"><h1>Read Our Blog</h1><p>Real life with little kids</p></div><section class="section post-list"><div class="wrap"><div class="grid">{cards}</div></div></section>'))
    for n, p in enumerate(posts):
        newer = posts[n - 1] if n > 0 else None
        older = posts[n + 1] if n + 1 < len(posts) else None
        pn = '<div class="postnav">' + (f'<a href="/blog/{newer["slug"]}">← {html.escape(newer["title"])}</a>' if newer else "<span></span>") + (f'<a href="/blog/{older["slug"]}">{html.escape(older["title"])} →</a>' if older else "") + "</div>"
        body = f'<article class="post"><a href="/blog/">← All posts</a><p class="date" style="margin:18px 0 0">{fmt_date(p["date"])}</p><h1>{html.escape(p["title"])}</h1><img class="cover" src="/img/blog/{p["img"]}" alt="{html.escape(p["title"])}">{md(p["body"])}{pn}</article>'
        write(f"/blog/{p['slug']}", page(f'{p["title"]} | BoomBooms Tunes', p["excerpt"], f"/blog/{p['slug']}", body, f"img/blog/{p['img']}"))

    # 404 + sitemap
    write("/404.html", page("Page not found | BoomBooms Tunes", "Page not found", "/404.html",
        '<div class="page-title"><h1>Oops! This page wandered off</h1><p>BoomBoom and Fuzz can\'t find it either.</p></div><section class="section center"><a class="btn" href="/">Back home</a></section>'))
    urls = ["/", "/books", "/videos", "/store", "/free-toddler-coloring-pages", "/blog/", "/about-us", "/contact-us"] + [f"/blog/{p['slug']}" for p in posts]
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls) + "</urlset>\n")
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(posts), "posts")

build()
