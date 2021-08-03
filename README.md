# plantpoetry

Poetry generated via machine learning from text scraped from a page of the Burpee seed catalog. 

Step 1: scrape text from here: https://www.burpee.com/flowers/full-sun-flowers/ via a python script.
Python script written following some of the tutorial here: https://www.edureka.co/blog/web-scraping-with-python/ 

Step 2: Feed the ML algorithm here (https://app.runwayml.com/workspaces/?modelId=PPLM ) with the scraped text, watch it go wild for a few iterations (using generated text as input for the next iteration). 

Step 3: Play with the text and break it up into something that looks like poetry. 
TODO: with a natural language processing librar, use the runwayml-generated text as input and use the library to break the text into poems. 
