# Professional layout of the Tavolata press kit (used by build.py). Claude, 26/11/2026.
# All facts come from build.py / l10n_more.py (already verified); this file only adds the page design and UI words.
import html, os, zipfile
from PIL import Image

e = lambda s: html.escape(s, quote=True)
STORE = "https://apps.apple.com/app/id6822874736"
PINTEREST = "https://www.pinterest.com/tavolata0126/"
LANGS = [("it", "Italiano"), ("en", "English"), ("fr", "Français"), ("es", "Español"), ("pt", "Português"), ("de", "Deutsch"), ("ja", "日本語"), ("zh", "繁體中文")]
HL = {"zh": "zh-Hant"}
SHOTS = ["01_partita", "02_restauro", "04_viaggio", "05_ricettario", "06_vittoria"]

UI = {
 "it": dict(trailer_p="30 secondi di gioco vero, con le schermate del gioco e una musica originale, senza voce: pronto per articoli, video e social.", eyebrow="Press kit · Materiale per la stampa", dl_all="Scarica tutto (ZIP)", watch="Guarda il trailer", dl="Scarica",
   stats=["città", "livelli", "ricette vere", "lingue", "regioni nel viaggio"], trailer="Trailer",
   caps=["Partita", "Restauro della città", "Viaggio in Italia", "Ricettario", "Vittoria"],
   icon_c="Icona dell'app · PNG 1024 × 1024", chef_c="Lo chef, la mascotte · PNG",
   contact_p="Per interviste, informazioni o materiale aggiuntivo:", dateline="Italia, novembre 2026", recipes="Le ricette", diary="Diario di sviluppo"),
 "en": dict(trailer_p="30 seconds of real gameplay screens with original music and no voice-over: ready for articles, videos and social media.", eyebrow="Press kit · Media resources", dl_all="Download all (ZIP)", watch="Watch the trailer", dl="Download",
   stats=["cities", "levels", "real recipes", "languages", "regions on the journey"], trailer="Trailer",
   caps=["Gameplay", "City restoration", "Journey across Italy", "Cookbook", "Victory"],
   icon_c="App icon · PNG 1024 × 1024", chef_c="The chef mascot · PNG",
   contact_p="For interviews, information or additional material:", dateline="Italy, November 2026", recipes="Recipes", diary="Devlog"),
 "fr": dict(trailer_p="30 secondes d'écrans du jeu avec une musique originale, sans voix off : prête pour vos articles, vidéos et réseaux sociaux.", eyebrow="Kit presse · Ressources médias", dl_all="Tout télécharger (ZIP)", watch="Voir la bande-annonce", dl="Télécharger",
   stats=["villes", "niveaux", "vraies recettes", "langues", "régions du voyage"], trailer="Bande-annonce",
   caps=["Partie", "Restauration de la ville", "Voyage en Italie", "Livre de recettes", "Victoire"],
   icon_c="Icône de l'app · PNG 1024 × 1024", chef_c="Le chef, la mascotte · PNG",
   contact_p="Pour une interview, des informations ou du matériel supplémentaire :", dateline="Italie, novembre 2026", recipes="Recettes", diary="Journal de développement"),
 "es": dict(trailer_p="30 segundos con pantallas reales del juego y música original, sin voz: listo para artículos, vídeos y redes sociales.", eyebrow="Kit de prensa · Recursos para medios", dl_all="Descargar todo (ZIP)", watch="Ver el tráiler", dl="Descargar",
   stats=["ciudades", "niveles", "recetas auténticas", "idiomas", "regiones en el viaje"], trailer="Tráiler",
   caps=["Partida", "Restauración de la ciudad", "Viaje por Italia", "Recetario", "Victoria"],
   icon_c="Icono de la app · PNG 1024 × 1024", chef_c="El chef, la mascota · PNG",
   contact_p="Para entrevistas, información o material adicional:", dateline="Italia, noviembre de 2026", recipes="Recetas", diary="Diario de desarrollo"),
 "pt": dict(trailer_p="30 segundos com telas reais do jogo e música original, sem narração: pronto para artigos, vídeos e redes sociais.", eyebrow="Kit de imprensa · Recursos para a mídia", dl_all="Baixar tudo (ZIP)", watch="Ver o trailer", dl="Baixar",
   stats=["cidades", "níveis", "receitas verdadeiras", "idiomas", "regiões na viagem"], trailer="Trailer",
   caps=["Partida", "Restauração da cidade", "Viagem pela Itália", "Livro de receitas", "Vitória"],
   icon_c="Ícone do app · PNG 1024 × 1024", chef_c="O chef, o mascote · PNG",
   contact_p="Para entrevistas, informações ou material adicional:", dateline="Itália, novembro de 2026", recipes="Receitas", diary="Diário de desenvolvimento"),
 "de": dict(trailer_p="30 Sekunden echte Spielszenen mit eigener Musik, ohne Sprecher: bereit für Artikel, Videos und soziale Medien.", eyebrow="Pressemappe · Medienmaterial", dl_all="Alles herunterladen (ZIP)", watch="Trailer ansehen", dl="Herunterladen",
   stats=["Städte", "Level", "echte Rezepte", "Sprachen", "Regionen der Reise"], trailer="Trailer",
   caps=["Spiel", "Stadt restaurieren", "Reise durch Italien", "Rezeptbuch", "Sieg"],
   icon_c="App-Icon · PNG 1024 × 1024", chef_c="Der Koch, das Maskottchen · PNG",
   contact_p="Für Interviews, Informationen oder weiteres Material:", dateline="Italien, November 2026", recipes="Rezepte", diary="Entwicklertagebuch"),
 "ja": dict(trailer_p="実際のゲーム画面とオリジナル音楽による30秒の映像（ナレーションなし）。記事・動画・SNSにご利用いただけます。", eyebrow="プレスキット · メディア向け資料", dl_all="すべてダウンロード（ZIP）", watch="トレーラーを見る", dl="ダウンロード",
   stats=["都市", "レベル", "本物のレシピ", "言語", "旅する州"], trailer="トレーラー",
   caps=["プレイ画面", "街の修復", "イタリアの旅", "レシピ帳", "勝利"],
   icon_c="アプリアイコン · PNG 1024 × 1024", chef_c="マスコットのシェフ · PNG",
   contact_p="取材・お問い合わせ・追加素材のご依頼：", dateline="イタリア、2026年11月", recipes="レシピ", diary="開発日記"),
 "zh": dict(trailer_p="30 秒真實遊戲畫面搭配原創音樂，無旁白：可直接用於文章、影片與社群媒體。", eyebrow="媒體資料包 · 媒體素材", dl_all="全部下載（ZIP）", watch="觀看預告片", dl="下載",
   stats=["座城市", "個關卡", "道真正食譜", "種語言", "個大區之旅"], trailer="預告片",
   caps=["遊戲畫面", "修復城市", "義大利之旅", "食譜", "勝利"],
   icon_c="App 圖示 · PNG 1024 × 1024", chef_c="吉祥物主廚 · PNG",
   contact_p="採訪、詢問或索取更多素材：", dateline="義大利，2026 年 11 月", recipes="食譜", diary="開發日誌"),
}
NUMS = ["6", "200", "62", "8", "20"]

