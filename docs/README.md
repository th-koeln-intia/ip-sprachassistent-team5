# Dokumentation lokal testen

Um die Dokumentation lokal zu testen müssen eine Dinge im System vorinstalliert sein.

## Vorraussetzungen

https://jekyllrb.com/docs/installation/

1. Ruby installieren.
2. Bundler mit Ruby gem installieren und und Per-User-Installation einstellen.
3. Dependencies mit `bundle install` installieren.

## Seite lokal testen

Mit dem serve Kommando kann man die Seite direkt lokal ausführen lassen bevor man pusht, sie ist dann i.d.R. [lokal auf dem Rechner](http://localhost:4000/) unter Port 4000 erreichbar.

```bash
bundle exec jekyll serve
```

Kann sein, dass man den github-pages Gem nach langer Zeit mit bundle update github-pages updaten muss damit alles weiterhin einheitlich aussieht.