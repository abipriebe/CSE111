# import altair as alt
# from vega_datasets import data

# source = data.cars()

# alt.Chart(source).mark_circle(size=60).encode(
#     x='Horsepower',
#     y='Miles_per_Gallon',
#     color='Origin',
#     tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
# ).interactive()


#Install the necessary libraries
import pandas as pd 
import altair as alt

# Load the data set 
students = pd.read_csv('/Users/abigailcluff/Documents/cse111/Week 11 and 12/StudentPerformance.csv')

chart = (alt.Chart(students)
    .mark_boxplot()
    .encode(x="gender", y="math_score"))

chart
# %%
