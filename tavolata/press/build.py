#!/usr/bin/env python3
# Builds the Tavolata press kit (index.html = Italian, en.html = English). Claude, 25/11/2026.
# Facts come from the App Store texts of version 1.0.9 and PROJECT.md (verified).
import html, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
STORE = "https://apps.apple.com/app/id6822874736"
e = lambda s: html.escape(s, quote=True)
T = {
 "it": dict(file="index.html", other="en.html", other_code="EN", title="Tavolata · Press kit",
  nav_rec="Ricette", nav_dl="Scarica gratis",
  h1="Press kit", lead="Tutto quello che serve per scrivere di Tavolata: scheda, comunicato, immagini e contatti.",
  facts_h="Scheda", facts=[("Nome", "Tavolata: Puzzle di ricette"), ("Genere", "Puzzle di tessere (tile match) a tema cucina italiana"),
   ("Piattaforme", "iPhone e iPad (App Store) · Android in arrivo"), ("Uscita", "11 novembre 2026"),
   ("Prezzo", "Gratis, con acquisti facoltativi nell'app e pubblicità"), ("Lingue", "Italiano, inglese, francese, spagnolo, portoghese, tedesco, giapponese, cinese tradizionale"),
   ("Contenuti", "6 città, 200 livelli del viaggio, 35 luoghi da restaurare, 62 ricette vere nel Ricettario"),
   ("Sviluppo", "Sviluppatore indipendente, Italia"), ("Sito", "gourbergnine07-source.github.io/ricette")],
  pr_h="Comunicato stampa",
  pr_title="Tavolata, il puzzle che porta in tavola le ricette vere d'Italia",
  pr=["Tavolata è un puzzle di tessere a tema cucina italiana per iPhone e iPad. Il giocatore tocca gli ingredienti nell'ordine giusto per completare le comande: pane, pomodoro e olio fanno una bruschetta. Le tessere sono impilate a strati e ogni mossa conta.",
      "Il gioco è un viaggio in Italia: si parte da Firenze e si passa per Bologna, Venezia, Trieste e Trento fino a Milano, per 6 città, 200 livelli e 35 luoghi da restaurare con le tegole guadagnate vincendo. Ogni città ha i suoi piatti tipici e un Passaporto raccoglie i timbri del viaggio.",
      "Il Ricettario del gioco contiene 62 ricette vere della tradizione, con ingredienti, passaggi e curiosità, consultabili anche gratis sul sito di Tavolata.",
      "Per le feste il gioco ha un Calendario dell'Avvento dal 1° al 24 dicembre e una Festa nuova ogni settimana fino al 6 gennaio, dal Mercatino di Natale di Trento alla Befana.",
      "Tavolata è gratuito su App Store, in 8 lingue, e si gioca anche senza connessione. Sono in arrivo nuove città, a partire da Aosta e Torino, e la versione Android."],
  quote_h="Una frase dello sviluppatore", quote="[Da scrivere: una frase tua su perché hai creato Tavolata]",
  img_h="Immagini", img_p="Tocca un'immagine per aprirla a piena grandezza e salvarla. Puoi usarle per articoli e recensioni di Tavolata.",
  logo_h="Icona e mascotte", contact_h="Contatti", contact="[Da completare: indirizzo email per la stampa]",
  foot="Tavolata: Puzzle di ricette · un gioco indipendente fatto in Italia", lang="it"),
 "en": dict(file="en.html", other="index.html", other_code="IT", title="Tavolata · Press kit",
  nav_rec="Recipes", nav_dl="Free download",
  h1="Press kit", lead="Everything you need to write about Tavolata: fact sheet, press release, images and contacts.",
  facts_h="Fact sheet", facts=[("Name", "Tavolata: Recipe Puzzle"), ("Genre", "Tile match puzzle with an Italian cooking theme"),
   ("Platforms", "iPhone and iPad (App Store) · Android coming"), ("Release", "November 11, 2026"),
   ("Price", "Free, with optional in-app purchases and ads"), ("Languages", "Italian, English, French, Spanish, Portuguese, German, Japanese, Traditional Chinese"),
   ("Content", "6 cities, 200 journey levels, 35 landmarks to restore, 62 real recipes in the Cookbook"),
   ("Developer", "Independent developer, Italy"), ("Website", "gourbergnine07-source.github.io/ricette/en")],
  pr_h="Press release",
  pr_title="Tavolata, the puzzle game that serves real Italian recipes",
  pr=["Tavolata is a tile puzzle with an Italian cooking theme for iPhone and iPad. Players tap ingredients in the right order to complete orders: bread, tomato and olive oil make a bruschetta. Tiles are stacked in layers and every move counts.",
      "The game is a journey through Italy: it starts in Firenze and goes through Bologna, Venezia, Trieste and Trento up to Milano, for 6 cities, 200 levels and 35 landmarks to restore with the roof tiles earned by winning. Every city has its own typical dishes, and a Passport collects the stamps of the journey.",
      "The game's Cookbook holds 62 real traditional recipes, with ingredients, steps and fun facts, also free to read on the Tavolata website.",
      "For the holidays the game has an Advent calendar from December 1 to 24 and a new festival every week until January 6, from the Trento Christmas market to the Befana.",
      "Tavolata is free on the App Store, in 8 languages, and can be played offline. New cities are coming, starting with Aosta and Torino, along with the Android version."],
  quote_h="A word from the developer", quote="[To be written: a sentence from Rodrigue on why he created Tavolata]",
  img_h="Images", img_p="Tap an image to open it full size and save it. You may use them in articles and reviews about Tavolata.",
  logo_h="Icon and mascot", contact_h="Contact", contact="[To be completed: press email address]",
  foot="Tavolata: Recipe Puzzle · an independent game made in Italy", lang="en")}
