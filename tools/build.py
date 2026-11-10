import pathlib, sys
OUT = pathlib.Path(sys.argv[1])
FORM = "https://formsubmit.co/ajax/andrew@localaibootcamp.com"
EMAIL = "andrew@localaibootcamp.com"
SITE = "https://localaibootcamp.com"

NAV = [("index.html","Home"),("team-training.html","Team training"),("classes.html","Classes"),("ai-policy.html","AI policy"),("about.html","About")]

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
      <a class="btn" href="contact.html">Book a call</a>
    </nav>
  </div>
</header>
<main id="main">
'''

FOOTER = f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <a class="brand" href="index.html">Local AI <span>Bootcamp</span></a>
      <p style="margin-top:14px">In-person, hands-on AI training for small businesses and teams across Dallas–Fort Worth.</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <h3>Training</h3>
      <ul>
        <li><a href="team-training.html">Team training</a></li>
        <li><a href="team-training#small-group">Private small groups</a></li>
        <li><a href="classes.html">Public classes</a></li>
        <li><a href="ai-policy.html">AI policy &amp; governance</a></li>
      </ul>
    </div>
    <div>
      <h3>Company</h3>
      <ul>
        <li><a href="about.html">About Andrew</a></li>
        <li><a href="classes.html#host">Host a class</a></li>
        <li><a href="contact.html">Contact</a></li>
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

# ---------------- HOME ----------------
schema = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"EducationalOrganization","name":"Local AI Bootcamp","url":"https://localaibootcamp.com","description":"In-person, hands-on AI training for small businesses and teams in Dallas–Fort Worth.","areaServed":{"@type":"Place","name":"Dallas–Fort Worth, TX"},"founder":{"@type":"Person","name":"Andrew Neal"}}
</script>
'''
home = f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>AI training, in the room with your team.</h1>
      <p class="lede">Hands-on sessions at your office or at coworking spaces around DFW. Your people bring their laptops and their real work, and leave using AI on it the same day.</p>
      <div class="actions">
        <a class="btn" href="contact.html">Book a call about your team</a>
        <a class="btn ghost" href="classes.html">See public classes</a>
      </div>
    </div>
    <aside class="room" aria-label="What a session covers">
      <h2>A typical half-day session</h2>
      <ul>
        <li><strong>Set up the right AI tools</strong><span>everyone, on their own laptop</span></li>
        <li><strong>Write the emails you owe today</strong><span>with your real inbox</span></li>
        <li><strong>Build a week of posts and listings</strong><span>in your brand voice</span></li>
        <li><strong>Check AI's work for mistakes</strong><span>what to trust, what not to</span></li>
        <li><strong>Agree on house rules</strong><span>what data stays out of AI</span></li>
      </ul>
      <div class="sticky">Bring your laptop. Leave with it working.</div>
    </aside>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="section-head">
      <h2>Three ways to train</h2>
      <p class="lede">Every option is in person and hands-on. Pick the one that fits how many people you need trained.</p>
    </div>
    <div class="ladder">
      <div class="rung lead">
        <div><h3>Team training</h3><p class="for">For brokerages, offices and companies training a whole team</p></div>
        <p>Andrew comes to your office and trains your team on the AI tools that fit your work. Programs include a written AI use policy for your company and months of follow-up support in a private Slack channel.</p>
        <div class="price">From $3,500<small>per team</small></div>
      </div>
      <div class="rung">
        <div><h3>Private small group</h3><p class="for">For an owner and a few key people</p></div>
        <p>A focused session for up to 6 people, built around your business. Good for owners who want their office manager or lead staff trained alongside them.</p>
        <div class="price">From $1,500<small>per group</small></div>
      </div>
      <div class="rung">
        <div><h3>Public classes</h3><p class="for">For individuals buying their own seat</p></div>
        <p>Small classes hosted at coworking spaces across DFW. Start with a 3-hour intro, or join the 4-week bootcamp to go from zero to using AI every day.</p>
        <div class="price">From $149<small>per seat</small></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>How team training works</h2></div>
    <div class="steps">
      <div class="step"><h3>We talk about your work</h3><p>A 30-minute call about what your team does all day, which tools you already use, and where time goes. The session is built around those answers.</p></div>
      <div class="step"><h3>Andrew trains in the room</h3><p>Your team works on their own laptops with their own emails, listings, quotes and posts. No slide marathons. Everyone leaves with things they made.</p></div>
      <div class="step"><h3>Support continues after</h3><p>Questions come up once people get back to work. Your team posts them in a private Slack channel and gets real answers, not a help article.</p></div>
    </div>
  </div>
