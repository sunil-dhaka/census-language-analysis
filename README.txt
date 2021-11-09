-----------------Q10 README.txt------------------


Plugins-
Software: python3 jupyter notebook (.sh files run python3 jupyter notebooks)

Environments: conda 4.10.3, python 3.8.5


Dependencies-
Python Libraries: pandas 1.1.3, numpy 1.19.2, scipy 1.5.2


Programs-

.sh files:

assign2.sh 
top level script that runs the entire assignment

How to use:
In order to run all programs sequentially, run the following command from the terminal-
bash assign1.sh 

One could use `time` command before bash execution to see how much time script takes to run.

Things to note:
It takes about 2 mins to run on my machine.
`scipy` have been used to compute p-values in Q2 and Q3.


How to run particular shell script:
--------------------------------------------------------------------------------------------
percent-india.sh
runs Q1_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q1_asgn2.ipynb

gender-india.sh
runs Q2_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q2_asgn2.ipynb

geography-india.sh
runs Q3_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q3_asgn2.ipynb

3-to-2-ratio.sh
runs Q4_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q4_asgn2.ipynb

2-to-1-ratio.sh
runs Q4_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q4_asgn2.ipynb

age-india.sh
runs Q5_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q5_asgn2.ipynb

literacy-india.sh
runs Q6_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q6_asgn2.ipynb

region-india.sh
runs Q7_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q7_asgn2.ipynb

age-gender.sh
runs Q8_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q8_asgn2.ipynb

literacy-gender.sh
runs Q9_asgn2.ipynb as
jupyter nbconvert --to notebook --execute Q9_asgn2.ipynb
------------------------------------------------------------------------------------------------

- NOTE: Every detail about the procedure to solve the question is given in markdowns and comments of notebooks. Also relevent obervation about outputs ate given in the last markdown section of each notebook file with appropriate data displyed above or below the obervations section, for better understanding and readibility. Even particular dataset files that are used to solve the question are mentioned in the markdowns. Please look there for minor details, here I am giving a summarised input/output for all notebooks.

Jupyter Notebook files points:

Q1_asgn2.ipynb
Input: datasets/C-17/{00-35}.xlsx, datasets/census.xlsx

Output: outputs/percent-india.csv

Q2_asgn2.ipynb
Input: datasets/C-18.xlsx, datasets/census.xlsx

Output: 
outputs/gender-india-a.csv
outputs/gender-india-b.csv
outputs/gender-india-c.csv

Q3_asgn2.ipynb
Input: datasets/C-18.xlsx, datasets/census.xlsx

Output: 
outputs/geography-india-a.csv
outputs/geography-india-b.csv
outputs/geography-india-c.csv

Q4_asgn2.ipynb -- uses scipy
Input: datasets/C-17/{00-35}.xlsx, datasets/census.xlsx

Output: 
outputs/3-to-2-ratio.csv
outputs/2-to-1-ratio.csv

Q5_asgn2.ipynb
Input: datasets/C-18.xlsx, datasets/C-13.xlsx

Output: outputs/age-india.csv

Q6_asgn2.ipynb
Input: datasets/C-19.xlsx, datasets/C-08.xlsx

Output: outputs/literacy-india.csv

Q7_asgn2.ipynb
Input: 
datasets/C-16.xlsx -- part-a
datasets/C-17/{00-35}.xlsx -- part-b

Output: 
outputs/region-india-a.csv
outputs/region-india-b.csv

Q8_asgn2.ipynb
Input: datasets/C-18.xlsx, datasets/C-13.xlsx

Output: 
outputs/age-gender-c.csv
outputs/age-gender-b.csv
outputs/age-gender-a.csv

Q9_asgn2.ipynb
Input: datasets/C-19.xlsx, datasets/C-08.xlsx

Output: 
outputs/literacy-gender-c.csv
outputs/literacy-gender-b.csv
outputs/literacy-gender-a.csv
