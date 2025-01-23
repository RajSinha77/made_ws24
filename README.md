## Project Work

<b>
Exploring the Correlation Between Unemployment and Crime Rates in MERCOSUR Countries Over Two Decades (2000-2020)<b> <br> 


https://github.com/RajSinha77/made-ws23/assets/33878640/895cb33c-1ad8-4f40-8038-93a5d51315ef

This project aims to investigate the relationship between unemployment rates and crime rates in a selection of global entities, focusing on the Unemployment is often linked to crime, as economic instability can drive individuals toward unlawful activities. This study examines the relationship between unemployment and crime rates in MERCOSUR countries (Argentina, Brazil, Paraguay, Uruguay, Colombia ,Guyana). By analyzing data on unemployment and crime, the research aims to uncover patterns and correlations, offering insights to help policymakers address unemployment-driven crime effectively. The diverse representation of economic structures, cultural contexts, and governance models in these entities offers a comprehensive understanding of the interplay between unemployment and crime.

The project employs statistical analysis to uncover patterns and trends, seeking correlations that can inform evidence-based policymaking. By examining data over several decades, the study provides a historical perspective on the evolving dynamics of unemployment and crime in the face of technological advancements and globalization. The ultimate goal is to contribute valuable insights for policymakers to formulate targeted interventions, social programs, and economic policies that address both unemployment and crime, promoting societal well-being.

Datasources : <br>
Unemployment Rates Dataset
<br>Data : https://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.ZS?downloadformat=csv
<br>Meta Data: https://databank.worldbank.org/reports.aspx?source=2&type=metadata&series=SL.UEM.TOTL.ZS
<br>Data Type: Zipped 
<br>CSVLicense: Creative Commons Attribution 4.0 International
<br>This dataset provides annual unemployment rates as a percentage of the total labor force, modeled by the International Labour Organization (ILO). It includes data for countries globally, allowing for cross-country comparisons.
<br><br>
Crime Rate Dataset
<br>Data URL: https://api.worldbank.org/v2/en/indicator/VC.IHR.PSRC.P5?downloadformat=csv
<br>Meta Data: https://databank.worldbank.org/reports.aspx?source=2&type=metadata&series=VC.IHR.PSRC.P5
<br>Data Type: Zipped
 <br>CSVLicense: Creative Commons Attribution 4.0 International
<br>This dataset records annual crime rates measured by the number of intentional homicides per 100,000 people. It serves as a key indicator for analyzing crime levels across different regions.
<br>

Further analysis is on report.ipynb or report.html (https://htmlpreview.github.io/?https://github.com/RajSinha77/made_ws24/blob/main/project/report.html))

Make sure to use setup Python v3.9.13 or above, use requirements.txt to install all dependencies alternatively you can also use pipenv to setup your Python enviournment.
```bash
project/
├── pipeline.py       -- performs ETL operations
├── pipeline.sh         -- makes a fetch data pipeline
├── project-plan.md		-- project plan readme file
├── report.ipynb        -- contains analysis
├── tests.sh	            -- implements tests.py
└── tests.py            -- implements unit tests for fetch_data pipeline 
```
Usage
To use this project, follow these steps:

 1. **Clone the Repository:**
   ```bash

git clone https://github.com/RajSinha77/made-ws23
cd made-ws23
```
2.**Run the Pipeline Script:**

- Execute the following command to run the pipeline script and download the datasets from World bank website.
```bash
bash pipeline.sh
The script will handle the download and extraction of datasets.
```

3. **Explore the Jupyter Notebooks:**
   - After downloading the datasets, explore the analysis by running the provided Jupyter Notebooks (report.ipynb)
   ```bash
   jupyter notebook
   ```



### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