</section>

<section class="ink">
  <div class="wrap split">
    <div>
      <h2>Your team is already using AI. Do you have rules for it?</h2>
      <p>Most small businesses have staff pasting client details into free AI tools with no guidance on what's safe. A short, plain-English AI use policy fixes that, and every team program includes one.</p>
      <div class="actions"><a class="btn ghost" style="color:var(--note);border-color:var(--note)" href="ai-policy.html">How the AI policy works</a></div>
    </div>
    <ul class="checklist">
      <li>Which AI tools your team is approved to use</li>
      <li>What client and company data never goes into AI</li>
      <li>When AI output needs a human review before it goes out</li>
      <li>Who to ask when something isn't covered</li>
    </ul>
  </div>
</section>

<section class="white">
  <div class="wrap split">
    <div>
      <h2>Taught by a marketer, not a programmer</h2>
      <p>Andrew Neal has spent 15+ years in marketing, leading marketing for 8-figure service companies and as a senior marketing director at bootstrapped and VC-funded software companies. He runs his own service business in DFW and uses these tools every day.</p>
      <p>That means training is about the work small businesses actually do: follow-ups, listings, quotes, posts, reviews and reports.</p>
      <p><a href="about.html">More about Andrew</a></p>
    </div>
    <div class="callout">
      <h3>Who this is for</h3>
      <ul class="checklist">
        <li>Real estate brokerages and their agents</li>
        <li>Home service and local service businesses</li>
        <li>Small offices that want their whole team on the same page</li>
        <li>Owners who know they should be using AI but don't know where to start</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div>
      <h2>Get dates for classes near you</h2>
      <p>Public classes are added as venues are confirmed around DFW. Join the list and you'll hear about new dates first.</p>
    </div>
    {form("class-list","Join the class list", name_email + f_select("area","Closest area",["Dallas","Fort Worth","Plano / Frisco / McKinney","Rockwall / Royse City / Rowlett","Arlington / Mid-Cities","Denton / Lewisville","Somewhere else in DFW"]), "You're on the list. You'll get an email when the next class near you is scheduled.", "One email when new dates are posted. No spam.")}
  </div>
</section>
'''
page("index.html","In-Person AI Training for DFW Teams | Local AI Bootcamp",
     "Hands-on AI training for small businesses, real estate offices and teams across Dallas–Fort Worth. On-site team training, private small groups and public classes.", home, schema)

# ---------------- TEAM TRAINING ----------------
faq = [
 ("How many people can you train at once?","Team sessions work best with up to 15 people so everyone gets hands-on help. For bigger teams, sessions are split into groups on the same day or across a few days."),
 ("Do we need any technical background?","No. Sessions start from zero. If someone can write an email, they can do this."),
 ("Which AI tools do you teach?","Mostly ChatGPT, Claude, Gemini, Microsoft Copilot and Canva's AI features, plus whatever your team already pays for. The call before the session decides which ones fit."),
 ("What does the Slack support include?","Your team gets a private channel. Post a question, a screenshot or a draft, and Andrew answers within one business day. It's for questions about using AI in your work, not a help desk for unrelated software."),
 ("Where do sessions happen?","At your office anywhere in DFW. If you don't have a room that fits, a coworking space conference room can be booked for you."),
 ("Can real estate agents in a brokerage join if they're independent contractors?","Yes. Many brokerages offer training as a perk for their agents. Talk to Andrew about splitting the cost or running it as an agent event."),
]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)
team = f'''
<section class="hero">
  <div class="wrap">
    <h1>Team training at your office.</h1>
    <p class="lede">Andrew comes to you, trains your whole team on their own laptops, and stays available afterward while the habits stick. Built for brokerages, small offices and service companies across DFW.</p>
    <div class="actions"><a class="btn" href="contact.html">Book a call</a></div>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="section-head"><h2>Two team packages</h2><p class="lede">Prices are per team of up to 15 people. Larger teams get a custom quote.</p></div>
    <div class="packages">
      <div class="package">
        <h3>Team Workshop</h3>
        <p>One focused session to get everyone using AI.</p>
        <div class="amount">$3,500</div>
        <div class="unit">per team, up to 15 people</div>
        <ul class="checklist">
          <li>Planning call about your team's work</li>
          <li>One half-day hands-on session at your office</li>
          <li>Prompt and template library for your business</li>
          <li>30 days of Q&amp;A in a private Slack channel</li>
        </ul>
        <a class="btn ghost" href="contact.html?package=workshop">Ask about the workshop</a>
      </div>
      <div class="package featured">
        <h3>Team Program</h3>
        <p>Training, a written AI policy and six months of support.</p>
        <div class="amount">$7,500</div>
        <div class="unit">per team, up to 15 people</div>
        <ul class="checklist">
          <li>Planning call and a review of how your team uses AI today</li>
          <li>Two half-day sessions: a kickoff, then a follow-up 30 days later</li>
          <li>A written AI use policy for your company, reviewed with leadership</li>
          <li>Prompt and template library built around your workflows</li>
          <li>6 months of Q&amp;A in a private Slack channel</li>
          <li>A 3-month AI roadmap for the business</li>
        </ul>
        <a class="btn" href="contact.html?package=program">Ask about the program</a>
      </div>
    </div>
  </div>
