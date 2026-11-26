#!/usr/bin/env python3
# Builds the Tavolata press kit (index.html = Italian, <lang>.html = the other 7 game languages). Claude, 25/11/2026; new layout in layout.py (26/11/2026).
# Facts come from the App Store texts of version 1.0.9 and PROJECT.md (verified).
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l10n_more import MORE
os.chdir(os.path.dirname(os.path.abspath(__file__)))
STORE = "https://apps.apple.com/app/id6822874736"
e = lambda s: html.escape(s, quote=True)
T = {
 "it": dict(file="index.html", title="Tavolata · Press kit",
  nav_rec="Ricette", nav_dl="Scarica gratis",
  h1="Press kit", lead="Tutto quello che serve per scrivere di Tavolata: scheda, comunicato, immagini e contatti.",
  facts_h="Scheda", facts=[("Nome", "Tavolata: Puzzle di ricette"), ("Genere", "Puzzle di tessere (tile match) a tema cucina italiana"),
   ("Piattaforme", "iPhone e iPad (App Store) · Android in arrivo"), ("Uscita", "11 novembre 2026"),
   ("Prezzo", "Gratis, con acquisti facoltativi nell'app e pubblicità"), ("Lingue", "Italiano, inglese, francese, spagnolo, portoghese, tedesco, giapponese, cinese tradizionale"),
   ("Contenuti", "Oggi 6 città, 200 livelli del viaggio, 35 luoghi da restaurare e 62 ricette vere nel Ricettario. Il viaggio toccherà tutte le 20 regioni d'Italia, con le città nuove in arrivo una dopo l'altra"),
   ("Sviluppo", "Sviluppatore indipendente, Italia"), ("Sito", "gourbergnine07-source.github.io/ricette")],
  pr_h="Comunicato stampa",
  pr_title="Tavolata, il puzzle che porta in tavola le ricette vere d'Italia",
  pr=["Tavolata è un puzzle di tessere a tema cucina italiana per iPhone e iPad. Il giocatore tocca gli ingredienti nell'ordine giusto per completare le comande: pane, pomodoro e olio fanno una bruschetta. Le tessere sono impilate a strati e ogni mossa conta.",
      "Il gioco è un viaggio in Italia: si parte da Firenze e si passa per Bologna, Venezia, Trieste e Trento fino a Milano, per 6 città, 200 livelli e 35 luoghi da restaurare con le tegole guadagnate vincendo. Ogni città ha i suoi piatti tipici e un Passaporto raccoglie i timbri del viaggio. In tutto il viaggio toccherà le 20 regioni d'Italia, da nord a sud fino alle isole, con una città per regione.",
      "Il Ricettario del gioco contiene 62 ricette vere della tradizione, con ingredienti, passaggi e curiosità, consultabili anche gratis sul sito di Tavolata.",
      "Per le feste il gioco ha un Calendario dell'Avvento dal 1° al 24 dicembre e una Festa nuova ogni settimana fino al 6 gennaio, dal Mercatino di Natale di Trento alla Befana.",
      "Tavolata è gratuito su App Store, in 8 lingue, e si gioca anche senza connessione. Le città nuove arrivano una dopo l'altra, a partire da Aosta e Torino, insieme alla versione Android."],
  quote_h="Una frase dello sviluppatore", quote="«Volevo un puzzle semplice e rilassante che lasciasse anche qualcosa: una ricetta vera da cucinare, un luogo da scoprire, una parola della cucina italiana. In Tavolata ogni livello è un passo di un viaggio a tavola attraverso tutta l'Italia.»",
  img_h="Immagini", img_p="Tocca un'immagine per aprirla a piena grandezza e salvarla. Puoi usarle per articoli e recensioni di Tavolata.",
  logo_h="Icona e mascotte", contact_h="Contatti", contact="tavolata07@gmail.com",
  foot="Tavolata: Puzzle di ricette · un gioco indipendente fatto in Italia", lang="it"),
 "en": dict(file="en.html", title="Tavolata · Press kit",
  nav_rec="Recipes", nav_dl="Free download",
  h1="Press kit", lead="Everything you need to write about Tavolata: fact sheet, press release, images and contacts.",
  facts_h="Fact sheet", facts=[("Name", "Tavolata: Recipe Puzzle"), ("Genre", "Tile match puzzle with an Italian cooking theme"),
   ("Platforms", "iPhone and iPad (App Store) · Android coming"), ("Release", "November 11, 2026"),
   ("Price", "Free, with optional in-app purchases and ads"), ("Languages", "Italian, English, French, Spanish, Portuguese, German, Japanese, Traditional Chinese"),
   ("Content", "Today 6 cities, 200 journey levels, 35 landmarks to restore and 62 real recipes in the Cookbook. The journey will cover all 20 regions of Italy, with new cities arriving one after another"),
   ("Developer", "Independent developer, Italy"), ("Website", "gourbergnine07-source.github.io/ricette/en")],
  pr_h="Press release",
  pr_title="Tavolata, the puzzle game that serves real Italian recipes",
  pr=["Tavolata is a tile puzzle with an Italian cooking theme for iPhone and iPad. Players tap ingredients in the right order to complete orders: bread, tomato and olive oil make a bruschetta. Tiles are stacked in layers and every move counts.",
      "The game is a journey through Italy: it starts in Firenze and goes through Bologna, Venezia, Trieste and Trento up to Milano, for 6 cities, 200 levels and 35 landmarks to restore with the roof tiles earned by winning. Every city has its own typical dishes, and a Passport collects the stamps of the journey. In total the journey will cover all 20 regions of Italy, from north to south and the islands, with one city per region.",
      "The game's Cookbook holds 62 real traditional recipes, with ingredients, steps and fun facts, also free to read on the Tavolata website.",
      "For the holidays the game has an Advent calendar from December 1 to 24 and a new festival every week until January 6, from the Trento Christmas market to the Befana.",
      "Tavolata is free on the App Store, in 8 languages, and can be played offline. New cities arrive one after another, starting with Aosta and Torino, along with the Android version."],
  quote_h="A word from the developer", quote="“I wanted a simple, relaxing puzzle that also leaves you with something: a real recipe to cook, a place to discover, a word of Italian cooking. In Tavolata every level is a step of a journey at the table across all of Italy.”",
  img_h="Images", img_p="Tap an image to open it full size and save it. You may use them in articles and reviews about Tavolata.",
  logo_h="Icon and mascot", contact_h="Contact", contact="tavolata07@gmail.com",
  foot="Tavolata: Recipe Puzzle · an independent game made in Italy", lang="en")}
for k, v in MORE.items():
    T[k] = dict(v, file=k + ".html", lang=k, contact="tavolata07@gmail.com")
import layout
layout.thumbs()
for L in T.values():
    open(L["file"], "w").write(layout.page(L, T))
layout.build_zip(T)
print("ok")
