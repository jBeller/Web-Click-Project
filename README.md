# Bit Clicker
Repo for my class project for CINS 465. 
Bit clicker is a simple clicking game where users can create an account and compete with other users in a leaderboard. Users earn “bits” by clicking. They can then purchase an upgrade once they acquire enough “bits.” The goal is to try to stay at the top in the leaderboard. The website uses Django, Javascript, and Foundation 6.

## For the grader

There isn’t much to the game, but I am happy I got what I want in the backend working. Here’s what you can do for testing my website:

* Register an account to see the state of the game from a fresh user. When you go to the game page, the game will start off with 0 bits and only 1 bit per click (i.e. no upgrades).

* To see the state of the game from an existing user, log in with the sample credentials:

  User: User1
  
  Password: wordpass1 

* You can test the save feature on the game page by simply getting bits and upgrades and then clicking “Save.” This will save your data into the database, so when you refresh the page, your score and number of upgrades will not be lost. Your new score will also appear in the leaderboard the next time it updates, which is every 30 seconds. If you refresh without saving, the game will load what was previously saved. You can also try having the home page open on another window or tab to see the leaderboard there update after you save your score.

* User authentication is required in order to access the game. Try accessing the game without logging in by appending “/game” without quotes into the URL. This will redirect you to the login page.

* The register and login pages should not be accessible while the user is authenticated. While logged in, try accessing those pages by appending “/register” and “/login” into the URL respectively. You will be redirected to the home page.
