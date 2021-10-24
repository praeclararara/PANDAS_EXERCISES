#!/usr/bin/env python
# coding: utf-8

# In[173]:


import numpy as np
import pandas as pd


# In[174]:


committee_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/committees.csv")


# In[175]:


committee_list


# In[176]:


contrib_list = pd.read_csv("https://raw.githubusercontent.com/california-civic-data-coalition/first-python-notebook/master/docs/_static/contributions.csv")


# In[177]:


contrib_list


# In[178]:


committee_list.info()


# In[179]:


committee_list.head()


# In[180]:


contrib_list.head()


# In[181]:


committee_list.prop_name


# In[182]:


committee_list.prop_name.value_counts()


# In[183]:


committee_list.prop_name.value_counts().reset_index()


# In[184]:


#we want to filter against is prop_name. We only want to keep those records
#where the value there matches the full name of Proposition 64.


# In[185]:


my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'


# In[186]:


#we will ask pandas to narrow down our list of COMMITTEES to just those that match
#the proposition we’re interested in. We will create a filter expression that looks like this:
#committee_list.prop_name == my_prop


# In[187]:


committee_list[committee_list.prop_name == my_prop]


# In[188]:


my_committees = committee_list[committee_list.prop_name == my_prop]
my_committees.head()
my_committees.info()


# In[189]:


#now we want to filter down the CONTRIBUTION list, which includes all disclosed contributions 
#to all proposition campaigns, to just those linked to Proposition 64


# In[190]:


contrib_list.info()


# In[191]:


committee_list.info()


# In[192]:


merged = pd.merge(my_committees, contrib_list, on="calaccess_committee_id")
merged.head()


# In[193]:


merged.amount


# In[194]:


merged.amount.sum() #total amount spent on this proposition.


# In[195]:


#We want to separate the money spent supporting the proposition from the money opposing it.
#Then we want to find out who raised more so we’re going to filter by, committee_position


# In[196]:


merged.committee_position.value_counts()


# In[197]:


support = merged[merged.committee_position == 'SUPPORT']
support.head()


# In[198]:


oppose = merged[merged.committee_position == 'OPPOSE']
oppose.head()


# In[199]:


oppose.amount.sum()


# In[200]:


support.amount.sum()


# In[201]:


#what percent is it of the overall disclosed total? We can find out by
#combining two sum calculations using the division operator


# In[202]:


support.amount.sum() / merged.amount.sum()


# In[203]:


merged.sort_values("amount", ascending=False).head()


# In[204]:


support.sort_values('amount', ascending=False).head()


# In[205]:


oppose.sort_values('amount', ascending=False).head()


# In[206]:


#How much of the money came from outside of California?


# In[207]:


merged.groupby("contributor_state").head()


# In[208]:


#totals by state
merged.groupby("contributor_state").amount.sum()


# In[209]:


merged.groupby("contributor_state").amount.sum().reset_index().sort_values("amount", ascending=False).head()


# In[210]:


#grouping by top contributors where first name and last name are in 2 different columns - list


# In[211]:


merged.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False).head()


# In[212]:


#find out if each contributor supported or opposed the measure


# In[213]:


merged.groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False)


# In[214]:


#top supporters or opponents alone


# In[215]:


support.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)


# In[216]:


oppose.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False).head()


# In[217]:


#Since Pandas drops any rows with null values in groupby func.,
#we need to replace those NaN first names with empty strings to get the right data


# In[218]:


merged.fillna("").groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False).head()


# In[219]:


#What are the top employers of donors for and against the measure?


# In[220]:


#top employers
merged.fillna("").groupby(["contributor_employer"]).head()
merged.fillna("").groupby(["contributor_employer"]).amount.sum().reset_index().sort_values("amount", ascending=False).head()


# In[221]:


#top employers for the measure


# In[222]:


support.fillna("").groupby(["contributor_employer"]).amount.sum().reset_index().sort_values("amount", ascending=False).head()


# In[223]:


#top employers against the measure


# In[224]:


oppose.fillna("").groupby(["contributor_employer"]).amount.sum().reset_index().sort_values("amount", ascending=False).head()


# In[225]:


#Which committees had the fewest donors?


# In[226]:


#getting the fewest donors by counting how many donations/amount have been done
merged.groupby(["committee_name_x"]).amount.count().reset_index().sort_values("amount", ascending=True).head()


# In[227]:


#What was the average size of donations both for and against?


# In[228]:


support.amount.mean()


# In[229]:


oppose.amount.mean()


# In[230]:


#REMIXING the analysis by a different proposition


# In[231]:


my_prop = 'PROPOSITION 062- DEATH PENALTY. INITIATIVE STATUTE.'


# In[232]:


committee_list[committee_list.prop_name == my_prop]


# In[233]:


#creating bar charts with ALTAIR_to istall alt the first time from Jupyter: !pip install altair


# In[234]:


import altair as alt


# In[235]:


top_supporters = support.fillna("").groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False).head(10)
top_supporters


# In[236]:


alt.Chart(top_supporters).mark_bar().encode(x="contributor_lastname", y="amount")


# In[237]:


#transposing the bars
alt.Chart(top_supporters).mark_bar().encode(
    x="amount",
    y="contributor_lastname")


# In[238]:


#top 5 records
alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y="contributor_lastname")


# In[239]:


#combine 2 columns (the first and last name) putting them together in a new field on the df and, just like a variable, setting it equal to a combination of the other fields.


# In[240]:


top_supporters["contributor_fullname"] = top_supporters["contributor_firstname"] + top_supporters["contributor_lastname"]
top_supporters.head()


# In[241]:


alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y="contributor_fullname")


# In[242]:


#This chart is sorted alphabetically by y-axis value but we want to
#sort the y-axis values by their corresponding x values


# In[243]:


alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_fullname", sort="-x"))


# In[244]:


#adding a title to the chart
alt.Chart(top_supporters.head(5)).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_fullname", sort="-x")).properties(title="Top Spenders in Support of Proposition 64")


# In[245]:


#checking who spent money on both sides (supporting AND opposing) by creating new dataframe, top_contributors,
#summing up the top contributors in our whole merged dataframe


# In[246]:


top_contributors = merged.fillna("").groupby(
    ["contributor_firstname", "contributor_lastname","committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False)
top_contributors.head(10)


# In[247]:


#adding top_contributor_fullname column
top_contributors["contributor_fullname"] = top_contributors["contributor_firstname"] + top_contributors["contributor_lastname"]
top_contributors.head(10)


# In[253]:


alt.Chart(top_contributors.head(10)).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_fullname", sort="-x")).properties(title="Top Contributors of Proposition 64")


# In[249]:


#adding color to show committee position (support or oppose)


# In[252]:


alt.Chart(top_contributors.head(10)).mark_bar().encode(
    x="amount",
    y=alt.Y("contributor_fullname",sort="-x"),
    color="committee_position")


# In[ ]:


#to export this data into a spreadsheet:
#top_supporters.head(10).to_csv("top_supporters.csv")


# In[ ]:




