# Tank Battle

How to install:
1. Download zip folder
2. Unzip it (extract all), save the items to your local disk (C:\\).
3. Move the file called "Tank_Battle_Simulator.py" to "C:\Users\Your-Username\AppData\Local\Programs\Python\Python-version_number-32_or_64_bit" (example: "C:\Users\John\AppData\Local\Programs\Python\Python39-64"), but keep the rest of the files where they are.
4. Type "import Tank_Battle_Simulator" into your python shell to run the game!

Note: You MUST save the Tank_Battle_Simulator folder directly to your local disk (C:\\), so that the path to it becomes "C:\Tank_Battle_Simulator". If you don't do this, your game will not work, because it will not be able to find the sound files/images included in the folder.

Instructions:
1. Arrow keys to move
2. Space key to fire (you can only fire forward)
3. Press q to activate/deactivate your personal shield. You cannot fire if your shield is on. Also, the shield will only protect your front side.
4. Destroy the other tank to win.

Game Sounds and Music (links will take you to the sites where I downloaded them from):
1. [Game music: Legend of Zelda Breath of the Wild Shrine Battle Music](https://downloads.khinsider.com/game-soundtracks/album/legend-of-zelda-the-breath-of-the-wild-original-soundtrack/1-09.%2520Battle%2520%2528Shrine%2529-%2520Original%2520Soundtrack%2520Ver..mp3)
2. [Minecraft "oof" sound for when you or the enemy gets hit](https://orangefreesounds.com/minecraft-death-sound/)
3. [Explosion sound for when your HP or the enemy's reaches 0](https://www.zapsplat.com/music/double-large-explosions-with-some-very-light-distortion/)
4. [Star Wars blaster sound for when you or the enemy shoots](https://soundbible.com/470-Laser-Blaster.html)
5. [winsound.Beep() for the "3 2 1 go" part at the beginning](https://docs.python.org/3/library/winsound.html)

Additional Notes:
1. The graphics are kind of simple... when you shoot, it may look like it hits, even though the game doesn't count it as a hit. But don't shoot from too close or too far; you basically need to skewer the enemy all the way through for it to count, and your tank cannot be touching the enemy when it happens.
2. If you want to save your scores, you'll have to do it manually. When the game ends, it will automatically copy the results, and you can paste it into your own text file. But, again, you'll have to manually do it - the game won't save your score. (Sorry! If it really bugs you, just say so and I will try to fix it).
3. You will also have to manually close the program and reopen it if you want to play it again. (Again, if it irritates you, I can try fix it).
4. If, at the end of the game, the shell gives you an error message saying "list index out of range", don't mind it, it usually happens but does not seem to interfere with the game's functioning.
5. The "tanks" are supposed to resemble [DJI's Robomaster S1](https://www.dji.com/robomaster-s1).
6. New versions and edits of the game may come out soon :)
7. Any suggestions, questions, or comments are welcome.
8. And, as always, have fun!

Credits:

Explosion Image: https://scratch.mit.edu/projects/107636750

Background remove tool used for explosion image: https://remove.bg

Help with code:
1. https://stackoverflow.com/questions/29849138/while-loop-not-working-while-using-tkinter
2. https://stackoverflow.com/questions/55069520/cant-play-mp3-file-using-winsound-on-windows
3. https://stackoverflow.com/questions/42393916/how-can-i-play-multiple-sounds-at-the-same-time-in-pygame
4. https://stackoverflow.com/questions/43400856/change-the-color-of-an-object-after-tkinter-has-been-initiated
5. https://stackoverflow.com/questions/42593589/cant-access-global-variable-from-inside-a-function-in-python
6. https://stackoverflow.com/questions/15753793/how-to-bind-spacebar-key-to-a-certain-method-in-tkinter-python
7. https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
8. https://stackoverflow.com/questions/46131369/how-to-stop-sound-in-pygame
9. https://stackoverflow.com/questions/3177969/how-to-resize-an-image-using-tkinter
10. https://stackoverflow.com/questions/26479728/tkinter-canvas-image-not-displaying
11. https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas
12. https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard
