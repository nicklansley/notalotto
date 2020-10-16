# Python 3
import random
import datetime
import time
import threading
import locale

# Set to your computer's local currency
locale.setlocale( locale.LC_ALL, '' )

# global variables you set to play this game:
# Set your favourite numbers into the two lists below, in ascending order (so 1, 2, 3, 4, 5 not 3, 5, 2, 4, 1):
wantedBalls = (3, 4, 5, 14, 28)  # Your Euromillions chosen numbers
wantedStars = (5, 7)  # Your Euromillions chosen stars

# Add some money to your 'bank account':
totalBank = 20000000  # this is the amount of money in your bank you spend at 2 units per lottery until it is empty!

# We can run lotteries in parallel - here decide how many simultaneous lottery draws you wish
# (speeds up program execution)
numberOfThreads = 16

# OK, now save the script and run it with a Python 3.x (not 2.x) interpreter!
# Let's see how much you win / lose!

# internal use variables
all_lotteryCount = 0
all_totalPrize = 0
win5s2 = 0
win5s1 = 0
win5s0 = 0
win4s2 = 0
win4s1 = 0
win4s0 = 0
win3s2 = 0
win3s1 = 0
win2s2 = 0
win3s0 = 0
win1s2 = 0
win2s1 = 0
win2s0 = 0
winFail = 0

startTime = 0
endTime = 0

originalBank = 0
threadList = []
threadData = []

# This threadLock variable will be used to ensure only one thread is printing to the screen
# or updating global variables at a time
threadLock = threading.Lock()

