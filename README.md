# Student Feedback Analysis Project-Task -3

This project involves analyzing student feedback data collected from college events using both Python and Power BI to generate actionable insights.

---

## Project Overview

- **Data Source:** Student feedback CSV file with multiple columns related to course and teaching quality.
- **Python Part:**  
  - Cleans and prepares the feedback data.  
  - Combines multiple feedback columns into a single text column.  
  - Performs sentiment analysis using VADER (NLTK).  
  - Visualizes sentiment distribution with bar charts and generates a word cloud of common feedback terms.  
  - Saves the processed data with sentiment labels to a CSV file for further use.

- **Power BI Part:**  
  - Imports the processed CSV file.  
  - Creates interactive dashboards visualizing:  
    - Average ratings by course and question.  
    - Sentiment distribution.  
    - Top rated questions and courses.  
  - Uses slicers and filters for dynamic exploration of feedback data.
-Key Deliverables
Cleaned Student Feedback Data (CSV format)
Interactive College Event Feedback Dashboard (Power BI .pbix file)
Summary of Key Insights and Recommendations based on rating analysis.
Data Source
The analysis was performed on the Student_Satisfaction_Survey.csv dataset, which contains structured feedback on various college events and courses. This dataset includes numerical ratings (from 1 to 5) and associated metadata for different questions and courses.

-Understanding Key Metrics & Data Structure
The dataset includes the following key columns relevant to the analysis:

Question_Text: The specific survey question asked.
Rating_Count_1 to Rating_Count_5: Counts of how many times each rating (1 to 5) was selected for a given question and course.
Total_Feedback_Given: The total number of responses received for a particular question-course combination.
Average_Rating: The calculated average rating for each question-course combination (derived from the original dataset).
Course_Name: The specific course or event name.
Basic_Course_Category: A broader category for the course/event.
Data Cleaning and Preparation (Using Power BI's Power Query)
The raw Student_Satisfaction_Survey.csv dataset was prepared for analysis directly within Power BI Desktop using its Power Query Editor. The key steps performed include:

Data Type Assignment: Ensured all numerical columns (Total_Feedback_Given, Rating_Count_1 to Rating_Count_5, Average_Rating) were correctly set as numeric data types (Whole Number or Decimal Number). Text columns were set as Text.
Column Renaming: Renamed columns for clarity and consistency (e.g., Total Feedback Given to Total_Feedback_Given, Questions to Question_Text, etc.).
Average Rating Parsing: While the Python script already created Average_Rating, if starting directly in Power BI, this would involve parsing the original Average/ Percentage column to extract the numerical average.
Data Validation: Verified consistency between Total_Feedback_Given and the sum of Rating_Count_1 to Rating_Count_5.
Analysis Performed & Key Insights
The interactive Power BI dashboard provides a clear overview of student satisfaction:


-
## How to Run Python Code

### Requirements

Install the required Python packages:

```bash
pip install pandas matplotlib seaborn nltk wordcloud

Run the script
Place your feedback CSV file in the project folder.

Update the list of feedback columns in the script to match your dataset.

Run the Python script:
 python sentiment_analysis.py



Contact:
Feel free to reach out if you have any questions or feedback!

Name:Pasupuleti Teja Prasad
Email:pasupuletitejaprasad@gmail.com
Linkedin:https://www.linkedin.com/in/teja-prasad-pasupuleti-100536275
