# Student Performance Dashboard

A basic interactive student performance dashboard built using **Python, Pandas, and Streamlit**.

The dashboard loads student data from a CSV file and provides an easy way to explore student performance based on branch and city.

## Features

* View total number of students
* Calculate average marks
* Find the highest marks
* Count BCA students
* Filter students by branch
* Filter students by city
* View complete student data
* Display student-wise marks using a bar chart
* Display number of students in each branch
* Analyze average marks by branch
* Analyze average marks by city

## Technologies Used

* Python
* Pandas
* Streamlit

## Project Structure

```text
student-performance-dashboard/
│
├── app.py
├── students.csv
└── README.md
```

## Dataset

The project uses a CSV file named `students.csv`.

The dataset contains the following columns:

| Column | Description               |
| ------ | ------------------------- |
| name   | Name of the student       |
| age    | Age of the student        |
| city   | Student's city            |
| branch | Student's academic branch |
| marks  | Student's marks           |

## How the Dashboard Works

The application first loads the CSV file using Pandas:

```python
df = pd.read_csv("students.csv")
```

Users can then filter the data using the sidebar by selecting a branch and/or city.

The filtered data is stored in:

```python
filtered_df
```

The dashboard then uses this filtered data to calculate metrics and generate charts.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Go to the project folder:

```bash
cd student-performance-dashboard
```

Install the required libraries:

```bash
pip install pandas streamlit
```

## Run the Project

Run the following command:

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

## Dashboard

The dashboard provides:

* Student performance table
* Total student count
* Average marks
* Highest marks
* BCA student count
* Student marks chart
* Students by branch chart
* Average marks by branch
* Average marks by city

## Learning Outcomes

Through this project, I practiced:

* Reading CSV files using Pandas
* Working with Pandas DataFrames
* Filtering DataFrames
* Using `unique()`
* Using `isin()`
* Using `value_counts()`
* Using `groupby()`
* Calculating mean and maximum values
* Creating interactive dashboards with Streamlit
* Creating charts using Streamlit
* Building a simple data analysis project

## Future Improvements

Some possible improvements for this dashboard are:

* Add student search functionality
* Add age-based analysis
* Add more interactive charts
* Add student profile selection
* Add downloadable filtered data
* Improve the dashboard UI
* Deploy the dashboard online

## Author

**Mankarandeep Singh**

This project was created as part of my learning journey in **Python, Pandas, and Data Science**.
