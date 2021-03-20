# jewlery-scraping

A simple web crawling project which crawls a Jewlery website named https://www.houseofindya.com/zyra/necklace-sets/cat which extract a set of necklaces.

## Steps to setup the project:

Clone the repository using the command

`git clone https://github.com/subhamyadav580/jewlery-scraping`

Get inside the project folder
`cd jewlery-scraping`

Activate the virtual environment

`soruce myvenv/bin/activate`

Install the dependenices

`pip install -r requirements.txt`

Now get into the main project folder

`cd scrapJewlery`

Start the crawler for crawling the website

`scrapy crawl necklace`

## for saving data into csv format

`scrapy crawl necklace -o items.csv`

## for saving data into .json format

`scrapy crawl necklace -o items.json`
