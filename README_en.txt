DESCRIPTION OF THE HARMONIZATION ALGORITHM IMPLEMENTATION

1. Requirements

Python 3.10.4 or later



2. How to run

Use a command: "python3 main.py [X]" in the project folder (there may be a different command in place of python3, depending on python installation details)
X is an optional seed number that is responsible for which solutions the algorithm will choose
by default it is set on 3 because of the subjectively best sounding solutions selected by the algorithm
After starting, the program asks for a sequence of functions or a cadence



3. Input format - sequence of functions

Functions are given as codes:

T           Tonic
S           Subdominant
S6          Subdominant with sixth
mollS       Minor subdominant (flat third in major tonation)
D           Dominant
D64         Dominant with sixth instead of fifth and fourth instead of third
D7          Dominant with seventh
D7n1        D7 without prime (double fifth)
D7n5        D7 without fifth (double prime)
Dch         Chopin's dominant (sixth in soprano instead of fifth)
D9          D7 with none (lack of fifth)
D9n1        D7 with none (lack of prime)
SII         Second degree subdominant
SN          Neapolitan subdominant (minor second flat degree subdominant) 
mollDVII    Seventh degree minor dominant
DIII        Third degree dominant
TIII        Third degree tonic
TVI         Sixth degree tonic
mollTVIobn  Sixth flat degree minor tonic
SVI         Sixth degree subdominant

Additionally, by adding the X$dN (X$uN) character attribute, we can obtain the appropriate inversion (position) of the X chord, establishing the N component in the bass (soprano)



4. Input format - cadence

In order to use a cadence, its name must be entered after starting the program
There are five cadences demonstrating the different mechanisms:

I.   perfectCadence - fundamental harmonic triad
	 corresponds to the input: "T S$d1 D$d1 T"
	 
II.  characteristicFunctionsCadence - characteristic harmonic functions: S6, D64, D7, D9 and interpreting upper and lower limits provided on input
	 corresponds to the input: "T$u5 T$d3 S S6 D64 D D7 D9 T"
	 
III. auxDegreesCadence - auxiliary degrees chord functions: TIII, TVI, SII, DIII and a deceptive solution (with the Chopin dominant)
	 corresponds to the input: "T TIII S SII D DIII D7 Dch TVI S D64 D T"
	 
IV.  mollChordsCadence - moll functions test: neapolitan subdominant, moll subdominant and tonic VI flat degree
	 corresponds to the input: "T mollS D D7 mollTVIobn SN D T"
	 
V.   incompleteChordsCadence - incomplete chord test: D7 without 1, D7 without 5 and D9 without 1
	 corresponds to the input: "T S D7n5 D7n1 T S6 D9 D9n1 T"
	 
	 
	 
5. Output format

There are two parts of output:

I.		sequence of chords in format "(B, T, A, S)", line by line on the standard output

II.		sample.musicxml file, that presents data in a universal music format
		this allows you to see the result on the staff and play it, for example, in the musescore program
