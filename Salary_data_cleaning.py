#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 13:43:29 2026

@author: hanin
"""

import pandas as pd 

df = pd.read_csv('glassdoor_jobs.csv')

## Salary Parsing 

## Remove jobs with no salary information 
df = df[df['Salary Estimate'] != '-1']

## Salary Estimate Parsing

## Make a row for hourly rate 
df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

## Make a row for employer provided data 
df['Employer Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

## Separate Salary Info 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

## Remove K and $ sign from Salary info 
salary_wo_K_D = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

## Remove Per Hour and Employer Provided text from Salary Info 
salary_wo_hr_ep = salary_wo_K_D.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

## Separate minimum and maximum salary, add an average salary column
df['Minimum Salary'] = salary_wo_hr_ep.apply(lambda x: int(x.split('-')[0]))
df['Maximum Salary'] = salary_wo_hr_ep.apply(lambda x: int(x.split('-')[1]))
df['Average Salary'] = (df['Minimum Salary'] + df['Maximum Salary'])/2

## Company name text only 
df['Company'] = df.apply(lambda row: row['Company Name'] if row['Rating'] < 0 else row['Company Name'][:-3] , axis=1) 

## State of the job 
df['State'] = df['Location'].apply(lambda x: x.split(', ')[1])

##  How many jobs in each state 
df.State.value_counts()
               
## Age of company 
df.columns
df['Company Age'] = df['Founded'].apply(lambda x: 2026 - x if x > 0 else x)

## Is the job location at the same location as the headquarters 
df['Same_State'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

## Parse job description 
## Which relevant skills are outlined in job description 

## Python
df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.Python.value_counts()

## R Studio 
df['R Studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['R Studio'].value_counts()

## Spark 
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['Spark'].value_counts()

## AWS
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['AWS'].value_counts()

## Excel 
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['Excel'].value_counts()


## Remove the unnamed first column 
df.columns
df_new = df.drop(['Unnamed: 0'], axis = 1)

## Convert to new csv file 
df_new.to_csv('salary_data_cleaned.csv', index = False)
pd.read_csv('salary_data_cleaned.csv')
    


