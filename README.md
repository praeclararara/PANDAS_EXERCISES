PANDAS EXERCISES 

# HELLO MONEY IN POLITICS
By election day, nearly $500 million dollars was spent by political campaigns that sought to influence voters to vote yes or no on those 17 propositions.
We know that because every dollar that is raised or spent by political campaigns in the state of California has to be disclosed. That’s thanks to the Political Reform Act of 1974, which was itself enacted by voters via a proposition.
Groups that support or oppose propositions, known as “committees,” must register with the secretary of state and file periodic reports. Those reports list the names, occupations and employers of donors, as well as how campaign funds are spent.
Those reports are stored in a public database maintained by the government. Almost every state has one like it.
In California, the database is called CAL-ACCESS, where you can download row data: https://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity
Unfortunately, the downloadable files are so jumbled, dirty and difficult that they are rarely used. In 2014, a team of journalists, academics and developers formed to solve the problem. They call themselves the California Civic Data Coalition: https://californiacivicdata.org/
An experimental early versions is used for this exercise (how to import that data into pandas and Jupyter notebook to start an analysis).

---source: https://www.firstpythonnotebook.org/money/index.html

# AIRBNB Venice
In this exercise I use an Airbnb listings dataset: http://insideairbnb.com/get-the-data.html
It will be interesting to answer some questions using the built-in functions in pandas. The goals in this case study will be to understand some of the differences between each type of listing in our data, defined by the room_type column. Specifically, we would like to know: What is the typical price for a listing? What is the difference in median price for different types of listings? How have these prices changed over time for each listing type? Finally, what is the distribution of typical listing prices?

---source: https://www.datacamp.com/community/tutorials/pandas

# TRAVEL_blog

Data sets for the TRAVEL_BLOG exercise: http://46.101.230.157/dilan/pandas_tutorial_read.csv AND http://46.101.230.157/dilan/pandas_tutorial_buy.csv
Selecting data
1) Print the whole dataframe
2) Print a sample of your dataframe
3) Select specific columns of your dataframe
4) Filter for specific values in your dataframe
5) Functions can be used after each other

TASKS:
TASK #1: What’s the most frequent source in the article_read dataframe?
TASK #2: For the users of country_2, what was the most frequent topic and source combination? Or in other words: which topic, from which source, brought the most views from country_2?
TASK #3: What’s the average (mean) revenue between 2018-01-01 and 2018-01-07 from the users in the article_read dataframe?
TASK #4: Print the top 3 countries by total revenue between 2018-01-01 and 2018-01-07

---source: https://data36.com/pandas-tutorial-1-basics-reading-data-files-dataframes-data-selection/ - author @tomimester


