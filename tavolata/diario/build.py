#!/usr/bin/env python3
# Tavolata devlog ("Diario di sviluppo"): index.html (Italian) and en.html (English).
# Every fact comes from PROJECT.md / PROJECT-STORIA.md of the game repo and the approved press kit. Claude, 25/11/2026.
import html, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
STORE = "https://apps.apple.com/app/id6822874736"
e = lambda s: html.escape(s, quote=True)

EP = {
 "it": [
  ("25/11/2026", "Prossime tappe: Aosta, Torino e Android", "it_04_viaggio.jpg", [
   "Dopo Milano il viaggio continua verso la Valle d'Aosta e il Piemonte. Le prossime città sono Aosta e Torino: livelli, ricette e luoghi da restaurare sono già in preparazione.",
   "Nello stesso periodo Tavolata arriverà anche su Android, dove oggi è in fase di test.",
   "In preparazione ci sono anche due piccole novità: un paesaggio notturno per la schermata iniziale e notifiche più discrete, al massimo una al giorno e mai di notte."]),
  ("24/11/2026", "Milano, la prima città a quartieri", "it_02_restauro.jpg", [
   "Con la versione 1.0.9 arriva Milano, la sesta città del viaggio. È la prima divisa in quartieri: Duomo, Brera, Navigli, Castello e Porta Nuova, con 100 livelli nuovi e 10 luoghi da restaurare.",
   "In tavola arrivano i piatti milanesi: risotto alla milanese, cotoletta, ossobuco con la gremolada, cassoeula, minestrone alla milanese e mondeghili.",
   "Da Milano si cucina sul serio: gli errori consentiti in ogni livello sono pochi e compaiono tessere «incartate», che si aprono solo quando una comanda le chiede.",
   "Cambia anche il Passaporto: raccoglie i timbri di ogni città (arrivo, quartieri, luoghi restaurati) e porta a sette gradi da viaggiatore."]),
  ("22/11/2026", "Feste più impegnative e la Tavolata di Natale", "it_06_vittoria.jpg", [
   "Giocando il Mercatino di Natale di Trento ci siamo accorti che era troppo facile. Con la versione 1.0.8 tutte le Feste e le porticine del Calendario dell'Avvento sono più impegnative.",
   "Le vittorie delle Feste danno ora le tegole di Natale, con cui si restaura, un pezzo a settimana, «La Tavolata di Natale».",
   "Le abitudini di «A tavola in Italia» passano da 12 a 60, e da dicembre arriva la Missione del mese."]),
  ("21/11/2026", "Un Natale lungo, dall'Avvento alla Befana", "it_05_ricettario.jpg", [
   "La versione 1.0.7 porta le Feste: il Mercatino di Natale di Trento e poi una Festa nuova ogni settimana fino al 6 gennaio, con le ricette della tradizione, fino alla Befana.",
   "Dal 1° al 24 dicembre c'è anche il Calendario dell'Avvento, con una porticina da aprire ogni giorno.",
   "Nei giorni prima erano arrivati lo chef che accoglie il giocatore all'apertura, con frasi diverse per ogni città, e le cartoline delle città da condividere."]),
  ("11/11/2026", "Perché Tavolata", "it_01_partita.jpg", [
   "Tavolata nasce da un'idea semplice: un puzzle rilassante che lasci anche qualcosa. Una ricetta vera da cucinare, un luogo da scoprire, una parola della cucina italiana.",
   "In ogni livello si abbinano gli ingredienti per completare le comande: pane, pomodoro e olio fanno una bruschetta. Vincendo si guadagnano le tegole per restaurare i luoghi delle città.",
   "L'11 novembre 2026 Tavolata è uscita su App Store. Il viaggio parte da Firenze e arriverà, una città dopo l'altra, in tutte le 20 regioni d'Italia."]),
 ],
 "en": [
  ("Nov 25, 2026", "Next stops: Aosta, Torino and Android", "en_04_viaggio.jpg", [
   "After Milano the journey heads to the Aosta Valley and Piedmont. The next cities are Aosta and Torino: levels, recipes and landmarks to restore are already in the works.",
   "Around the same time Tavolata will also come to Android, where it is currently in testing.",
   "Two smaller things are also in the works: a night landscape for the home screen and gentler notifications, at most one a day and never at night."]),
  ("Nov 24, 2026", "Milano, the first city with districts", "en_02_restauro.jpg", [
   "Version 1.0.9 brings Milano, the sixth city of the journey. It is the first one divided into districts: Duomo, Brera, Navigli, Castello and Porta Nuova, with 100 new levels and 10 landmarks to restore.",
   "Milanese dishes come to the table: risotto alla milanese, cotoletta, ossobuco with gremolada, cassoeula, minestrone alla milanese and mondeghili.",
   "From Milano on, the cooking gets serious: each level allows only a few mistakes, and new \"wrapped\" tiles only open when an order asks for them.",
   "The Passport changes too: it collects the stamps of every city (arrival, districts, restored landmarks) and leads through seven traveller ranks."]),
  ("Nov 22, 2026", "Tougher festivals and the Christmas Table", "en_06_vittoria.jpg", [
   "Playing the Trento Christmas market, we realised it was too easy. With version 1.0.8 every festival and every door of the Advent calendar is more challenging.",
   "Festival wins now give Christmas roof tiles, used to restore \"The Christmas Table\", one piece a week.",
   "The \"At the table in Italy\" habits grow from 12 to 60, and the Mission of the month starts in December."]),
  ("Nov 21, 2026", "A long Christmas, from Advent to the Befana", "en_05_ricettario.jpg", [
   "Version 1.0.7 brings the festivals: the Trento Christmas market and then a new festival every week until January 6, with traditional recipes, all the way to the Befana.",
   "From December 1 to 24 there is also an Advent calendar, with a door to open every day.",
   "In the days before, the chef started welcoming players when the game opens, with different lines for every city, and city postcards became shareable."]),
  ("Nov 11, 2026", "Why Tavolata", "en_01_partita.jpg", [
   "Tavolata started from a simple idea: a relaxing puzzle that also leaves you with something. A real recipe to cook, a place to discover, a word of Italian cooking.",
   "In every level you match ingredients to complete orders: bread, tomato and olive oil make a bruschetta. Winning earns roof tiles to restore the landmarks of each city.",
   "On November 11, 2026 Tavolata came out on the App Store. The journey starts in Firenze and will reach, one city after another, all 20 regions of Italy."]),
 ]}