SHOTS = ["01_partita", "02_restauro", "04_viaggio", "05_ricettario", "06_vittoria"]
for L in T.values():
    facts = "".join(f"<tr><th>{e(a)}</th><td>{e(b)}</td></tr>" for a, b in L["facts"])
    shots = "".join(f'<a href="img/{L["lang"]}_{s}.jpg" target="_blank"><img src="img/{L["lang"]}_{s}.jpg" alt="" loading="lazy"></a>' for s in SHOTS)
    page = f"""<!doctype html><html lang="{L['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(L['title'])}</title><meta name="description" content="{e(L['lead'])}"><link rel="icon" href="../../ricette/img/site_icon.png"><link rel="stylesheet" href="../../ricette/site.css">
<style>.pk table{{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}}
.pk th,.pk td{{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top}}.pk th{{width:32%;color:var(--muted);font-weight:600}}
.shots{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}}.shots img{{width:100%;border-radius:14px;border:1px solid var(--line)}}
.logos{{display:flex;gap:20px;align-items:end;flex-wrap:wrap}}.logos img{{height:160px;border-radius:24px}}
.pr{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px 24px}}.pr h3{{font-family:Georgia,serif;font-size:24px;margin:0 0 10px}}
.todo{{background:#fff3cd;color:#5c4400;border-radius:8px;padding:8px 12px;display:inline-block}}</style></head><body>
<div class="cloth"></div><header><div class="wrap"><a class="brand" href="../../ricette/{'' if L['lang']=='it' else 'en/'}index.html"><img src="../../ricette/img/site_icon.png" alt="">Tavolata</a>
<nav><a href="../../ricette/{'' if L['lang']=='it' else 'en/'}index.html">{e(L['nav_rec'])}</a><a class="lang" href="{L['other']}">{L['other_code']}</a><a class="btn hide" href="{STORE}">{e(L['nav_dl'])}</a></nav></div></header>
<main class="wrap pk"><h1 style="font-family:Georgia,serif;font-size:42px;margin:26px 0 6px">{e(L['h1'])}</h1><p class="lead">{e(L['lead'])}</p>
<h2 class="h">{e(L['facts_h'])}</h2><table>{facts}</table>
<h2 class="h">{e(L['pr_h'])}</h2><div class="pr"><h3>{e(L['pr_title'])}</h3>{''.join(f'<p>{e(p)}</p>' for p in L['pr'])}
<p><b>{e(L['quote_h'])}:</b> <span class="todo">{e(L['quote'])}</span></p></div>
<h2 class="h">{e(L['img_h'])}</h2><p class="small">{e(L['img_p'])}</p><div class="shots">{shots}</div>
<h2 class="h">{e(L['logo_h'])}</h2><div class="logos"><a href="img/tavolata_icona_1024.png" target="_blank"><img src="img/tavolata_icona_1024.png" alt="Tavolata"></a><a href="img/tavolata_chef.png" target="_blank"><img src="img/tavolata_chef.png" alt="Chef" style="border-radius:0"></a></div>
<h2 class="h">{e(L['contact_h'])}</h2><p><span class="todo">{e(L['contact'])}</span> · App Store: <a href="{STORE}">apps.apple.com/app/id6822874736</a></p>
</main><footer><div class="wrap"><span>{e(L['foot'])}</span></div></footer><div class="cloth"></div></body></html>
"""
    open(L["file"], "w").write(page)
print("ok")
