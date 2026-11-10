import pathlib, sys
OUT = pathlib.Path(sys.argv[1])
FORM = "https://formsubmit.co/ajax/6638b572df1cd1faa5b6cd55414ca8cc"
SITE = "https://localaibootcamp.com"

NAV = [("index.html","Home"),("how-it-works.html","How it works"),("teams.html","For teams"),("about.html","About")]
PAGES = ["index.html","how-it-works.html","teams.html","about.html","contact.html"]
# Old URLs that now forward to their new home
REDIRECTS = {"team-training.html":"teams.html","ai-policy.html":"teams.html#guidelines","classes.html":"how-it-works.html#open-sessions"}

def head(title, desc, path):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if path=='index.html' else path[:-5]}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..800&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
'''

def header(path):
    links = "\n".join(f'<a href="{h}"{" aria-current=\"page\"" if h==path else ""}>{t}</a>' for h,t in NAV)
    return f'''</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">Local AI <span>Bootcamp</span></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <a class="btn" href="contact.html">Start a conversation</a>
    </nav>
  </div>
</header>
<main id="main">
'''

FOOTER = '''</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <a class="brand" href="index.html">Local AI <span>Bootcamp</span></a>
      <p style="margin-top:14px">In-person AI training across Dallas–Fort Worth. Someone beside you, showing you how AI makes what you already know go further.</p>
    </div>
    <div>
      <h3>Training</h3>
      <ul>
        <li><a href="how-it-works.html">How it works</a></li>
        <li><a href="teams.html">For teams</a></li>
        <li><a href="how-it-works.html#open-sessions">Open sessions</a></li>
      </ul>
    </div>
    <div>
      <h3>Local AI Bootcamp</h3>
      <ul>
        <li><a href="about.html">About Andrew</a></li>
        <li><a href="how-it-works.html#host">Host a session</a></li>
        <li><a href="contact.html">Start a conversation</a></li>
      </ul>
    </div>
    <p class="legal">© 2026 Local AI Bootcamp. Serving Dallas, Fort Worth, Plano, Frisco, McKinney, Rockwall and the rest of DFW.</p>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
'''

def page(path, title, desc, body, extra_head=""):
    (OUT/path).write_text(head(title, desc, path) + extra_head + header(path) + body + FOOTER)

def form(kind, button, fields, success, note=""):
    return f'''<form class="signup" action="{FORM}" method="POST" data-success="{success}">
  <input type="hidden" name="form" value="{kind}">
  <input type="hidden" name="_subject" value="New {kind} submission from localaibootcamp.com">
  <input type="hidden" name="_template" value="table">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
  {fields}
  <button class="btn" type="submit">{button}</button>
  {f'<p class="form-note">{note}</p>' if note else ''}
  <p class="form-status" role="status" aria-live="polite"></p>