</section>

<section id="small-group">
  <div class="wrap split">
    <div>
      <h2>Private small group</h2>
      <p class="lede">For an owner and up to 5 key people.</p>
      <p>A single 3-hour session built around your business, at your office or in a reserved meeting room. It's the right fit when the owner wants to learn alongside an office manager, an assistant or a few lead staff without booking the whole team.</p>
      <p><strong>From $1,500</strong> per group, including 30 days of email support.</p>
      <div class="actions"><a class="btn" href="contact.html?package=small-group">Book a small-group session</a></div>
    </div>
    <div class="callout">
      <h3>Good fits for small groups</h3>
      <ul class="checklist">
        <li>A team lead and their assistants inside a brokerage</li>
        <li>A home service owner and the office staff who quote, schedule and follow up</li>
        <li>Business partners who want to plan how AI fits before training everyone</li>
      </ul>
    </div>
  </div>
</section>

<section class="white">
  <div class="wrap split">
    <div><h2>What teams practice</h2><p>Every session is adjusted to your industry. These are the tasks that come up most.</p></div>
    <ul class="checklist">
      <li>Client follow-up emails and texts in your voice</li>
      <li>Listing descriptions, service pages and quotes</li>
      <li>A week of social posts and graphics in one sitting</li>
      <li>Replying to reviews and handling common objections</li>
      <li>Summarizing meetings, calls and long documents</li>
      <li>Checking AI output for wrong facts before it goes out</li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>Questions teams ask</h2></div>
    <div class="faq">{faq_html}</div>
  </div>
</section>
'''
page("team-training.html","On-Site AI Team Training in DFW | Local AI Bootcamp",
     "In-person AI training at your office in Dallas–Fort Worth. Hands-on sessions, a written AI use policy and up to 6 months of Slack support for your team.", team)

# ---------------- CLASSES ----------------
classes = f'''
<section class="hero">
  <div class="wrap">
    <h1>Public AI classes around DFW.</h1>
    <p class="lede">Small, hands-on classes hosted at coworking spaces across the metroplex. Buy your own seat, bring your laptop, and work on your own business in class.</p>
    <div class="actions"><a class="btn" href="#list">Get class dates</a></div>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <div class="ladder">
      <div class="rung lead">
        <div><h3>AI Basics for Business</h3><p class="for">One 3-hour class, up to 12 people</p></div>
        <p>Set up the right tools, write real emails and posts for your business, and learn how to catch AI's mistakes. The fastest way to go from curious to actually using it.</p>
        <div class="price">$149<small>per seat</small></div>
      </div>
      <div class="rung">
        <div><h3>4-Week AI Bootcamp</h3><p class="for">Four 3-hour sessions, one per week, up to 10 people</p></div>
        <p>The full course: everyday writing, content and graphics, client follow-up and chatbots, then market research and a simple intro to automation. Includes homework on your own business, templates and 30 days of support after.</p>
        <div class="price">$800<small>per seat</small></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>What the 4-week bootcamp covers</h2></div>
    <div class="steps four">
      <div class="step"><h3>AI basics and quick wins</h3><p>What AI is good and bad at, setting up your tools, and writing professional emails you check yourself.</p></div>
      <div class="step"><h3>Content that sounds like you</h3><p>Prompts for your brand voice, reusable templates, and flyers and posts with Canva's AI features.</p></div>
      <div class="step"><h3>Following up with clients</h3><p>Personal follow-ups, handling objections, simple chatbots and email sequences you review before sending.</p></div>
      <div class="step"><h3>Market insight and next steps</h3><p>Local market research with AI, measuring time saved, an intro to automation, and your 3-month plan.</p></div>
    </div>
  </div>
