# **REST-API-for-Data-Analysis-and-Visualization-with-Flask-and-Pandas**

Develop a REST API using Flask to upload and process CSV files. The API will allow users to upload data, perform data analysis (like summarizing statistics, filtering data, etc.), and then return the processed data in both JSON format and a visual format (graphical charts). The project will end with a simple, user-friendly web interface to visualize the data analysis results.

**Step-by-Step Breakdown:**

**1. Flask REST API Development**

**Endpoint 1**: Upload CSV data.
**Endpoint 2**: Perform basic data analysis using Pandas (e.g., summary statistics, column filtering).
**Endpoint 3**: Return the processed data as JSON or visualizations (plots).

**2. Data Analysis with Pandas**

**When a CSV file is uploaded through the API:**

**Step 1**: Load the data using Pandas.
**Step 2**: Perform analysis, like:
  1) Descriptive statistics (mean, median, etc.).
  2) Data filtering (e.g., by date range, specific conditions).
  3) Plot visualizations (histograms, bar charts, etc.).
  
**3. Web Interface for Data Visualization**

 **Create a simple web page where users can:**
 
   1) Upload their CSV file.
   2) View data statistics and visualizations (charts generated using Matplotlib or Plotly).
