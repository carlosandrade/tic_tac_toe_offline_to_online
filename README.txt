This is a very, VERY, simple attempt to use a 2 human player tic tac toe code and make it an online tic tac toe using two different hosts using python.

Offline tictactoe is available here: http://www.geekstogo.com/forum/topic/148200-python-tic-tac-toe-game-2-player/

Gamecon class was used and adapted to this code from: http://python.org.br/wiki/PequenoUsoDeSockets


Other useful sources: http://docs.python.org/howto/sockets.html

Code is functional and may be run on two different machines. Code organization and performance need a lot of fixes since it wasn't the main goal of this practice (main goal was moving the tic tac toe from offline to online with the simplest modifications as possible, or maybe more dull). 

Both client and server are inside velhaonline.py so execution requires only python velhaonline.py 

I've added a modification to original GameCon so it provides the ip that the other user will need to connect to the server machine. 

This ip should be used on my Csocket code as well. 

