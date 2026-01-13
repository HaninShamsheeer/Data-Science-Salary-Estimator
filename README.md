# Salary Estimator

A tool to observe and estimate salaries 

<img width="644" height="544" alt="Screenshot 2026-01-13 at 11 58 53 AM" src="https://github.com/user-attachments/assets/862e0423-369d-4c10-8d9d-085c09ca3dd6" />
<img width="924" height="451" alt="Screenshot 2026-01-13 at 11 58 40 AM" src="https://github.com/user-attachments/assets/4d9d7fe8-211e-4884-a394-79bc5ccc59a4" />
<img width="432" height="789" alt="Screenshot 2026-01-13 at 11 57 54 AM" src="https://github.com/user-attachments/assets/1c68b16a-9dee-476e-8288-2ae4e3499dd3" />


## Dataset 

The Data Scientist salary dataset was downloaded from (@PlayingNumbers) which orginally scraped 1000 data science job descriptions from Glassdoor using Python and Selenium. 

The dataset orginally consisted of columns such as Job Title, Salary Estimate, Job Description,	Rating,	Company Name,	Location,	Headquarters,	Size,	Founded, Type of ownership,	Industry, Sector, Revenue, Competitors

## Data Cleaning Process

* Jobs with no salary information was removed
* Two new columns that contained information on whether salary was in hourly rate or employee provided estimate were created
* The salary column was split in order to extract only the salary amount; then it was formatted by removing $ and K
* Hourly rate and employer provided estimate was removed from the orginial salary column
* Min, max and avg salary info columns were created
* Company name column was split in order to show only the company name
* State was separated from location
* Age of the company was calculated from year founded
* Checked descriptions for which technical skills: Python, R Studio, Spark, AWS, Excel were contained
* Unnamed first column was removed
* Job Categories were simplified into 7 main categories
* A seniority column that indicates level of seniority was created
* Description length column was created
* Competitor count was calculated
* Hourly wage was converted into yearly wage
* New line character in Company Name was fixed

Libraries: pandas 

## Data Exploration using Jupyter 

* Histograms were created for the ratings, age of the company, avg salary 
* Boxplots between company age and average salary, ratings was examined
* Correlations between some of the columns were examined
* Plots for categorical columns and other columns were also observed
* These pivot charts were also observed:
  * Average Salary by Job titles
  * Average Salary by Seniority and job titles
  * Average Salary by Location
  * and other combinations
* Pivot tables of average salary and other columns were observed
* A wordcloud heatmap of the description was created 
   

Libraries: pandas, matplotlib, seaborn

## Data modelling & Productionization 

In progress 
