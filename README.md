# Let's learn Scrapping

This repository will explaing how to use scrapping technique to extract data from a web page.

## Language used
Python <code><img height="20" alt="Python" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>: This will be the main language. We'll use the selenium module to open a chrome-controller instance.</br>
HTML <code><img height="20" alt="Python" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code>: Basic knowledge to scrapping throught the page.</br>
CSS <code><img height="20" alt="Python" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code>: Basic knowledge to identify classes

## Setup pre requirements
<p>For this exercise we will need to download the chromedriver of the related version of our Chrome explorer.</p>
<p>So, let's do this!</p>

### Checking our Chrome version
1. Open Chrome then click the 3dot menu to go to the *Help* option and click on *About Google Chrome*</br>
<img height="300" alt="Chrome screenshot showing the 3-dot menu" src="./images/settings.png">

2. Then check the installed version of Chrome, please pay attention to the first three digits, you'll need them. *In the example is showing the version number 109.*</br>
<img height="300" alt="Chrome screenshot showing the version number" src="./images/version.png">

### Downloading Chrome driver
Selenium uses a driver to navigate though the web page, so we'll need to download the driver related to the version of Chrome we've installed.

1. Let´s google *chromedriver* to go to the <a href="https://chromedriver.chromium.org/">**Chromium.org**</a> page.</br>
<img height="300" alt="Chromedriver main page at Chromium dot org" src="./images/chromedriver.png">

2. Click at the version to download. In some cases you'll need to click on *Download* to find older versions.</br>
<img height="300" alt="Chromedriver version to download" src="./images/chromedriver_version.png">

3. Once the chromedriver is downloaded, unzip it and place it into a folder on the project. This way we can use the driver by using the path: `./chromedriver/chromedriver.exe`</br>
<img height="300" alt="Chromedriver placed into a project folder" src="./images/unziped.png">

We're ready to go!

## Explore the page
In this example we'll extract all the results of a lotto, so first we'll need to understand how the lotto page is working to navigate it thought the results.

We'll dive into the <a href="https://www.baloto.com/"> **Baloto** </a> page, a colombian lotery, you can access it by clicking <a href="https://www.baloto.com/">here</a>

The page is in spanish so I'll refer to the word in spanish by using *Italic* and the english word by using **bold**.

First, we can notice that the page has a *Results* page (**Resultados**), so let's click on it.

<img height="300" alt="Baloto's main page" src="./images/blt_main.png">

### Looking for a pattern to navigate the results
Now, we can see at first sight the results of the last game. But we want them all.

When we scroll down we can see there's a table summarizing the lotto game status for each instance, but no results. 

We can see that there's a *game number* at the column **N° de sorteo** and for each game number there are two types of *games* at the column **sorteo**: Baloto and Revancha

So, let's check the game number 2261 by clicking *view detail* (**ver detalle**) and see if we can find any pattern to get through all the results.

Here we have the result numbers and taking a look to the URL it seems like a pattern.

<img height="300" alt="Baloto's 2261 game results" src="./images/baloto_pattern.png">

Let's check same game nunmber but different type going backwards and clicking the next row on the table.

<img height="300" alt="Baloto_revancha's 2261 game results" src="./images/revancha_pattern.png">

Seems like a pattern, lets try changing the game number to 2259 in the URL.

<img height="300" alt="Chromedriver main page at Chromium dot org" src="./images/revancha_pattern_2.png">

It's a pattern!

Now check yourself the lowest number game to use it to navigate through all the games from it to 2261

### Check the numbers CSS

To get the result numbers we'll need to know where are they placed on the page, we'll use one of the developer's tool called the 'inspector'.

We'll inspect the ball to get its class. So first, right-click the ball to open the context menu, then click *Inspect*.

<img height="300" alt="Chromedriver main page at Chromium dot org" src="./images/context_menu.png">

Well done! Now we know the yellow ball belongs to the class `"yellow-ball"` but, will it work with the red ball? Let's check

We'll use the element selector tool to select the red ball with the developer tool already opened.

<img height="300" alt="Chromedriver main page at Chromium dot org" src="./images/element_selector.png">

Once we click on the red ball we noticed that the red ball belongs to the class `"red-ball"`

### Sumary

Now we know that the URL has a pattern with two dependencies:

- Game type (baloto|revancha)
- Game number (2261|2259 examples)

Adn that the result balls belong to two classes:

- `yellow-ball`
- `red-ball`

Time to code!

## The code