</form>'''

def f_input(name, label, type="text", req=True, auto=""):
    r = " required" if req else ""
    a = f' autocomplete="{auto}"' if auto else ""
    return f'<div class="field"><label for="{name}">{label}{"" if req else " (optional)"}</label><input id="{name}" name="{name}" type="{type}"{r}{a}></div>'

def f_select(name, label, opts):
    o = "".join(f"<option>{x}</option>" for x in opts)
    return f'<div class="field"><label for="{name}">{label}</label><select id="{name}" name="{name}">{o}</select></div>'

def f_text(name, label, req=False):
    return f'<div class="field"><label for="{name}">{label}{"" if req else " (optional)"}</label><textarea id="{name}" name="{name}" rows="4"{" required" if req else ""}></textarea></div>'

name_email = f'<div class="field-row">{f_input("name","Your name",auto="name")}{f_input("email","Email","email",auto="email")}</div>'
AREAS = ["Dallas","Fort Worth","Plano / Frisco / McKinney","Rockwall / Royse City / Rowlett","Arlington / Mid-Cities","Denton / Lewisville","Somewhere else in DFW"]

SETTINGS = '''
    <div class="ladder">
      <div class="rung noprice lead">
        <div><h3>With your team</h3><p class="for">At your office</p></div>
        <p>Andrew comes to you and works with your whole team on the work they actually do. Everyone learns together, so AI becomes part of how the business runs, not one person's side project.</p>
      </div>
      <div class="rung noprice">
        <div><h3>In a small group</h3><p class="for">An owner and a few key people</p></div>
        <p>A focused session for you and the people you rely on most. Good when you want to figure out where AI fits before bringing in everyone else.</p>
      </div>
      <div class="rung noprice">
        <div><h3>At an open session</h3><p class="for">Hosted around DFW</p></div>
        <p>Small sessions at coworking spaces across the metroplex for individuals who want to learn on their own. Same approach, with a handful of other local professionals at the table.</p>
      </div>
    </div>'''

# ---------------- HOME ----------------
schema = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"EducationalOrganization","name":"Local AI Bootcamp","url":"https://localaibootcamp.com","description":"In-person AI training in Dallas–Fort Worth. Learn to use AI to make what you already know go further, with someone beside you showing you how.","areaServed":{"@type":"Place","name":"Dallas–Fort Worth, TX"},"founder":{"@type":"Person","name":"Andrew Neal"}}
</script>
'''
home = f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Learn AI with someone right beside you.</h1>
      <p class="lede">Not another online course, YouTube video or webinar. Andrew sits down with you and your team, works through your real work, and shows you how AI can make what you already know go further.</p>
      <div class="actions">
        <a class="btn" href="contact.html">Start a conversation</a>
        <a class="btn ghost" href="how-it-works.html">See how it works</a>
      </div>
    </div>
    <aside class="room shift" aria-label="What changes">
      <h2>Where people start, and where they end up</h2>
      <ul>
        <li><span>"I know I should be using AI. I don't know where it fits."</span><strong>Using it every day on the work that matters to them</strong></li>
        <li><span>"I tried ChatGPT. The answers were generic."</span><strong>Getting answers that sound like them and know their business</strong></li>
        <li><span>"Is this going to replace me?"</span><strong>Using it to do more of what they're best at</strong></li>
      </ul>
      <div class="sticky">You bring the know-how. AI brings the speed.</div>
    </aside>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="section-head">
      <h2>You don't need another course.</h2>
      <p class="lede">There's no shortage of AI content. What's missing is someone showing you how it applies to you.</p>
    </div>
    <div class="contrast">
      <div><h3>Online courses</h3><p>You sign up, watch the first two modules, and never finish. Nobody notices.</p></div>
      <div><h3>YouTube videos</h3><p>Great demos built on someone else's business. Getting from their example to your work is left to you.</p></div>
      <div><h3>Webinars</h3><p>An hour of slides, a few takeaways, and nothing changes on Monday morning.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <p class="pull">AI doesn't replace what you know. It multiplies it.</p>
    </div>
    <div>
      <p>Your experience, judgment and relationships are what make you good at your job. AI can't replace those. Used well, it takes the first draft, the research and the repetitive parts off your plate, so you spend more of your time on the work only you can do.</p>
      <p>That's the whole idea here. You don't come out of this as a "tech person." You come out as a better version of what you already are, with a new skill you'll use for the rest of your career.</p>
      <p>You also learn where AI falls short: when it's confidently wrong, and why your own knowledge is what keeps it honest.</p>
    </div>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="section-head">
      <h2>Same approach, three settings</h2>
      <p class="lede">Every session is in person, and built around the people in the room.</p>
    </div>
    {SETTINGS}
    <div class="actions"><a class="btn" href="contact.html">Talk about what fits</a></div>
  </div>
</section>

<section class="ink">
  <div class="wrap split">
    <div>
      <h2>Taught by someone who uses it to run a business.</h2>
      <p>Andrew Neal has spent 15+ years in marketing, leading marketing for 8-figure service companies and as a senior marketing director at both bootstrapped and VC-funded software companies. Today he runs his own service business in DFW, and AI is part of how he works every day.</p>
      <p><a href="about.html">More about Andrew</a></p>
    </div>
    <ul class="checklist">
      <li>Real estate agents and brokerages</li>
      <li>Owners of service and local businesses</li>
      <li>Office managers and the people who keep things running</li>
      <li>Sales, marketing and client-facing teams</li>
      <li>Anyone who knows their job well and wants AI to help them do more of it</li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <h2>Let's talk about where you are.</h2>
      <p>Tell Andrew a little about you or your team. He'll reach out to set up a short call and figure out what would actually help.</p>
    </div>
    {form("contact","Start a conversation", name_email + f_select("interest","I'm interested in",["Training for my team","A small group session","Open sessions near me","Not sure yet"]) + f_text("message","Anything Andrew should know?"), "Thanks. Andrew will reach out within one business day.")}
  </div>