# This lotteryThread class stores the mechanics of running lottery draws
class lotteryThread (threading.Thread):

    # Run a single lottery draw
    def RunLotteryDraw(self):

        # Shuffle the list of 50 ball and 11 star possible values
        random.shuffle(self.ballPossibleValuesList)
        random.shuffle(self.starPossibleValuesList)

        # Now the list is shuffled, we'll take the ball values from these positions
        self.lotteryDrawBalls = (self.ballPossibleValuesList[1], self.ballPossibleValuesList[2], self.ballPossibleValuesList[3], self.ballPossibleValuesList[4], self.ballPossibleValuesList[5])
        # Now the list is shuffled, we'll take the star values from these positions
        self.lotteryDrawStars = (self.starPossibleValuesList[1], self.starPossibleValuesList[2])

        # Sort ball and star values chosen in the draw for easier matching
        self.lotteryDrawBalls = sorted(self.lotteryDrawBalls)
        self.lotteryDrawStars = sorted(self.lotteryDrawStars)


    # Let's find out if our stars match the draw's stars
    def MatchedStars(self, lotteryDrawStars, wantedStars, matchStarCount):
        ballCount = 0
        for star in lotteryDrawStars:
            if star in wantedStars:
                ballCount += 1

            if ballCount == matchStarCount:
                return True
            else:
                return False


    # Let's find out if our balls match the draw's balls
    def MatchedBalls(self, lotteryDrawBalls, wantedBalls, matchBallCount):
        ballCount = 0
        for ball in lotteryDrawBalls:
            if ball in wantedBalls:
                ballCount += 1

        if ballCount == matchBallCount:
            return True
        else:
            return False



    # Calculate what we won in the current draw (of anything)
    def WhatDidWeWin(self):
        prizeValue = 0
        # prize money is average prize win, from page http://www.euro-millions.com/prizes.asp
        if (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 5) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 2)):
            prizeValue = 44992371
            self.win5s2 += 1
            threadLock.acquire(blocking=True, timeout=5)
            if threadLock.locked():
                print("Thread", self.threadId, "JACKPOT!!!")
                threadLock.release()

        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 5) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 1)):
            prizeValue = 305829
            self.win5s1 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 5) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 0)):
            prizeValue = 47882
            self.win5s0 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 4) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 2)):
            prizeValue = 3297
            self.win4s2 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 4) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 1)):
            prizeValue = 145.78
            self.win4s1 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 4) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 0)):
            prizeValue = 72.51
            self.win4s0 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 3) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 2)):
            prizeValue = 44.40
            self.win3s2 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 3) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 1)):
            prizeValue = 10.09
            self.win3s1 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 2) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 2)):
            prizeValue = 14.03
            self.win2s2 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 3) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 0)):
            prizeValue = 8.42
            self.win3s0 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 1) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 2)):
            prizeValue = 7.49
            self.win1s2 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 2) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 1)):
            prizeValue = 5.54
            self.win2s1 += 1
        elif (self.MatchedBalls(self.lotteryDrawBalls, self.wantedBalls, 2) and self.MatchedBalls(self.lotteryDrawStars, self.wantedStars, 0)):
            prizeValue = 2.79
            self.win2s0 += 1
        else:
            self.winFail += 1

        return prizeValue

    def saveResultsToMainThread(self):
        threadLock.acquire(blocking=True, timeout=50)
        if threadLock.locked():
            print("Thread", str(self.threadId),"saving results...")
            global all_lotteryCount
            global all_totalPrize
            global balls
            global stars
            global win5s2
            global win5s1
            global win5s0
            global win4s2
            global win4s1
            global win4s0
            global win3s2
            global win3s1
            global win3s0
            global win1s2
            global win2s1
            global win2s0
            global win2s2
            global winFail
            all_lotteryCount += self.lotteryCount
            all_totalPrize += self.totalPrize
            win5s2 += self.win5s2
            win5s1 += self.win5s1
            win5s0 += self.win5s0
            win4s2 += self.win4s2
            win4s1 += self.win4s1
            win4s0 += self.win4s0
            win3s2 += self.win3s2
            win3s1 += self.win3s1
            win3s1 += self.win3s1
            win1s2 += self.win1s2
            win2s1 += self.win2s1
            win2s0 += self.win2s0
            win2s2 += self.win2s2
            winFail += self.winFail
            threadLock.release()
        else:
            print("Could not lock the thread to save the results! :-(")

    def saveProgress(self):
        threadLock.acquire(blocking=True, timeout=5)
        if threadLock.locked():
            global threadData
            data = {"lotteriesPlayed": self.lotteryCount, "prizeHaul": round(self.totalPrize, 2), "spendingMoneyLeft": self.threadSpendingMoney}
            threadData[self.threadId] = data
            threadLock.release()

    # initialising function for the lotteryThread.
    # threadId is the thread number as assigned by the initialising for() loop in main()
    # threadSpendingMoney is the amount this thread can spend. When it runs out, the thread will end.
    # wantedBalls is the list of ball values that we want to play with
    # wantedStars in the list of wantedStars we want to play with
    def __init__(self, threadId, threadSpendingMoney, wantedBalls, wantedStars):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadSpendingMoney = threadSpendingMoney
        self.win5s2 = 0
        self.win5s1 = 0
        self.win5s0 = 0
        self.win4s2 = 0
        self.win4s1 = 0
        self.win4s0 = 0
        self.win3s2 = 0
        self.win3s1 = 0
        self.win2s2 = 0
        self.win3s0 = 0
        self.win1s2 = 0
        self.win2s1 = 0
        self.win2s0 = 0
        self.winFail = 0
        self.totalPrize = 0
        self.lotteryCount = 0
        self.wantedBalls = wantedBalls
        self.wantedStars = wantedStars

        self.ballPossibleValuesList = []
        self.starPossibleValuesList = []

        # These two loops create a list of num values from 1 to 50 (for balls) and 1 to 11 (for stars)
        # Later, for each draw these two lists will be shuffled, and the first 5 ball entries and first 2
        # star entries will be chosen in the lottery draw.
        for i in range(50):
            self.ballPossibleValuesList.append(i + 1)
        for i in range(11):
            self.starPossibleValuesList.append(i + 1)


    # Run this thread's lottery mechanics
    def run(self):
        self.totalPrize = 0
        self.lotteryCount = 0
        threadLock.acquire(blocking=True, timeout=5)
        if threadLock.locked():
            print("Playing in thread " + str(self.threadId))
            threadLock.release()

        while self.threadSpendingMoney > 0:
            self.threadSpendingMoney -= 2  # spend 2 units on your lottery ticket
            self.lotteryCount += 1  # add 1 to the count of lotteries played
            self.RunLotteryDraw()  # let's run those big money machines to choose this lottery draw's balls and stars
            self.totalPrize += self.WhatDidWeWin()  # Let's find out what we won, and add it to the prize haul

            if self.lotteryCount % 10000 == 0:
                self.saveProgress()

        # Finally we add our results to the global variables
        self.saveProgress()
        self.saveResultsToMainThread()
        print("Thread", str(self.threadId),"completed")


