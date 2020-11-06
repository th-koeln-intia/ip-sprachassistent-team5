# Jekyll Dokumentation

Um die Dokumentation lokal zu testen müssen einige Dinge im System vorinstalliert sein.

Da das standardmäßig installierte Theme `minima` mit  `PrettyDocs` ersetzt worden ist, mussten ein paar Änderungen in der `Gemfile`, `_config.yml` und in der Verzeichnisstruktur (`_doc/`) vorgenommen werden.

## Vorraussetzungen

Da die Installation abhängig vom Betriebssystem ist, gibt es hier eine genauere [Anleitung](https://jekyllrb.com/docs/installation/).

Die Schritte sind in etwa:

1. Ruby installieren.
2. Bundler mit Ruby gem installieren und und Per-User-Installation einstellen.
3. Im `docs/` Verzeichnis die Dependencies mit `bundle install` installieren.

   Hier wird alles installiert, was in der `Gemfile` definiert ist.
   **Wichtig**: Es wird außerdem eine `Gemfile.lock` Datei erstellt, die ebenfalls versioniert werden muss.

   Dazu einfach:
   `git add Gemfile*`

## Seite lokal testen

Mit dem serve Kommando kann man die Seite direkt lokal ausführen lassen bevor man pusht, sie ist dann i.d.R. [lokal auf dem Rechner](http://localhost:4000/) unter Port 4000 erreichbar.

```bash
bundle exec jekyll serve
```

Es ist möglich, dass man den `github-pages` Gem nach längerer Zeit mit `bundle update github-pages` updaten muss, damit alles weiterhin einheitlich aussieht.

## Verzeichnisstruktur in `docs/`

Eine genaue Dokumentation zur Verzeichnisstruktur ist [hier](https://jekyllrb.com/docs/structure/) zu finden.

| Datei / Verzeichnis                                          | Beschreibung                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Gemfile](https://bundler.io/gemfile.html)                   | Datei, die alle Dependencies (Gems) enthält, die mit Bundler installiert werden. |
| [_config.yml](https://jekyllrb.com/docs/configuration/)      | Konfigurationsdatei für Jekyll im YAML-Format. Änderungen während `serve` werden nicht berücksichtigt. |
| [CNAME](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain) | Datei mit CNAME DNS Record um Github pages eine benutzerdefinierte Domain mitzuteilen. |
| assets/                                                      | Verzeichnis, das zusätzliche Assets wie z.B. Bilder enthält. |
| **_doc/**                                                    | Selbst erstelltes Verzeichnis mit allen `.md` Dateien und den dazugehörigen Subsections, die in gleichnamigen Verzeichnissen enthalten sind und in der `.md` Datei spezifiziert werden.<br /><br />Standardmäßig sind alle `.md` Dateien auf Root-Ebene, was bei so vielen Dateien und Ordnern unübersichtlich wird. Für die Auslagerung in `_doc` mussten Änderungen in der `_config.yml` Datei vorgenommen werden. Dazu wurden die Mappings `collections` und `defaults` hinzugefügt. |
| _posts/                                                      | Enthält dynamischen Content.<br />Hierbei ist die Namenskonvention für die Dateien zu beachten: `JAHR-MONAT-TAG-titel.md`. |
| _site/                                                       | Enthält die beim `serve` generierte Seite und wird nicht versioniert. |

## PrettyDocs

Um [PrettyDocs](https://github.com/LeakyAbstractions/pretty-docs) zu installieren wurde das Theme `minima` aus der `Gemfile` entfernt und die `_config.yml` Datei so angepasst, dass Jekyll das Theme als `remote_theme` einbindet. 

Mit PrettyDocs kommen noch ein paar weitere Mappings zur `_config.yml` hinzu u.a. `branding`, welches das Logo inkl. Icon generiert. Es gibt noch weitere Mappings, die für Social Plugins genutzt werden können. Es gibt leider keine Dokumentation der Mappings außer das was im [Branch](https://github.com/LeakyAbstractions/pretty-docs/tree/gh-pages) `gh-pages` des Gitrepos spezifiziert ist.

Außerdem bietet das Theme viele vorgefertigte Komponenten, die auf der Beispielseite zu sehen sind aber im Grunde genommen Bootstrap 4 basiert sind, sowie verschiedene Icon-Packs (Font Awesome), Google Fonts und 6 Farbschemata und vieles mehr.

### `_doc/`-Verzeichnis

Im `_doc/`-Verzeichnis haben wir u.a. eine `index.md`-Datei aus der die Startseite generiert wird und alle weiteren`.md`-Dateien per `navigation` mapping einbindet und somit die Navigation generiert. Dies hat nicht funktioniert als die Konfiguration noch alles was im Hauptverzeichnis war eingebunden hat.

In den anderen `.md`-Dateien können wir `title`, `excerpt`, `date`, `icon` und `color` definieren, die sowohl auf die Seite selbst als auch auf das Navigationselement auf der Startseite haben.

Außerdem werden in den anderen `.md`-Dateien mit `sections` Subsections definiert, die in gleichnamigen Verzeichnissen ausgelagert sind.