CSS = """
:root{--cream:#f7f1e8;--paper:#fffdf9;--ink:#271c17;--muted:#6f625a;--line:#e7ddd0;--tomato:#c8452f;--tomato-d:#a3361f;--deep:#2b1711;--deep2:#43231a;--olive:#5d6b39;--gold:#e2b65a}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:72px}
body{margin:0;background:var(--cream);color:var(--ink);font:16px/1.65 "Inter",system-ui,-apple-system,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}img{max-width:100%;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
.serif{font-family:"Fraunces",Georgia,serif}
/* top bar */
.top{position:sticky;top:0;z-index:20;background:rgba(43,23,17,.92);backdrop-filter:saturate(1.4) blur(10px);-webkit-backdrop-filter:saturate(1.4) blur(10px);color:#f6ede2;border-bottom:1px solid rgba(255,255,255,.08)}
.top .wrap{display:flex;align-items:center;gap:22px;height:64px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:"Fraunces",Georgia,serif;font-weight:700;font-size:20px;letter-spacing:.2px}
.brand img{width:34px;height:34px;border-radius:9px}
.secnav{display:flex;gap:18px;margin-left:12px;font-size:14px;overflow-x:auto;scrollbar-width:none}.secnav::-webkit-scrollbar{display:none}
.secnav a{text-decoration:none;opacity:.78;white-space:nowrap}.secnav a:hover{opacity:1}
.sp{flex:1}
.lang{font:inherit;font-size:13px;background:transparent;color:#f6ede2;border:1px solid rgba(255,255,255,.25);border-radius:8px;padding:5px 8px}
.lang option{color:#222}
.btn{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:600;font-size:15px;border-radius:999px;padding:12px 22px;border:1px solid transparent;transition:.15s}
.btn.pri{background:var(--tomato);color:#fff}.btn.pri:hover{background:var(--tomato-d)}
.btn.ghost{border-color:rgba(255,255,255,.35);color:#fff}.btn.ghost:hover{background:rgba(255,255,255,.08)}
.btn.dark{background:var(--ink);color:#fff}.btn.dark:hover{background:#000}
.btn.line{border-color:var(--line);background:var(--paper);color:var(--ink)}.btn.line:hover{border-color:var(--tomato);color:var(--tomato)}
.btn svg{width:18px;height:18px}
/* hero */
.hero{background:radial-gradient(1200px 600px at 85% 10%,#5a2c1e 0%,transparent 60%),linear-gradient(160deg,var(--deep2),var(--deep));color:#f6ede2;overflow:hidden;position:relative}
.hero:after{content:"";position:absolute;inset:auto 0 0 0;height:10px;background:repeating-linear-gradient(90deg,var(--tomato) 0 14px,transparent 14px 28px)}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center;padding-top:72px;padding-bottom:84px}
.eyebrow{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:18px}
.hero h1{font-family:"Fraunces",Georgia,serif;font-weight:700;font-size:clamp(40px,6vw,68px);line-height:1.02;margin:0 0 6px;letter-spacing:-.5px}
.hero .sub{font-family:"Fraunces",Georgia,serif;font-style:italic;font-size:clamp(20px,2.4vw,26px);color:#f0c9a8;margin:0 0 18px}
.hero p.lead{font-size:18px;color:#e7d9cb;max-width:540px;margin:0 0 28px}
.cta{display:flex;flex-wrap:wrap;gap:12px}
.stats{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-top:40px;border-top:1px solid rgba(255,255,255,.14);padding-top:22px;max-width:560px}
.stats div{padding-right:10px}.stats b{display:block;font-family:"Fraunces",Georgia,serif;font-size:34px;line-height:1;color:#fff}
.stats span{font-size:12.5px;color:#d5c3b2;line-height:1.3;display:block;margin-top:6px}
.phones{position:relative;height:560px}
.phone{position:absolute;width:236px;border-radius:38px;padding:9px;background:#120a07;box-shadow:0 30px 60px rgba(0,0,0,.45),0 0 0 1px rgba(255,255,255,.08) inset}
.phone img{border-radius:30px;width:100%}
.phone.c{left:50%;top:10px;transform:translateX(-50%);z-index:3;width:256px}
.phone.l{left:2%;top:70px;transform:rotate(-8deg);z-index:2;opacity:.96}
.phone.r{right:2%;top:70px;transform:rotate(8deg);z-index:2;opacity:.96}
/* sections */
section.s{padding:84px 0;border-bottom:1px solid var(--line)}
.kicker{font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--tomato);margin:0 0 10px}
h2{font-family:"Fraunces",Georgia,serif;font-weight:700;font-size:clamp(30px,3.6vw,42px);line-height:1.1;margin:0 0 28px;letter-spacing:-.3px}
.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:18px;overflow:hidden}
.fact{background:var(--paper);padding:22px 24px}.fact.wide{grid-column:span 3}.fact.span2{grid-column:span 2}.fact dd a{color:var(--tomato);text-decoration:none}
.fact dt{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.fact dd{margin:0;font-size:16px}
.release{display:grid;grid-template-columns:1fr 300px;gap:56px;align-items:start}
.release article{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:44px 48px}
.release h3{font-family:"Fraunces",Georgia,serif;font-size:30px;line-height:1.2;margin:0 0 18px}
.dateline{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--tomato);margin-bottom:14px}
.release p{margin:0 0 16px;font-size:17px}
.release aside{position:sticky;top:96px}
blockquote{margin:0;font-family:"Fraunces",Georgia,serif;font-style:italic;font-size:22px;line-height:1.45;color:var(--ink);border-left:4px solid var(--tomato);padding:4px 0 4px 22px}
blockquote cite{display:block;margin-top:14px;font-family:"Inter",sans-serif;font-style:normal;font-size:13px;font-weight:600;color:var(--muted);letter-spacing:.06em;text-transform:uppercase}
.trailer{display:grid;grid-template-columns:340px 1fr;gap:56px;align-items:center}
.trailer video{width:100%;border-radius:28px;background:#000;box-shadow:0 24px 50px rgba(43,23,17,.25)}
.trailer p{font-size:17px;color:var(--muted);max-width:460px}
.shots{display:grid;grid-template-columns:repeat(5,1fr);gap:20px}
.shot figure{margin:0}.shot .frame{display:block;border-radius:26px;padding:7px;background:#1b110d;box-shadow:0 14px 30px rgba(43,23,17,.18)}
.shot .frame img{border-radius:20px}
.shot figcaption{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:12px;font-size:14px;font-weight:600}
.shot figcaption a{font-weight:500;color:var(--tomato);text-decoration:none;font-size:13px;white-space:nowrap}
.note{font-size:14px;color:var(--muted);margin:-12px 0 28px}
.assets{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;max-width:820px}
.asset{border:1px solid var(--line);border-radius:20px;overflow:hidden;background:var(--paper)}
.asset .pv{height:240px;display:flex;align-items:center;justify-content:center}
.asset .pv.light{background:#f3ece1}.asset .pv.dark{background:linear-gradient(160deg,var(--deep2),var(--deep))}
.asset .pv img{max-height:190px;width:auto}.asset .pv img.icon{border-radius:40px;box-shadow:0 12px 26px rgba(0,0,0,.25)}
.asset .meta{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;font-size:14px;font-weight:600;gap:10px}
.asset .meta a{color:var(--tomato);text-decoration:none;font-weight:500;font-size:13px}
.contact{display:grid;grid-template-columns:1.2fr .8fr;gap:24px;align-items:stretch}
.card{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:34px 36px}
.card .mail{font-family:"Fraunces",Georgia,serif;font-size:clamp(22px,3vw,30px);font-weight:700;text-decoration:none;color:var(--tomato);word-break:break-all}
.links{list-style:none;margin:0;padding:0}.links li{border-top:1px solid var(--line)}.links li:first-child{border-top:0}
.links a{display:flex;justify-content:space-between;padding:12px 0;text-decoration:none;font-weight:500}.links a:after{content:"→";color:var(--tomato)}
footer.f{background:var(--deep);color:#d9c8b8;font-size:14px;padding:34px 0}
footer.f .wrap{display:flex;flex-wrap:wrap;gap:18px;align-items:center}footer.f a{text-decoration:none;opacity:.85}
@media (max-width:980px){.hero .wrap{grid-template-columns:1fr;padding-top:48px}.phones{height:440px}.phone{width:180px}.phone.c{width:200px}
 .release{grid-template-columns:1fr}.release aside{position:static}.trailer{grid-template-columns:1fr}.trailer video{max-width:340px}
 .shots{grid-template-columns:repeat(3,1fr)}.assets{grid-template-columns:1fr 1fr}.contact{grid-template-columns:1fr}.secnav{display:none}}
@media (max-width:640px){.wrap{padding:0 16px}.facts{grid-template-columns:1fr}.fact.wide,.fact.span2{grid-column:auto}.stats{grid-template-columns:repeat(3,1fr);row-gap:18px}
 .release article{padding:28px 22px}.shots{grid-template-columns:1fr 1fr}.assets{grid-template-columns:1fr}.phones{height:360px}.phone{width:140px;border-radius:26px;padding:6px}.phone img{border-radius:21px}.phone.c{width:160px}
 section.s{padding:60px 0}.top .btn{display:none}}
"""

