# PANDAS PROJECTS - DA 

## HELLO MONEY IN POLITICS
By election day, nearly $500 million dollars was spent by political campaigns that sought to influence voters to vote yes or no on those 17 propositions.
We know that because every dollar that is raised or spent by political campaigns in the state of California has to be disclosed. That’s thanks to the Political Reform Act of 1974, which was itself enacted by voters via a proposition.
Groups that support or oppose propositions, known as “committees,” must register with the secretary of state and file periodic reports. Those reports list the names, occupations and employers of donors, as well as how campaign funds are spent.
Those reports are stored in a public database maintained by the government. Almost every state has one like it.
In California, the database is called CAL-ACCESS, where you can download row data: https://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity
Unfortunately, the downloadable files are so jumbled, dirty and difficult that they are rarely used. In 2014, a team of journalists, academics and developers formed to solve the problem. They call themselves the California Civic Data Coalition: https://californiacivicdata.org/
An experimental early versions is used for this exercise (how to import that data into pandas and Jupyter notebook to start an analysis).

---source: https://www.firstpythonnotebook.org/money/index.html

## Healthcare-Analysis
A nationwide survey of hospital costs conducted by the US Agency for Healthcare consists of hospital records of inpatient samples. The given data is restricted to the city of Wisconsin and relates to patients in the age group 0-17 years. The agency wants to analyze the data to research on the healthcare costs and their utilization. Here is a detailed description of the given dataset: AGE : Age of the patient discharged FEMALE : Binary variable that indicates if the patient is female LOS : Length of stay, in days RACE : Race of the patient (specified numerically) TOTCHG : Hospital discharge costs APRDRG : All Patient Refined Diagnosis Related Groups. The data was provided by through the link (under the name HospitalCosts): http://instruction.bus.wisc.edu/jfrees/jfreesbooks/Regression%20Modeling/BookWebDec2010/data.html
The goals of this project are:
-To record the patient statistics, the agency wants to find the age category of people who frequent the hospital and has the maximum expenditure.
-In order of severity of the diagnosis and treatments and to find out the expensive treatments, the agency wants to find the diagnosis related group that   has maximum hospitalization and expenditure.
-To make sure that there is no malpractice, the agency needs to analyze if the race of the patient is related to the hospitalization costs.
-To properly utilize the costs, the agency has to analyze the severity of the hospital costs by age and gender for proper allocation of resources.
-Since the length of stay is the crucial factor for inpatients, the agency wants to find if the length of stay can be predicted from age, gender, and       race.
-To perform a complete analysis, the agency wants to find the variable that mainly affects the hospital costs.
In this case study, I have performed the Descriptive Analysis, Exploratory Data Analysis and Predictive Analysis.
###Classification:
APR-DRGs
Early patient classification systems, such as the Medicare DRGs and All Patient (AP) DRGs were developed to provide patient classification systems that relate the types of patients treated to the resources they consume. \ Thus, these systems focus exclusively on resource intensity. \ Some drawbacks of these systems:
– Medicare DRGs were designed for the Medicare population only.\ – Neither system is severity adjusted and therefore does not\ provide an incentive to care for higher need patients.\ – Higher complexity DRGs (with CC) are formed based on resource\ intensity and do not address severity of illness nor risk of mortality.\ – Medicare addressed these needs by developing MS-DRGs.\
APR-DRG address these deficiencies\ • All APR DRGs have 4 severity levels\ • Patient age is used in severity leveling\ • Significant pediatric and adult problems have a separate APR-DRG\
What makes APR-DRG’s Relevant?\ • APR-DRGs make clinical sense. The clinical logic of APR-DRGs has undergone the most intensive scrutiny of any severity system on the market.\ • The logic is open and available. APR-DRGs are not a “black box”.\ • The system was designed to be fully comprehensive and account for all payers, patients, and ages (including pediatrics).\

## AIRBNB Venice
In this exercise I use an Airbnb listings dataset: http://insideairbnb.com/get-the-data.html
It will be interesting to answer some questions using the built-in functions in pandas. The goals in this case study will be to understand some of the differences between each type of listing in our data, defined by the room_type column. Specifically, we would like to know: What is the typical price for a listing? What is the difference in median price for different types of listings? How have these prices changed over time for each listing type? Finally, what is the distribution of typical listing prices?

---source: https://www.datacamp.com/community/tutorials/pandas

## RATING MOVIES - MovieLens dataset
Find out what are the most rated movies, which movies are most controversial amongst different ages, Which movies do men and women most disagree on.
Based on "Intro to pandas data structures": http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

## CHICAGO_EMPLOYEES-SALARIES
This exercise is good for learning Cleaning Up Currency Data in Pandas.
This is a useful article that explains the procedure: https://pbpython.com/currency-cleanup.html
SOLUTION #1 with CUSTOM FUNCTION
def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)
This function will check if the supplied value is a string and if it is, will remove all the characters we don’t need. If it is not a string, then it will return the original value.

Here is how we call it and convert the results to a float. I also show the column with the types:

df['Sales'] = df['Sales'].apply(clean_currency).astype('float')
df['Sales_Type'] = df['Sales'].apply(lambda x: type(x).__name__)

SOLUTION #2 WITH LAMBDA FUNCTION
df['Sales'] = df['Sales'].apply(lambda x: x.replace('$', '').replace(',', '')
                                if isinstance(x, str) else x).astype(float)

## Analysing multiple records of sales
In this project I use Python Pandas, Seaborn & Python Matplotlib to analyze and answer business questions about 12 months worth of sales data. The data contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc.
The objective is to stack all the original tables and finding:
-the city that made the most purchases
-the most profitable time of the sale
-the most profitable item
-the most profitable items sold together
DATA SOURCE: https://github.com/KeithGalli/Pandas-Data-Science-Tasks/tree/master/SalesAnalysis/Sales_Data

## TRAVEL_blog

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


