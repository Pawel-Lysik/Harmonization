OPIS IMPLEMENTACJI ALGORYTMU AUTOMATYCZNEJ HARMONIZACJI

1. Wymagania

Python w wersji 3.10.4, lub nowszej



2. Uruchomienie programu

W celu uruchomienia programu należy użyć komendy: "python3 main.py [X]" w folderze z projektem (w miejscu python3 może być inna komenda, w zależności od szczegółów installacji python)
X to opcjonalny numer seed odpowiadający za to, które rozwiązania będzie wybierał algorytm
domyślnie jest on ustawiony na 3 (z powodu subiektywnie najlepszego brzmienia wybranych przez algorytm rozwiązań)
Po uruchomieniu program prosi o podanie kadencji, lub ciągu funkcji



3. Format wejścia - ciąg funkcji

Funkcje są podawane w podstaci kodów:

T           Tonika
S           Subdominanta
S6          Subdominanta z sekstą
mollS       Moll subdominanta (obniżona tercja w tonacjach durowych)
D           Dominanta
D64         Dominanta z sekstą zamiast kwinty i kwartą zamiast tercji
D7          Dominanta septymowa
D7n1        D7 bez prymy (podwojona kwinta)
D7n5        D7 bez kwinty (podwojona pryma)
Dch         Dominanta Chopinowska (zamiast kwinty, seksta w sopranie)
D9          Dominanta nonowa (bez kwinty)
D9n1        Dominanta nonowa bez prymy
SII         Subdominanta drugiego stopnia
SN          Subdominanta neapolitańska (moll subdominanta drugiego stopnia obniżonego)
mollDVII    Moll dominanta siódmego stopnia obniżonego
DIII        Dominanta trzeciego stopnia
TIII        Tonika trzeciego stopnia
TVI         Tonika szóstego stopnia
mollTVIobn  Moll tonika szóstego stopnia obniżonego
SVI         Subdominanta szóstego stopnia obniżonego

Dodatkowo poprzez dodanie atrybutu postaci X$dN (X$uN) możemy uzyskać odpowiedni przewrót (pozycję) akordu X, ustalając składnik N w basie (sopranie)



4. Format wejścia - kadencja

Skorzystanie z kadencji wymaga podania jej nazwy po uruchomieniu programu
Przygotowałem pięć kadencji demonstrujących poszczególne mechanizmy:

I.   perfectCadence - podstawowa triada harmoniczna, przykład z tekstu pracy
	 odpowiada wejściu: "T S$d1 D$d1 T"
	 
II.  characteristicFunctionsCadence - funkcje charakterystyczne: S6, D64, D7, D9 oraz mechanizm ograniczeń górnych i dolnych dostarczonych na wejściu
	 odpowiada wejściu: "T$u5 T$d3 S S6 D64 D D7 D9 T"
	 
III. auxDegreesCadence - funkcje akordów pobocznych: TIII, TVI, SII, DIII oraz rozwiązanie zwodnicze (w wariancie z dominantą chopinowską)
	 odpowiada wejściu: "T TIII S SII D DIII D7 Dch TVI S D64 D T"
	 
IV.  mollChordsCadence - funkcje mollowe: test wersji mollowych akordów, tj. subdominanta neapolitańska, moll subdominanta i tonika VI st. obniżonego
	 odpowiada wejściu: "T mollS D D7 mollTVIobn SN D T"
	 
V.   incompleteChordsCadence - test akordów niepełnych: D7 bez 1, D7 bez 5 oraz D9 bez 1
	 odpowiada wejściu: "T S D7n5 D7n1 T S6 D9 D9n1 T"
	 
	 
	 
5. Format wyjścia

Wyjście składa się z dwóch części:

I.		ciąg akordów w postaci "(B, T, A, S)" w kolejnych liniach na standardowym wyjściu

II.		plik sample.musicxml prezentujący dane w uniwersalnym formacie muzycznym
		pozwala to na zobaczenie wyniku działania na pięciolini oraz odtworzenie go na przykład w programie musescore