</section>

<section class="white" id="list">
  <div class="wrap split">
    <div>
      <h2>Get the next class dates</h2>
      <p>Classes are added as coworking venues are confirmed. Tell us where you are and which class you want, and you'll get an email when seats open near you.</p>
    </div>
    {form("class-list","Get class dates", name_email + f_select("area","Closest area",["Dallas","Fort Worth","Plano / Frisco / McKinney","Rockwall / Royse City / Rowlett","Arlington / Mid-Cities","Denton / Lewisville","Somewhere else in DFW"]) + f_select("class","Which class?",["AI Basics for Business (3 hours)","4-Week AI Bootcamp","Not sure yet"]), "You're on the list. You'll get an email when seats open near you.", "One email when new dates are posted. No spam.")}
  </div>
</section>

<section class="ink" id="host">
  <div class="wrap split">
    <div>
      <h2>Run a coworking space? Host a class.</h2>
      <p>Classes bring local business owners through your doors and give your members something worth staying for. Hosts share in ticket revenue, and members get a discount.</p>
    </div>
    <div>
      <ul class="checklist" style="margin-bottom:28px">
        <li>A share of ticket revenue for every class at your space</li>
        <li>Member pricing you can promote as a perk</li>
        <li>Classes promoted to the DFW list, bringing new faces in to tour</li>
        <li>You provide a room, Wi-Fi and a screen. Andrew handles the rest.</li>
      </ul>
      <a class="btn" style="background:var(--note);border-color:var(--note);color:var(--ink)" href="contact.html?package=host">Talk about hosting</a>
    </div>
  </div>
</section>
'''
page("classes.html","AI Classes in Dallas–Fort Worth | Local AI Bootcamp",
     "Small, hands-on AI classes for business owners at coworking spaces across DFW. A 3-hour intro class and a 4-week AI bootcamp.", classes)

# ---------------- AI POLICY ----------------
policy = f'''
<section class="hero">
  <div class="wrap">
    <h1>An AI policy your team will actually read.</h1>
    <p class="lede">Your employees are already using AI, approved or not. A short, plain-English policy tells them which tools are OK, what data stays out, and when a human has to check the work.</p>
    <div class="actions"><a class="btn" href="contact.html?package=policy">Talk about an AI policy</a></div>
  </div>
</section>

<section class="white">
  <div class="wrap split">
    <div>
      <h2>Why it matters now</h2>
      <p>Without rules, people make their own. Someone pastes a client's financials into a free chatbot. Someone sends an AI-written email with a made-up fact in it. Nobody meant any harm, and nobody told them otherwise.</p>
      <p>A policy isn't about slowing people down. It's what lets you say yes to AI with confidence.</p>
    </div>
    <div>
      <h3>What your policy covers</h3>
      <ul class="checklist">
        <li>Approved AI tools and which accounts to use them on</li>
        <li>Data that never goes into AI: client info, financials, passwords, contracts</li>
        <li>When AI output needs a human review before it's sent or published</li>
        <li>How to disclose AI use to clients when it matters</li>
        <li>Who owns the policy and how it gets updated</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>How it gets done</h2></div>
    <div class="steps">
      <div class="step"><h3>Find out what's happening</h3><p>A short survey and conversation to learn which AI tools your team already uses and for what.</p></div>
      <div class="step"><h3>Write the policy</h3><p>A two-to-three page policy in plain language, written for your business and industry, reviewed with your leadership.</p></div>
      <div class="step"><h3>Train the team on it</h3><p>The policy is walked through in person so people understand the why, not just the rules.</p></div>
    </div>
    <div class="callout" style="margin-top:48px">
      <p><strong>Included in every Team Program.</strong> Also available on its own from $2,500. This is practical guidance for small businesses, not legal advice; your attorney should review anything that touches regulated data.</p>
    </div>
  </div>