ICON_DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>'
ICON_PLAY = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
ICON_APPLE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.3.8c1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.8-1-2.8-4.3zM14 5.3c.7-.8 1.2-2 1-3.1-1 0-2.2.7-2.9 1.5-.6.7-1.2 1.9-1 3 1.1.1 2.2-.6 2.9-1.4z"/></svg>'


def thumbs():
    os.makedirs("img/thumb", exist_ok=True)
    for f in os.listdir("img"):
        if f.endswith(".jpg"):
            out = "img/thumb/" + f
            if not os.path.exists(out):
                im = Image.open("img/" + f).convert("RGB"); im.thumbnail((600, 1400)); im.save(out, quality=84, optimize=True)


def build_zip(T):
    with zipfile.ZipFile("Tavolata_press_kit.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.write("img/tavolata_icona_1024.png", "Tavolata/logo/tavolata_icona_1024.png")
        z.write("img/tavolata_chef.png", "Tavolata/logo/tavolata_chef.png")
        for lang, _ in LANGS:
            for s in SHOTS:
                z.write(f"img/{lang}_{s}.jpg", f"Tavolata/screenshots/{lang}/{lang}_{s}.jpg")
            L = T[lang]
            txt = L["pr_title"] + "\n\n" + "\n\n".join(L["pr"]) + "\n\n" + L["quote_h"] + ": " + L["quote"] + "\n\n" + \
                  "\n".join(f"{a}: {b}" for a, b in L["facts"]) + f"\n\nEmail: tavolata07@gmail.com\nApp Store: {STORE}\n"
            z.writestr(f"Tavolata/press_release/press_release_{lang}.txt", txt)
        for v in ("it", "en"):
            z.write(f"video/Tavolata_trailer_{v}.mp4", f"Tavolata/trailer/Tavolata_trailer_{v}.mp4")


def page(L, T):
    lang = L["lang"]; U = UI[lang]; vl = "it" if lang == "it" else "en"
    rec = "../../ricette/" + ("" if lang == "it" else lang + "/") + "index.html"
    dia = "../diario/" + ("index" if lang == "it" else "en") + ".html"
    opts = "".join(f'<option value="{T[c]["file"]}"{" selected" if c == lang else ""}>{n}</option>' for c, n in LANGS)
    alts = "".join(f'<link rel="alternate" hreflang="{HL.get(c, c)}" href="https://gourbergnine07-source.github.io/tavolata/press/{T[c]["file"] if c != "it" else ""}">' for c, _ in LANGS)
    facts = L["facts"]
    def cell(i, a, b):
        if i == len(facts) - 1:
            url = "https://" + b
            return f'<div class="fact span2"><dt>{e(a)}</dt><dd><a href="{e(url)}">{e(b)}</a></dd></div>'
        return f'<div class="fact{" wide" if i == 6 else ""}"><dt>{e(a)}</dt><dd>{e(b)}</dd></div>'
    cells = "".join(cell(i, a, b) for i, (a, b) in enumerate(facts))
    stats = "".join(f"<div><b>{n}</b><span>{e(t)}</span></div>" for n, t in zip(NUMS, U["stats"]))
    shots = "".join(
        f'<div class="shot"><figure><a class="frame" href="img/{lang}_{s}.jpg" target="_blank"><img src="img/thumb/{lang}_{s}.jpg" alt="{e(c)}" loading="lazy"></a>'
        f'<figcaption>{e(c)}<a href="img/{lang}_{s}.jpg" download>{e(U["dl"])} ↓</a></figcaption></figure></div>' for s, c in zip(SHOTS, U["caps"]))
    secs = [("scheda", L["facts_h"]), ("comunicato", L["pr_h"]), ("trailer", U["trailer"]), ("immagini", L["img_h"]), ("logo", L["logo_h"]), ("contatti", L["contact_h"])]
    nav = "".join(f'<a href="#{i}">{e(t)}</a>' for i, t in secs)
    pr = "".join(f"<p>{e(p)}</p>" for p in L["pr"])
    quote = L["quote"].strip("«»“”「」„\"")
    return f"""<!doctype html><html lang="{HL.get(lang, lang)}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(L['title'])}</title><meta name="description" content="{e(L['lead'])}">{alts}
<meta property="og:title" content="{e(L['title'])}"><meta property="og:description" content="{e(L['lead'])}"><meta property="og:image" content="https://gourbergnine07-source.github.io/tavolata/press/img/tavolata_icona_1024.png">
<link rel="icon" href="img/tavolata_icona_1024.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header class="top"><div class="wrap"><a class="brand" href="{rec}"><img src="img/tavolata_icona_1024.png" alt="">Tavolata</a><nav class="secnav">{nav}</nav><span class="sp"></span>
<select class="lang" aria-label="Language" onchange="location.href=this.value">{opts}</select><a class="btn pri" href="Tavolata_press_kit.zip" download>{ICON_DL}{e(U['dl_all'])}</a></div></header>
<section class="hero"><div class="wrap"><div><span class="eyebrow">{e(U['eyebrow'])}</span><h1>Tavolata</h1><p class="sub">{e(L['facts'][0][1].split(':', 1)[-1].split('：', 1)[-1].strip())}</p>
<p class="lead">{e(L['pr_title'])}</p><div class="cta"><a class="btn pri" href="Tavolata_press_kit.zip" download>{ICON_DL}{e(U['dl_all'])}</a><a class="btn ghost" href="#trailer">{ICON_PLAY}{e(U['watch'])}</a><a class="btn ghost" href="{STORE}">{ICON_APPLE}App Store</a></div>
<div class="stats">{stats}</div></div>
<div class="phones" aria-hidden="true"><div class="phone l"><img src="img/thumb/{lang}_05_ricettario.jpg" alt=""></div><div class="phone r"><img src="img/thumb/{lang}_02_restauro.jpg" alt=""></div><div class="phone c"><img src="img/thumb/{lang}_01_partita.jpg" alt=""></div></div></div></section>
<main>
<section class="s" id="scheda"><div class="wrap"><p class="kicker">01</p><h2>{e(L['facts_h'])}</h2><dl class="facts">{cells}</dl></div></section>
<section class="s" id="comunicato"><div class="wrap"><p class="kicker">02</p><h2>{e(L['pr_h'])}</h2><div class="release"><article><div class="dateline">{e(U['dateline'])}</div><h3>{e(L['pr_title'])}</h3>{pr}</article>
<aside><blockquote>{e(quote)}<cite>{e(L['quote_h'])}</cite></blockquote></aside></div></div></section>
<section class="s" id="trailer"><div class="wrap trailer"><video controls playsinline preload="metadata" poster="video/poster_{vl}.jpg"><source src="video/Tavolata_trailer_{vl}.mp4" type="video/mp4"></video>
<div><p class="kicker">03</p><h2>{e(U['trailer'])}</h2><p>{e(U['trailer_p'])}</p><a class="btn line" href="video/Tavolata_trailer_{vl}.mp4" download>{ICON_DL}{e(U['dl'])} · MP4 1080 × 1920</a></div></div></section>
<section class="s" id="immagini"><div class="wrap"><p class="kicker">04</p><h2>{e(L['img_h'])}</h2><p class="note">{e(L['img_p'])}</p><div class="shots">{shots}</div></div></section>
<section class="s" id="logo"><div class="wrap"><p class="kicker">05</p><h2>{e(L['logo_h'])}</h2><div class="assets">
<div class="asset"><div class="pv light"><img class="icon" src="img/tavolata_icona_1024.png" alt="Tavolata"></div><div class="meta">{e(U['icon_c'])}<a href="img/tavolata_icona_1024.png" download>{e(U['dl'])} ↓</a></div></div>
<div class="asset"><div class="pv dark"><img src="img/tavolata_chef.png" alt="Chef"></div><div class="meta">{e(U['chef_c'])}<a href="img/tavolata_chef.png" download>{e(U['dl'])} ↓</a></div></div>
</div></div></section>
<section class="s" id="contatti"><div class="wrap"><p class="kicker">06</p><h2>{e(L['contact_h'])}</h2><div class="contact"><div class="card"><p style="margin:0 0 10px;color:var(--muted)">{e(U['contact_p'])}</p><a class="mail" href="mailto:tavolata07@gmail.com">tavolata07@gmail.com</a>
<div class="cta" style="margin-top:24px"><a class="btn dark" href="{STORE}">{ICON_APPLE}App Store</a><a class="btn line" href="Tavolata_press_kit.zip" download>{ICON_DL}{e(U['dl_all'])}</a></div></div>
<div class="card"><ul class="links"><li><a href="{rec}">{e(U['recipes'])}</a></li><li><a href="{dia}">{e(U['diary'])}</a></li><li><a href="{PINTEREST}">Pinterest</a></li><li><a href="https://www.instagram.com/tavolata.game.official/">Instagram</a></li><li><a href="https://www.tiktok.com/@tavolata.game.official">TikTok</a></li><li><a href="https://www.youtube.com/channel/UCom5s1w9BMZgBJ99r7sOwbg">YouTube</a></li></ul></div></div></div></section>
</main><footer class="f"><div class="wrap"><span>{e(L['foot'])}</span><span class="sp"></span><a href="{rec}">{e(U['recipes'])}</a><a href="{dia}">{e(U['diary'])}</a><a href="{STORE}">App Store</a></div></footer></body></html>
"""
