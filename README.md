#Python code that suggests you are unlikely to win the Euromillions Lottery jackpot

(…or any other state, national or international lottery for that matter!)

I know: the Europe-wide Euromillions Lottery pays tens of millions of the finest in European currencies to lucky jackpot winners every few weeks. Next time could it be you? More importantly, could it be me?

So I set out to prove this one way or another and wrote a Python 3 program to play a simulation of the Euromillions lottery over and over as fast as it could to see what would happen. You are welcome to run the code on your computer. too.

Just some information about the Euromillions lottery, as the program was tuned to play this particular game:

1. To  play Euromillions, you choose five different numbers between 1 and 50 then two more different ‘Lucky Stars’ numbers between 1 and 12
2. For each line you play, you pay £2.50 (GBP)
3. The odds of matching all the numbers and winning the jackpot is 1: 139,838,160 (so 140 million to one against this happening)
4. You can match fewer numbers and stars with better odds (current odds and payout percentage available on this link as of October 2016)

The Python 3 program I’ve written at the bottom of this article allows you to play a single line of 5 numbers and 2 Lucky Stars. You can set the numbers in a variable called wantedballs, the stars in wantedStars, and the amount of money starting in your account in totalBank at the top of the program script.

The program will then run until the money runs out from your account. So if you have £1million to spend, set totalBank to a value of 1000000, which will make the program play 400,000 lotteries at 2.50 per play.

I’ve set the winning values based on average win amounts – so the average jackpot win is £44,992,371. The averages are bound to change over time, and you can make alterations to your winnings in the function called WhatDidWeWin() – but leave it for now and let’s get winning the lottery!

To run the program:

1. Open a command-prompt or terminal window
2. Test that Python 3 is installed by running the command:<pre>python -v</pre>. If it is not installed, you’ll just get an error, and you need to download Python 3 (not Python 2) from the Python web site (or use your package manager for Linux for example “sudo apt-get python3“).
You may find that running this command shows that you have Python 2 installed! In which case try <pre>python3 -v</pre>If that works, you can run the script with command 'python3' rather than 'python' 
3. When Python is installed you’ll be welcomed by the Python3 interpreter. Type the command ‘quit()’ <return> to exit.
4. Copy the Python program from the bottom of this article to a text editor and save it to your Desktop as euromillionssim.py
5. If you have some favourite numbers, change them in the two variables wantedBalls and wantedStars at the top of the script before you save the file. When entering your own numbers, store them in ascending numeric order. This speeds up the results-checking by the Python code so the lotteries are played faster For example:

<pre>
wantedballs = (3, 4, 5, 14, 28) # spot on - ball numbers are in ascending order
</pre> ...and <b><i>not</i></b> <pre>wantedballs = (5, 14, 28, 3, 4)  # don't do this - balls must be in the ascending order
</pre>
At the command-line change directory to your Desktop (usually as simple as “cd Desktop“!)

## Run the simulator
Run the command: <pre>python notalotto.py</pre> ..or.. <pre>python3 notalotto.py</pre> and watch the lotteries play!

Following the above instructions, here is what happened to me just now:
<pre>
Last login: Sat Oct 1 10:58:48 on ttys000
Nicks-Mac-Pro:~ nick$ python3
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
Nicks-Mac-Pro:~ nick$ cd Desktop
Nicks-Mac-Pro:Desktop nick$ python3 euromillionssim.py
Euromillions simulator v1.0 by Nick Lansley
Lottery ticket numbers are (set in script): balls: (3, 4, 5, 14, 28) stars: (5, 7)
Playing....
Total lotteries played so far: 10,000
Total lotteries played so far: 20,000
Total lotteries played so far: 30,000
... (edited for article length!) ...
Total lotteries played so far: 390,000
Total lotteries played so far: 400,000
Completed!
Time taken: 0:00:46.764576
Total lotteries played: 400,000
Total money spent playing: £1,000,000
Amount won: £148,520.38
Net won (minus if lost): £-851,479.62
Win counts (balls + stars matched):
5 + 2: 0
5 + 1: 1
5 + 0: 0
4 + 2: 1
4 + 1: 13
4 + 0: 28
3 + 2: 32
3 + 1: 600
2 + 2: 507
3 + 0: 1211
1 + 2: 2540
2 + 1: 8705
2 + 0: 17657
Lost!: 368705
Nicks-Mac-Pro:Desktop nick$

</pre>
## Reviewing the output
Let’s review the output from the run output above:

1. I played 400,000 lottery games in 46.7 seconds
2. The money I spent was £1,000,000
3. I won £148,520.38 – very nice!
4. …but, because I spent £1million, my net loss was £-851,479.62
5. I notice I came ‘close’ to the jackpot because, in one game, I matched 5 balls + 1 star.
6. On the other hand, I lost 368,705 times!

All this serves to prove that the probability of being a net winner when you play a lottery game is poor indeed.  But don’t stop playing the Lottery as long as you do it for fun. Some of your loss goes to the good causes which are a good thing. Play for fun only, and when that fun stops, stop.(OK, my lawyers?)

Sorry, another disclaimer: I should also point out that my lottery simulator is just that: A simulator. That means that my coding is my interpretation of the rules and odds; it has not been quality-assured by the lottery regulator or lottery licensee Camelot as being an accurate reflection of the odds and winnings. Also remember that any standard computer program can’t generate truly random numbers without special hardware. The random number generator in Python 3 is pseudo-random. That means there is a possibility that a pattern could be detected if you tested its randomness enough times, affecting outcomes. That’s why lotteries use physical balls mixed and tumbled so that the choice is truly random.

Try this: Look at the time it takes for your computer to play the default 400,000 lotteries (46.7 seconds in my case) then calculate the amount to put into your account for the lottery to play for hours. If I left my computer running overnight playing from 10pm to 7am (9 hours) then I would need to add:

(400,000 plays / 46.7 seconds)  x  £2.50 per play  x  60 seconds in a minute  x  60 minutes in an hour  x  9 hours = 693790149

So I would need to set totalBank to a value of 693790149  (£693,790,149) to play through the night on my computer.

Your computer will get hot doing this so make sure there’s plenty of ventilation. If trying this on a laptop place it on a stand to get maximum air circulation around it, particularly on its underside.