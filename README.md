# ReadMe zum Code "Online-Buchhandlung"

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

Hierbei handelt es sich um ein Praxisprojekt, welches wir innerhalb des Kurses gemacht haben. Hier habe ich mit verschiedenen Klassen gearbeitet, um eine Online-Buchhandlung zu simulieren. Zu Beginn wird der Kunde nach seiner E-Mail Adresse gefragt, welche danach mit den hinterlegten Adressen verglichen wird. Ist die Adresse vorhanden, wird der Kunde mit seinem Namen begrüßt. Falls nicht, wird der Kunde nach seinem Namen gefragt und wird danach begrüßt.

Danach hat Kunde bzw. der Codeuser hat im Hauptmenü folgende Möglichkeiten:
1. Buch suchen
2. Buch kaufen
3. Sammlung ansehen
4. Wunschliste ansehen
5. Bücher auf Wunschliste kaufen
6. Beenden

## Buch suchen
Der Kunde kann mithilfe eines Suchbegriffes ein Buch suchen. Im Hintergrund wird überprüft, ob das gesuchte Keyword mit einem der Bücher im Bestand übereinstimmt. 
Ist das gesuchte Buch bzw. Keyword nicht verfügbar (nicht in der .json-Datei hinterlegt), kann es sich der Kunde auf die Wunschliste setzen. Dies funktioniert jedoch auch bei Büchern, die sich im Bestand befinden

## Buch kaufen   
Hier wird dem Kunden eine Bestandsliste der Buchhandlung gezeigt. Diese ist derzeit auf 3 Bücher von Sebastian Fitzek beschränkt, ist aber beliebig erweiterbar. Die Liste ist in einer .json-Datei verpackt, um den Code nicht mit unnötigen Informationen zu überlasten. 

## Sammlung ansehen
In diesem Menü-Punkt werden dem Kunden die Bücher gezeigt, die er im Menüpunkt 2 (_Buch kaufen_) gekauft hat.

## Wunschliste anzeigen
Ist eines der gesuchten Bücher bzw. Keywords aus Menüpunkt 1 (_Buch suchen_) auf die Wunschliste gesetzt worden, können sie hier abgerufen werden.

## Bücher auf Wunschliste kaufen
Möchte der Kunde prüfen, ob eines der Bücher auf seiner Wunschliste verfügbar ist, kann er dies mit dieser Funktion tun. Hier kann er das gewünschte Element auswählen, welches direkt ähnlich wie Menüpunkt 1 (_Buch suchen_) in der Bestandsliste gesucht wird.

## Beenden
Beendet das Programm mit einer Verabschiedung des Kunden.



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/flo130522/Online-Buchhandlung.svg?style=for-the-badge
[contributors-url]: https://github.com/flo130522/Online-Buchhandlung/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/flo130522/Online-Buchhandlung.svg?style=for-the-badge
[forks-url]: https://github.com/flo130522/Online-Buchhandlung/network/members
[stars-shield]: https://img.shields.io/github/stars/flo130522/Online-Buchhandlung.svg?style=for-the-badge
[stars-url]: https://github.com/flo130522/Online-Buchhandlung/stargazers
[issues-shield]: https://img.shields.io/github/issues/flo130522/Online-Buchhandlung.svg?style=for-the-badge
[issues-url]: https://github.com/flo130522/Online-Buchhandlung/issues
[license-shield]: https://img.shields.io/github/license/flo130522/Online-Buchhandlung.svg?style=for-the-badge
[license-url]: https://github.com/flo130522/Online-Buchhandlung/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/flokurek
