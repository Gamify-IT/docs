# Generell
  - [DOKU] Wie darstellen? Wiki/ README/ markdown/ pdf?
  - [DOKU] Zentraler Ort für Doku
Sollte beinhalten:
  - [DOKU] Dev Tutorial: Examples for adding a new minigame, Architektur, Testingstruktur, Wie Projekt runnen
  - Toggl Time Track: Wenn etwas zu lange dauert am Besten mittels Toggl nachweisebar, selbst wenn nichts vorhanden
  - ADR: Architecural Decision Records: gemeinsam getroffene Architekturentscheidungen und warum. Template auf https://adr.github.io/madr/ : Beschreib das Problem mit Pro und Contra,
  - (Overkill: readthedocs)
  - Nutzerhandbuch (wie der User das bedienen kann): "Er muss es halt verstehen".
  - Pro service sauberes README: wie starten, wie aufgebaut,...
  - Protokolle: kleiner Mitschrieb der Meetingergebnisse und wer was gemacht hat -> zum Argumentieren.
  - Pro Review: Präsentation bauen mit Fortschritten, und was zu erwarten ist. Vielleicht auch SonarQube Statistiken als Screenshot einbauen.
  - Zum Startreview: Liste der Rollen, und wann genau minimal running example zu erwarten ist.
  - wie Projektalltag gestalten?
  - Aufwandsschätzung / Storypoints  / Planning Poker -> mit Storypoints können gut Taskdauern geschätzt werden, wenn ein Storypoint ca. 5 Stunden (oder weniger, je nach Gusto)
     - kein Task größer als X: In Subtasks runterbrechen
  - Planning und Refinement: jedem muss am Anfang klar sein, was muss getan werden. Außerdem empfehlenswert: Experten(gebiete) aufbauen.
  - Zweiwochensprints empfehlenswert
  - Review: x Tasks erledigt, y Storypoints geschätzt, bspw. wenn mir die Leute ihre Toggl Zeiten schicken (I-Tüpfelchen).
    - Ich gebe groben Überblick: Was wurde erledigt?
    - Weitergeben an die einzelnen Implementierer: Wie wurde es genau erledigt?
    - Klausurphasen und Sommerurlaube einplanen! (Bspw. weil in einer Woche nur 3 da sind)
  - Doku Repo: Wie service adden, Dev Doku, User Doku, (readthedocs...), setup, CI/ CD (i.e. Jenkins/ SonarQube), IDE setup, ADR, ReST API
  - Meilensteine/ Releases: Frei wählbar, hier vermutlich nicht so sinnvoll, MVP
  - Bezüglich Deployen: Vielleicht mal BW Cloud anfragen, kann aber Downtime geben weil gratis
  - Discord Bot für notifications? Eher nicht.
  - Doku Sachen an Doku verantwortlichen weiterleiten.
  - Wie Reviewfolien aufbauen:
     - Agenda: Übersicht
     - Ziele: Was ist passiert? Was wurde sich vorgenommen? Wurde es implementiert? Wenn nein, warum?
     - Falls vorhanden: Events (i.e. Entwickler verlässt Team)
     - Zahlen: wie viele Tickets insgesamt, ...
     - Kuhn Diagramm?
     - SonarQube Statistics -> Für DevOps, also Iliaz, aber erst, wenn alles funktioniert
     - Präsentation der jeweils eigenen Features von den Entwicklern
     - Next steps
     - Aufs Wesentliche konzentrieren
     - (Retrospektive)