UI = {
 "it": dict(file="index.html", other="en.html", oc="EN", title="Diario di sviluppo · Tavolata", h1="Diario di sviluppo",
  lead="Come nasce e come cresce Tavolata, versione dopo versione. Scritto da chi lo sviluppa, in Italia.",
  rec="Ricette", press="Press kit", dl="Scarica gratis", rp="../../ricette/index.html", pk="../press/index.html",
  foot="Tavolata: Puzzle di ricette · un gioco indipendente fatto in Italia", lang="it"),
 "en": dict(file="en.html", other="index.html", oc="IT", title="Devlog · Tavolata", h1="Devlog",
  lead="How Tavolata is made and how it grows, version after version. Written by its developer, in Italy.",
  rec="Recipes", press="Press kit", dl="Free download", rp="../../ricette/en/index.html", pk="../press/en.html",
  foot="Tavolata: Recipe Puzzle · an independent game made in Italy", lang="en")}
for L, U in UI.items():
    posts = ""
    for d, t, img, ps in EP[L]:
        posts += (f'<article class="post"><img src="../press/img/{img}" alt="" loading="lazy"><div><time>{e(d)}</time><h2>{e(t)}</h2>'
                  + "".join(f"<p>{e(p)}</p>" for p in ps) + "</div></article>")
    page = f"""<!doctype html><html lang="{L}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(U['title'])}</title><meta name="description" content="{e(U['lead'])}"><link rel="icon" href="../../ricette/img/site_icon.png"><link rel="stylesheet" href="../../ricette/site.css">
<link rel="alternate" hreflang="it" href="https://gourbergnine07-source.github.io/tavolata/diario/"><link rel="alternate" hreflang="en" href="https://gourbergnine07-source.github.io/tavolata/diario/en.html">
<style>.post{{display:grid;grid-template-columns:180px 1fr;gap:24px;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:20px;margin:18px 0}}
.post img{{width:100%;border-radius:14px;border:1px solid var(--line)}}.post time{{color:var(--acc);font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase}}
.post h2{{font-family:Georgia,serif;font-size:27px;margin:4px 0 8px}}.post p{{margin:8px 0}}
@media (max-width:640px){{.post{{grid-template-columns:1fr}}.post img{{max-width:150px}}}}</style></head><body>
<div class="cloth"></div><header><div class="wrap"><a class="brand" href="{U['rp']}"><img src="../../ricette/img/site_icon.png" alt="">Tavolata</a>
<nav><a href="{U['rp']}">{e(U['rec'])}</a><a class="hide" href="{U['pk']}">{e(U['press'])}</a><a class="lang" href="{U['other']}">{U['oc']}</a><a class="btn hide" href="{STORE}">{e(U['dl'])}</a></nav></div></header>
<main class="wrap"><h1 style="font-family:Georgia,serif;font-size:42px;margin:26px 0 6px">{e(U['h1'])}</h1><p class="lead">{e(U['lead'])}</p>
{posts}</main><footer><div class="wrap"><span>{e(U['foot'])}</span><span class="sp"></span><a href="{U['pk']}">Press kit</a></div></footer><div class="cloth"></div></body></html>
"""
    open(U["file"], "w").write(page)
print("ok")
