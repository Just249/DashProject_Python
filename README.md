herokuapp link: https://data551-dashproject-python.herokuapp.com/

Note: For some reason I have to pay inorder to get it running, will showcase to TA/Teacher that it is working.

Here is a screenshot of it:
![image](https://user-images.githubusercontent.com/61757423/222994209-ba896e75-e038-413a-a6e4-0013946778cf.png)


# Milestone 1 - Dashboard proposal
### Section 1: Motivation and Purpose of the dashboard

> Our role: Data science consultancy firm
>
> Target audience: Health care researchers and Doctors
>
> Sleep has a very important role to play in everyone's life. The quality, length, schedule, intake of caffeine and intake of drugs among other things affect the way one will feel after waking up the next morning. Hence, it is important to study how sleep is affected when the external factors surrounding sleep change. Does it vary between genders? What external factors affect it? Does longer duration in REM sleep mean better sleep quality? Does caffeine affect sleep? Does smoking affect sleeping patterns, sleeping duration and awakenings? To help the researchers in answering these questions better, we propose building a dashboard that allows stakespersons to visually explore different aspects of the sleep dataset that is taken from Kaggle which contains information about a group of test subjects and their sleep patterns. Our dashboard will show how different factors contribute to the type of sleep we get and allow users to explore different aspects of sleep data by filtering on different variables in order to compare factors that contribute to the type of sleep one gets.

### Section 2: Description of the data

- We will be visualizing a dataset of approximately `450` subjects and their sleeping patterns.
- Each subject has `15` variables associated with them pertaining to their sleeping paterns and process, and conditions 24 hours before their sleep. 
- Some of the important variables include: `Age`, `Gender`, `Sleep Duration`, `Sleep Efficiency`, `REM sleep percentage`, `Deep sleep percentage`, `Light sleep percentage`, `Awakenings`.
- We will visualize REM sleep percentage, Deep Sleep percentage Slow sleep percentage in one tab which will have the option of filtering using factors like: `Smoke Status`, `Alcohol Consumption`, `Caffeine Consumption`, `Exercise Frequency` 
- In another tab we try to give the overview of the data by showing sleep efficiency percentage and sleep duration percentage and count of awakenings by age group and gender respectively wherever each one is applicable.
- We create new columns as required to assist in our visualizations. For example, we bin the `Age` column to boslter our visualizations.
- Some initial wrangling showed that the columns: `Awakenings`, `Caffeine consumption`, `Alcohol consumption`, `Exercise frequency` had some NA values which were dealt with by replacing mean values with mean values.

### Section 3: Research questions and usage scenarios

> Dean Winchester is a sleep researcher with the Canadian Ministry of Health and he wants to understand what factors lead to better sleep in order to educate doctors further on how to improve the sleep quality and duration of their patients. He wants to be able to explore the sleep data collected on subjects by measuring various different factors and conditions to identify variables that most affect sleep, especially how different genders measure on different kinds of sleeps and what affects it. When Dean comes to this dashboard, he will be able to see how the sleep duration, sleep efficiency and awakenings are spread among males and females. Furthermore, he will be able to see how many people in each gender are able to get REM, Deep or Light sleep by varying factor inputs mentioned in Section 2. This dashboard will be a very handy tool in bolstering the knowledge that researchers and doctors have regarding the science of sleep. Dean may find that consuming alcohol helps in getting a better quality sleep but only to a certain level. Or, he may find that caffeine consumption before sleep reduces the sleep duration and efficiency. By varying these factors for various subjects, Dean will be able to study, observe and notice variables that affect sleep the most and this will provide him further guidance on what kind of sleep related factors he should be looking into to go deeper into this research.


# Dash Sketch:


![image](https://user-images.githubusercontent.com/61757423/220833021-9431a3d6-04e8-469a-b4c1-dfeeef92fd37.png)

![image](https://user-images.githubusercontent.com/61757423/220833031-102f7831-b810-41fb-81f4-7e775c6eca5a.png)

# For users of the dashboard

Sleep plays a vital role in everyone's life, and its quality, duration, and schedule are influenced by various external factors. Understanding how sleep is affected by external factors such as caffeine, drugs, and smoking is crucial. To facilitate this understanding, the proposal is to develop a dashboard that visually explores the sleep dataset from Kaggle. The dashboard will enable users to analyze the effects of different variables on sleep and compare the impact of these variables. The aim of this analysis is to answer questions regarding the impact of external factors on sleep patterns, including differences between genders, the effect of caffeine and smoking, and the relationship between REM sleep and sleep quality.

# Things that can be improved among other things

- From the pictures attached above of tab 1 and tab 2, we can see that the genders are put into groups using different colours. There is scope for future improvement to show the data by other categorical data like 'Smoke Status'
- To see more statistics of the data like range, standard deviation, standard errors and confidence intervals, a new widget can be incorporated on the dash on which the user can see all the above mentioned values according to variables that he chooses using a dropdown or radio buttons, etc.
- Any other sensible addition which helps improve the story telling part of the dataset is welcome.

# How to get involved

If you think you can help in any of the areas listed above (and we bet you can) or in any of the many areas that we haven't yet thought of (and here we're sure you can) then please check out our contributors' guidelines and join the madness.

Please note that it's very important to us that we maintain a positive and supportive environment for everyone who wants to participate. When you join us we ask that you follow our code of conduct in all interactions both on and offline.