</section>
'''
page("index.html","In-Person AI Training in DFW | Local AI Bootcamp",
     "Learn AI with someone right beside you. In-person AI training for professionals and teams across Dallas–Fort Worth. No courses, no webinars.", home, schema)

# ---------------- HOW IT WORKS ----------------
how = f'''
<section class="hero">
  <div class="wrap">
    <h1>How it works.</h1>
    <p class="lede">Every session starts with you: what you do, what you already know, and where your time goes. Then Andrew shows you, side by side, how AI fits into that.</p>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="steps">
      <div class="step"><h3>Start with your work</h3><p>Before anything is scheduled, Andrew talks with you about your role, your business and what a normal week looks like. Nothing is generic. The session is shaped around those answers.</p></div>
      <div class="step"><h3>Learn shoulder to shoulder</h3><p>You work on your own laptop, on your own real work, with Andrew right there. When something doesn't click, you get help in the moment instead of rewinding a video.</p></div>
      <div class="step"><h3>Keep going afterward</h3><p>Questions show up once you're back at your desk. You'll have a direct line to Andrew while the new habits settle in, so you aren't left on your own.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <h2>What you walk away with</h2>
      <p>The goal isn't to learn every AI tool. It's to leave with a few ways of working you'll actually keep using, because they came from your own work.</p>
    </div>
    <ul class="checklist">
      <li>A clear sense of what AI is good at, and where it isn't</li>
      <li>The confidence to use it on your own, without a script</li>
      <li>Ways to get answers that sound like you and fit your business</li>
      <li>Habits for checking AI's work against what you know</li>
      <li>A short plan for where to take it next</li>
    </ul>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="section-head"><h2>Three settings</h2></div>
    {SETTINGS}
  </div>
</section>

<section id="open-sessions">
  <div class="wrap split">
    <div>
      <h2>Open sessions near you</h2>
      <p>Open sessions are added as venues are confirmed around DFW. Join the list and you'll hear about new dates first.</p>
    </div>
    {form("open-sessions","Get session dates", name_email + f_select("area","Closest area",AREAS), "You're on the list. You'll get an email when the next session near you is scheduled.", "One email when new dates are posted. No spam.")}
  </div>
</section>

<section class="ink" id="host">
  <div class="wrap split">
    <div>
      <h2>Run a coworking space? Host a session.</h2>
      <p>Sessions bring local professionals through your doors and give your members something worth staying for. Hosts share in the revenue from every session at their space.</p>
    </div>
    <div>
      <ul class="checklist" style="margin-bottom:28px">
        <li>A share of revenue from sessions at your space</li>
        <li>Something valuable to offer your members</li>
        <li>New faces in the building who may come back to tour</li>
        <li>You provide the room, Wi-Fi and a screen. Andrew handles the rest.</li>
      </ul>
      <a class="btn" style="background:var(--note);border-color:var(--note);color:var(--ink)" href="contact.html?interest=host">Talk about hosting</a>
    </div>
  </div>
</section>
'''
page("how-it-works.html","How In-Person AI Training Works | Local AI Bootcamp",
     "Personal, in-person AI training in DFW built around your real work. Learn shoulder to shoulder with Andrew Neal, with support afterward.", how)

# ---------------- TEAMS ----------------
faq = [
 ("How is this different from an online AI course?","Online courses are the same for everyone, and most people never finish them. This is built around your team's actual work, delivered in person, with Andrew in the room to help each person as they go."),
 ("Does my team need to be technical?","No. Most people start with little or no AI experience. If someone can write an email, they can do this."),
 ("Will AI replace people on my team?","That's not what this is about. The focus is helping the people you already have use AI to get more out of their own experience and skills."),
 ("What does it cost?","Every engagement is shaped around your team: how many people, what they do and what support you want afterward. Start a conversation and Andrew will put together a proposal."),
 ("Where does training happen?","At your office anywhere in DFW. If you don't have a room that fits, a meeting space can be arranged nearby."),
 ("Can a brokerage offer this to its agents?","Yes. Many brokerages offer training as a benefit for their agents. Andrew can work with you on how to set it up."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
teams = f'''
<section class="hero">
  <div class="wrap">
    <h1>Bring your whole team along.</h1>
    <p class="lede">Your people are already experimenting with AI on their own, with mixed results. Training together gives everyone the same footing, the same habits and the same guardrails.</p>
    <div class="actions"><a class="btn" href="contact.html?interest=team">Talk about your team</a></div>
  </div>
</section>

<section class="white">
  <div class="wrap split">
    <div>
      <h2>Built around how your team works</h2>
      <p>Before any training, Andrew learns how your business runs: the roles, the busy seasons, the tasks that eat up time. The sessions are then built around your team's real work, so people leave using AI on the things they'll do tomorrow.</p>
    </div>
    <ul class="checklist">
      <li>In-person sessions at your office</li>
      <li>Hands-on time for every person, on their own work</li>
      <li>Ongoing support after training while habits settle in</li>
      <li>Clear guidelines for how your company uses AI</li>
    </ul>
  </div>
</section>

<section id="guidelines">
  <div class="wrap split">
    <div>
      <h2>Guidelines your team will actually follow</h2>
      <p>Your team is already using AI, approved or not. Without guidance, people make their own rules about what's safe to share and what needs a second look.</p>
      <p>Andrew helps you put simple, plain-English AI guidelines in place: which tools are approved, what information stays out, and when a person needs to review AI's work before it goes out. Then he walks your team through them in person, so they understand the why.</p>
    </div>
    <div class="callout">
      <h3>Your AI guidelines cover</h3>
      <ul class="checklist">
        <li>Which AI tools your team can use, and how</li>
        <li>Client and company information that never goes into AI</li>
        <li>When AI output needs a human review</li>
        <li>Who to ask when something isn't covered</li>
      </ul>
      <p class="small" style="margin-top:16px">Practical guidance for your business, not legal advice.</p>
    </div>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="section-head"><h2>Questions teams ask</h2></div>
    <div class="faq">{faq_html}</div>
  </div>
</section>
'''
page("teams.html","In-Person AI Training for Teams in DFW | Local AI Bootcamp",
     "On-site AI training for teams across Dallas–Fort Worth. Built around your team's real work, with AI guidelines and ongoing support afterward.", teams)

# ---------------- ABOUT ----------------
about = '''
<section class="hero">
  <div class="wrap split">
    <div>
      <h1>Hi, I'm Andrew.</h1>
      <p class="lede">I help people take what they already know and make it go further with AI. In person, at the same table, on your own work.</p>
    </div>
    <div class="callout">
      <p>Based in Royse City. Working with people across Dallas, Fort Worth and everywhere in between.</p>
    </div>
  </div>
</section>
<section class="white">
  <div class="wrap split">
    <div>
      <h2>Background</h2>
      <p>I've spent more than 15 years in marketing. I've been head of marketing for 8-figure service companies and a senior marketing director at both bootstrapped and VC-funded software companies.</p>
      <p>I also own and run a local service business here in DFW. AI is part of how I work every day. It hasn't replaced anything I know. It's let me do more with it.</p>
    </div>
    <div>
      <h2>Why in person</h2>
      <p>Most people I talk to have already tried to learn AI. They've bookmarked the courses, watched the videos and sat through the webinars. What they didn't get was someone showing them how it applies to their job, their clients and their business.</p>
      <p>That's what I do. I sit down next to you, we work on your real work, and we figure it out together. You leave more capable than you came in, and still fully in charge.</p>
      <div class="actions"><a class="btn" href="contact.html">Start a conversation</a></div>
    </div>
  </div>
</section>
'''
page("about.html","About Andrew Neal | Local AI Bootcamp",
     "Andrew Neal brings 15+ years of marketing leadership to personal, in-person AI training for professionals and teams in Dallas–Fort Worth.", about)

# ---------------- CONTACT ----------------
contact_fields = name_email + '<div class="field-row">' + f_input("company","Company", req=False) + f_input("phone","Phone","tel",req=False,auto="tel") + '</div>' + \
  f_select("interest","I'm interested in",["Training for my team","A small group session","Open sessions near me","Hosting sessions at my coworking space","Not sure yet"]) + \
  f_select("team_size","How many people?",["Just me","2–6","7–15","16–40","40+"]) + f_text("message","What would you most like AI to help with?")
contact = f'''
<section class="hero">
  <div class="wrap split">
    <div>
      <h1>Let's talk about where you are.</h1>
      <p class="lede">Tell Andrew a little about you, your role or your team. He'll reply within one business day to set up a short call.</p>
      <p>No pressure and no pitch deck. The call is about what you do and whether this would actually help.</p>
    </div>
    {form("contact","Start a conversation", contact_fields, "Thanks. Andrew will reply within one business day to set up a call.")}
  </div>
</section>
<script>
(function(){{var p=new URLSearchParams(location.search).get('interest');var m={{team:0,'small-group':1,sessions:2,host:3}};
if(p in m){{document.getElementById('interest').selectedIndex=m[p];}}}})();
</script>
'''
page("contact.html","Start a Conversation | Local AI Bootcamp",
     "Talk with Andrew about in-person AI training for you or your team in Dallas–Fort Worth.", contact)

# Redirect stubs for retired URLs
for old, new in REDIRECTS.items():
    (OUT/old).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title><link rel="canonical" href="{SITE}/{new.replace(".html","")}"><meta http-equiv="refresh" content="0; url={new}"><meta name="robots" content="noindex"></head><body><p>This page moved. <a href="{new}">Continue</a>.</p></body></html>')

# favicon, robots, sitemap
(OUT/"assets/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#172033"/><rect x="30" y="30" width="26" height="26" fill="#FFD54A" transform="rotate(4 43 43)"/><text x="10" y="40" font-family="Arial Black,Arial" font-weight="900" font-size="26" fill="#fff">AI</text></svg>')
(OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"<url><loc>{SITE}/{'' if p=='index.html' else p[:-5]}</loc></url>" for p in PAGES)
(OUT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
print("built")
