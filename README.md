# Python code that suggests you are unlikely to win the Euromillions Lottery jackpot

(…or any other state, national or international lottery for that matter!)

I know: the Europe-wide Euromillions Lottery pays tens of millions of the finest in European currencies to lucky jackpot winners every few weeks. Next time could it be you? More importantly, could it be me?

So I set out to prove this one way or another and wrote a Python 3 program to play a simulation of the Euromillions lottery over and over as fast as it could to see what would happen. You are welcome to run the code on your computer. too.

Just some information about the Euromillions lottery, as the program was tuned to play this particular game:

1. To  play Euromillions, you choose five different numbers ('balls') between 1 and 50 then two more different ‘Lucky Stars’ numbers between 1 and 11
2. For each line you play, you pay £2 (GBP)
3. The odds of matching all the numbers and winning the jackpot is 1: 139,838,160 (so 140 million to one against this happening)
4. You can match fewer numbers and stars with better odds (current odds and payout percentage available on this link as of October 2016)

The Python 3 program I’ve written  in this repo allows you to play a single line of 5 numbers and 2 Lucky Stars. You can set the numbers in a variable called wantedBalls, the stars in wantedStars, and the amount of money starting in your account in totalBank at the top of the program script.

The program will then run until the money runs out from your account. So if you have £1million to spend, set totalBank to a value of 1000000, which will make the program play 400,000 lotteries at 2.50 per play.

I’ve set the winning values based on average win amounts – so the average jackpot win is £44,992,371. The averages are bound to change over time, and you can make alterations to your winnings in the function called WhatDidWeWin() – but leave it for now and let’s get winning the lottery!

To run the program:

1. Open a command-prompt or terminal window
2. Test that Python 3 is installed by running the command:<pre>python --version</pre>. If it is not installed, you’ll just get an error, and you need to download Python 3 (not Python 2) from the Python web site (or use your package manager for Linux for example “sudo apt-get python3“).
You may find that running this command shows that you have Python 2 installed! In which case try <pre>python3 --version</pre>If that works, you can run the script with command 'python3' rather than 'python' 
3. When Python is installed you’ll be welcomed by the Python3 interpreter. Type the command ‘quit()’ <return> to exit.
4. Copy the Python program to your Desktop as notalotto.py
5. If you have some favourite numbers, change them in the two variables wantedBalls and wantedStars at the top of the script before you save the file. When entering your own numbers, store them in ascending numeric order. This speeds up the results-checking by the Python code so the lotteries are played faster For example:

<pre>
wantedBalls = (3, 4, 5, 14, 28) # spot on - ball numbers are in ascending order
</pre> ...and <b><i>not</i></b> <pre>wantedBalls = (5, 14, 28, 3, 4)  # don't do this - balls must be in the ascending order
</pre>
The are two more values you are welcome to change:
The totalBank variable stores a value of the toal money to spend. When you run the simulation, this amount is divided equally amongst the number of threads you wish to run in parallel.
Set the total amount to spend in totalBank and the number of threads to run the simulation in parallel in variable numberOfThreads, both at the top of the script.
The more threads you set, the faster the simulation will run up to the physical limit of the number of CPU cores built into your particular computer. You can run even more threads if
your CPU is not being utilised 100%.


## Run the simulator
At the command-line change directory to your Desktop (usually as simple as “cd Desktop“!)
Run the command: <pre>python notalotto.py</pre> ..or.. <pre>python3 notalotto.py</pre> and watch the lotteries play! 

Every 5 seconds, a dashboard will update you with how the lottery simulation is progressing. Here I am running it with 16 threads:
<pre>
|-------|--------------------|--------------|---------------|
| Thrd# |  Lotteries played  |  Prize Haul  |    Money Left |
|-------|--------------------|--------------|---------------|
|   0   |           610000   | £224,061.18  |    £30,000.00 |    
|   1   |           590000   | £223,716.44  |    £70,000.00 |    
|   2   |           600000   | £220,199.46  |    £50,000.00 |    
|   3   |           580000   | £571,426.92  |    £90,000.00 |    
|   4   |           580000   | £210,065.30  |    £90,000.00 |    
|   5   |           600000   | £220,208.15  |    £50,000.00 |    
|   6   |           550000   | £201,700.77  |   £150,000.00 |    
|   7   |           550000   | £248,359.62  |   £150,000.00 |    
|   8   |           570000   | £206,199.11  |   £110,000.00 |    
|   9   |           580000   | £212,600.22  |    £90,000.00 |    
|  10   |           600000   | £221,382.37  |    £50,000.00 |    
|  11   |           590000   | £217,710.54  |    £70,000.00 |    
|  12   |           560000   | £206,995.56  |   £130,000.00 |    
|  13   |           580000   | £217,142.82  |    £90,000.00 |    
|  14   |           590000   | £220,602.26  |    £70,000.00 |    
|  15   |           580000   | £218,232.20  |    £90,000.00 |    
|-------|--------------------|--------------|---------------|
</pre> 
It's interesting to see what thread is winning the most money.

Following the above instructions, here is what happened to me just now.
I played 10 million lotteries because I had 20 million in currency at the start.
I didn't win the jackpot (5 balls + 2 stars matching) but I came close with 5 balls and 1 star.
Overall I won £148,520.38 but, because I spent £20m, I lost over £15m!
<pre>
Completed!
Time taken: 0:05:12.320797
Total lotteries played: 10,000,000
Total money spent playing: 20,000,000
Amount won: 4,142,042.98
Net won (minus if lost): -15,857,957.02
Win counts (balls + stars matched):
5 + 2: 0
5 + 1: 1
5 + 0: 3
4 + 2: 19
4 + 1: 342
4 + 0: 699
3 + 2: 856
3 + 1: 30592
2 + 2: 12175
3 + 0: 0
1 + 2: 64028
2 + 1: 218411
2 + 0: 438100
Lost!: 9219861

</pre>

All this serves to prove that the probability of being a net winner when you play a lottery game is poor indeed.  But don’t stop playing the Lottery as long as you do it for fun. Some of your loss goes to the good causes which are a good thing. Play for fun only, and when that fun stops, stop.(OK, my lawyers?)

Sorry, another disclaimer: I should also point out that my lottery simulator is just that: A simulator. That means that my coding is my interpretation of the rules and odds; it has not been quality-assured by the lottery regulator or lottery licensee Camelot as being an accurate reflection of the odds and winnings. Also remember that any standard computer program can’t generate truly random numbers without special hardware. The random number generator in Python 3 is pseudo-random. That means there is a possibility that a pattern could be detected if you tested its randomness enough times, affecting outcomes. That’s why lotteries use physical balls mixed and tumbled so that the choice is truly random.

