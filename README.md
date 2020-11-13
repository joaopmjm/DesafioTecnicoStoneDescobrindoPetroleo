# Desafio Tecnico Stone - Descobrindo Petroleo

Participant: Joao Pedro Montefeltro Junqueira Meirelles

made on python (version >= 3.6.9)
Dependencies for working, Python3 installed and TKinter Library aswell.

to run:
if you are on Win10 and just have python3 downloaded:
    python main.py

if you on linux or have python2 in parallel, should probably run:
    python3 main.py

the input needed is a .txt file with the following format (commands.txt is an exemple that works):

input.txt
5 5                 # First Line, size of the area, X and Y
1 3 N               # Second Line, initial X and Y of one Ship and Where it's facing (Only takes N, E, W, S)
MMLMRMLM            # Third Line, ships movemente, 'M' move forward, 'L' turn left without moving and 'R' turn right without moving

only this 3 lines is needed to work, if you want more ships, repeat the lines numebers 2 and 3, and adapt them to the other ships.

Disregards:
    -Collision of ships not applied
    -Ships can't go beyond the border, if tries to, it doesn't move.
    -Input file must be execlty as expected