def spaceFormatData(data, maxLength):
    if isinstance(data, str):
        dataString = data
    else:
        dataString = str(data)
    outputString = ""
    diff = maxLength - len(dataString)
    for spaceCounter in range(0, diff):
        outputString += " "
    return outputString + dataString

# this function places vertical bars | into a data string to give it a table look.
# The column positions for the vars are in columnList e.g. [3, 7, 9]
def placeTableVerticalBars(dataString, columnList):
    outputString = ""
    for columnNumber in range(0, len(dataString)):
        if columnNumber in columnList:
            outputString += "|"
        else:
            outputString += dataString[columnNumber:columnNumber+1]
    return outputString


# Prints the results so far in a tabular format
def printDashboard():
    locale.setlocale( locale.LC_ALL, '' )
    verticalBarColumnList = [0, 8, 29, 44, 60]
    threadLock.acquire(blocking=True, timeout=5)
    if threadLock.locked():
        print(placeTableVerticalBars(" ----------------------------------------------------------- ", verticalBarColumnList))
        print(placeTableVerticalBars("  Thrd#    Lotteries played     Prize Haul       Money Left  ", verticalBarColumnList))
        print(placeTableVerticalBars(" ----------------------------------------------------------- ", verticalBarColumnList))
        for threadId in range (0, numberOfThreads):
            dataDict = threadData[threadId]
            dataString = spaceFormatData(str(threadId), 5)
            dataString += spaceFormatData(dataDict.get("lotteriesPlayed"), 21)
            dataString += spaceFormatData(locale.currency(dataDict.get("prizeHaul"), grouping=True), 16)
            dataString += spaceFormatData(locale.currency(dataDict.get("spendingMoneyLeft"), grouping=True), 17)
            dataString += "      "
            print(placeTableVerticalBars(dataString, verticalBarColumnList))

        print(placeTableVerticalBars(" ----------------------------------------------------------- ", verticalBarColumnList))
        print()
        threadLock.release()

def printResults():
    print("Completed!")
    print("Time taken:", endTime - startTime)
    print("Total lotteries played: " + '{:,}'.format(all_lotteryCount))
    print("Total money spent playing: {:,}".format(originalBank))
    print("Amount won: {:,}".format(round(all_totalPrize, 3)))
    print("Net won (minus if lost): {:,}".format(round(all_totalPrize - originalBank, 3)))
    print("Win counts (balls + stars matched):")
    print("5 + 2: " + str(win5s2))
    print("5 + 1: " + str(win5s1))
    print("5 + 0: " + str(win5s0))
    print("4 + 2: " + str(win4s2))
    print("4 + 1: " + str(win4s1))
    print("4 + 0: " + str(win4s0))
    print("3 + 2: " + str(win3s2))
    print("3 + 1: " + str(win3s1))
    print("2 + 2: " + str(win2s2))
    print("3 + 0: " + str(win3s0))
    print("1 + 2: " + str(win1s2))
    print("2 + 1: " + str(win2s1))
    print("2 + 0: " + str(win2s0))
    print("Lost!: " + str(winFail))


def createAndStartThreads():
    # Create the desired number of threads (simultaneous lottery draws)
    for threadId in range (0, numberOfThreads):
        threadSpendingMoney = int(totalBank / numberOfThreads)
        threadList.append(lotteryThread(threadId, threadSpendingMoney, wantedBalls, wantedStars))
        threadData.append({"lotteriesPlayed": 0, "prizeHaul": 0, "spendingMoneyLeft": 0})

    # Start the threads
    global startTime
    startTime = datetime.datetime.now()
    for threadId in range (0, numberOfThreads):
        threadList[threadId].start()


def main():
    print("EuroMillions Simulator v1.0 by Nick Lansley")
    print("Lottery ticket numbers are (set in script): balls: " + str(wantedBalls) + "  stars: " + str(wantedStars))

    global originalBank
    originalBank = totalBank

    # Get those big money machines spinning!
    createAndStartThreads()

    # Wait for the threads to complete
    allThreadsCompletedFlag = False
    while not allThreadsCompletedFlag:
        time.sleep(5)
        allThreadsCompletedFlag = True
        for threadId in range (0, numberOfThreads):
            if threadList[threadId].is_alive():
                allThreadsCompletedFlag = False

        if not allThreadsCompletedFlag:
            printDashboard()

    global endTime
    endTime = datetime.datetime.now()
    printDashboard()
    printResults()

if __name__ == '__main__':
    main()

