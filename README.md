# Disney Movie Financial Performance Analysis

## Project Overview
This project explores whether Disney movies that feature a signature song perform better financially at the box office compared to non-musical movies. The analysis uses historical Disney movie data to examine revenue trends and compare financial performance between musical and non-musical films.

## Research Question
Do Disney movies that feature a signature song perform better financially at the box office than non-musical movies?

## Datasets Used
The datasets used in this project are part of the **Disney Character Success** dataset collection.

Files used:
- `disney-characters.csv`
- `disney_movies_total_gross.csv`

Source:  
Kelly Garrett – Disney Character Success Dataset (data.world)

## Project Workflow
The analysis was conducted using the following steps:

1. **Data Import**
   - Loaded datasets using Python and pandas.

2. **Data Cleaning**
   - Removed newline characters from movie titles.
   - Converted revenue fields to numeric values.
   - Formatted release dates for analysis.

3. **Data Merging**
   - Merged character and financial datasets using the `movie_title` column.

4. **Feature Engineering**
   - Created a new boolean variable `is_musical` to classify movies based on whether a signature song exists.

5. **Exploratory Data Analysis**
   - Compared total revenue and inflation-adjusted revenue.
   - Generated visualizations to analyze revenue trends over time.

6. **Visualization**
   - Scatter plot to compare original and inflation-adjusted revenue.
     <img width="697" height="464" alt="revenue_scatter_plot" src="https://github.com/user-attachments/assets/0216849b-a0a2-4ebf-8547-8d543ec9c35a" />

   - Bar chart comparing average revenue between musical and non-musical movies.
     <img width="1776" height="1152" alt="Average Revenue of Musical vs Non-Musical Movies" src="https://github.com/user-attachments/assets/8994ba23-368a-4c2b-8e85-445ac1cd5fe2" />

   - Line chart showing revenue trends across years.
     <img width="774" height="460" alt="Average Inflation-Adjusted Revenue by Year for Musical and Non-Musical Disney Movies" src="https://github.com/user-attachments/assets/343f29e1-2528-47eb-8890-aea47b019cd4" />


## Key Findings
- Disney movies that feature signature songs generally show higher average box office revenue.
- Early Disney films show very high inflation-adjusted revenues because their original earnings are converted to today's dollar value.
- Revenue trends appear more stable in later years for both musical and non-musical films.

## Tools and Technologies
- Python
- Pandas
- Altair
- Data cleaning and preprocessing techniques

## Author
Seno Umoh  
Business Analyst | Data & Reporting | Power BI | Python
LinkedIn: www.linkedin.com/in/seno-umoh