</section>
'''
page("ai-policy.html","AI Use Policy & Governance for Small Businesses | Local AI Bootcamp",
     "A plain-English AI use policy for your DFW business: approved tools, data rules and human review, plus in-person training so your team follows it.", policy)

# ---------------- ABOUT ----------------
about = f'''
<section class="hero">
  <div class="wrap split">
    <div>
      <h1>Hi, I'm Andrew.</h1>
      <p class="lede">I teach small business owners and their teams how to use AI on the work they already do. In person, at a table, on your own laptop.</p>
    </div>
    <div class="callout">
      <p>Based in Royse City. Training across Dallas, Fort Worth and everywhere in between.</p>
    </div>
  </div>
</section>
<section class="white">
  <div class="wrap split">
    <div>
      <h2>Background</h2>
      <p>I've spent more than 15 years in marketing. I've been head of marketing for 8-figure service companies and a senior marketing director at both bootstrapped and VC-funded software companies.</p>
      <p>I also own and run a local service business here in DFW. AI writes my first drafts, organizes my notes and saves me hours every week, and I've learned where it falls on its face.</p>
    </div>
    <div>
      <h2>Why in person</h2>
      <p>Online AI courses are everywhere, and most people never finish them. What actually works is sitting next to someone while they try it on their own email, their own listing, their own quote, and fixing what goes wrong right there.</p>
      <p>That's what these sessions are. No hype and no jargon, just your work, done faster, with you still in charge of it.</p>
      <div class="actions"><a class="btn" href="contact.html">Book a call</a></div>
    </div>
  </div>
</section>
'''
page("about.html","About Andrew Neal | Local AI Bootcamp",
     "Andrew Neal brings 15+ years of marketing leadership to hands-on, in-person AI training for small businesses in Dallas–Fort Worth.", about)

# ---------------- CONTACT ----------------
contact_fields = name_email + '<div class="field-row">' + f_input("company","Company") + f_input("phone","Phone","tel",req=False,auto="tel") + '</div>' + \
  f_select("interest","What are you interested in?",["Team training at our office","Private small-group session","AI policy for our company","Hosting classes at our coworking space","Public classes","Something else"]) + \
  f_select("team_size","How many people?",["Just me","2–6","7–15","16–40","40+"]) + f_text("message","Anything Andrew should know?")
contact = f'''
<section class="hero">
  <div class="wrap split">
    <div>
      <h1>Let's talk about your team.</h1>
      <p class="lede">Tell Andrew a little about your business. He'll reply within one business day to set up a 30-minute call.</p>
      <p>Prefer email? <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    {form("contact","Send", contact_fields, "Sent. Andrew will reply within one business day to set up a call.")}
  </div>
</section>
<script>
(function(){{var p=new URLSearchParams(location.search).get('package');var m={{workshop:0,program:0,'small-group':1,policy:2,host:3}};
if(p in m){{document.getElementById('interest').selectedIndex=m[p];}}}})();
</script>
'''
page("contact.html","Contact | Local AI Bootcamp",
     "Book a call about in-person AI training for your team in Dallas–Fort Worth.", contact)

# favicon, robots, sitemap
(OUT/"assets/favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#172033"/><rect x="30" y="30" width="26" height="26" fill="#FFD54A" transform="rotate(4 43 43)"/><text x="10" y="40" font-family="Arial Black,Arial" font-weight="900" font-size="26" fill="#fff">AI</text></svg>')
(OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = "".join(f"<url><loc>{SITE}/{'' if p=='index.html' else p[:-5]}</loc></url>" for p in ["index.html","team-training.html","classes.html","ai-policy.html","about.html","contact.html"])
(OUT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
print("built")
