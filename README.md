# Netflix Movie Analysis

## Overview

This repository contains a Python script that analyzes Netflix movie data and visualizes the movie durations over the years. It also categorizes movies based on genres and presents a scatter plot showing the relationship between movie durations and their release years.

## Prerequisites

- Python 3.x
- pandas library
- matplotlib library

## Getting Started

1. Clone the repository to your local machine:
2. Make sure you have Python 3.x installed.
3. Install the required libraries using the following command:
   pip install pandas matplotlib


4. Download the "netflix_data.csv" file, which contains the Netflix movie data. Ensure that it is in the same directory as the Python script.

## Usage

1. Navigate to the project directory:
  cd netflix-movie-analysis

2. Run the Python script to perform the analysis:
   python netflix_analysis.py


The script will generate the following outputs:

- A line graph "Netflix Movie Durations 2011-2020" showing how movie durations have changed over the years.
- The first five rows of the "netflix_data.csv" file will be printed.
- A subset of the data containing only movies will be printed, along with specific columns.
- A list of short movies (duration < 60 minutes) will be printed.
- A scatter plot "Movie duration by year of release" categorizing movies by genre and representing the relationship between movie durations and release years.

## Data Source

The movie data used in this analysis is from the "netflix_data.csv" file. It contains information about various movies available on Netflix, including their titles, release years, genres, countries, and durations.

Please make sure to replace the "netflix_data.csv" file with your own dataset or provide a link to the actual data source if using this repository for your analysis.

## Results

- The line graph "Netflix Movie Durations 2011-2020" shows how movie durations have changed over the years.
- The scatter plot "Movie duration by year of release" categorizes movies by genre and represents the relationship between movie durations and release years.








