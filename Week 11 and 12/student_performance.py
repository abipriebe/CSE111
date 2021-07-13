#Install the necessary libraries
import pandas as pd 
import altair as alt

# Load the data set 
students = pd.read_csv('/Users/abigailcluff/Documents/cse111/Week 11 and 12/StudentPerformance.csv')

# Functions
def average_of_3scores(score1, score2, score3):
    return round((score1 + score2 + score3)/3)

def average_of_2scores(score1, score2):
    return round((score1 + score2)/2)

def create_boxplot(data, x_var, y_var):
    (alt.Chart(data)
    .mark_boxplot()
    .encode(x=x_var, y=y_var))

def create_scatterplot(data, x_var, y_var):
    (alt.Chart(data)
    .mark_circle(size=60)
    .encode(x=x_var, y=y_var))

def create_barplot(data, x_var, y_var):
    (alt.Chart(data)
    .mark_bar()
    .encode(x=x_var, y=y_var))

def filter_edu_level(target):
    students_target = students[students.parental_education == target]
    return students_target

def parentedu_testprep_proportion(data):
    num = data[data == "completed"].count()
    denom = data.count()
    return num / denom

# Main Function
def main():
    '''
    ### QUESTION 1:
    # Does gender play a role in student performance? Is it consistent across all subjects?
    '''
    # Create a new variable (average_score) that combines a student's math, reading, and writing scores into one 
    # that averages them together.  
    students["average_score"] = average_of_3scores(students.math_score, students.reading_score, students.writing_score)

    # Create a boxplot that shows the distribution of average_score grouped by gender
    boxplot1 = create_boxplot(students, "gender", "average_score")
    boxplot1

    # Create a boxplot that shows the distribution of math_score grouped by gender
    boxplot2 = create_boxplot(students, "gender", "math_score")
    boxplot2

    # Create a boxplot that shows the distribution of reading_score grouped by gender
    boxplot3 = create_boxplot(students, "gender", "reading_score")
    boxplot3

    # Create a boxplot that shows the distribution of writing_score grouped by gender
    boxplot4 = create_boxplot(students, "gender", "writing_score")
    boxplot4

    '''
    ### QUESTION 2:
    # Is there a significant relationship between a student's math and english scores?
    '''
    # Create a new variable (english_score) that combines a student's reading and writing scores into one 
    # that averages them together.
    students["english_score"] = average_of_2scores(students.reading_score, students.writing_score)

    scatterplot = create_scatterplot(students, "math_score", "english_score")
    scatterplot

    '''
    ### QUESTION 3:
    # Does a student's parent's education level have any effect on whether or not a student completed the test 
    # preparation course? Was there a difference in scores between the students who completed the course and 
    # the students who did?
    '''
    # What proportion of students with parents who have master's degrees completed the test prep course?
    students_master = filter_edu_level("master's degree")
    master_prop = parentedu_testprep_proportion(students_master["test_preparation_course"])
    print(master_prop)

    # What proportion of students with parents who have bachelor's degrees completed the test prep course?
    students_bach = filter_edu_level("bachelor's degree")
    bach_prop = parentedu_testprep_proportion(students_bach["test_preparation_course"])
    print(bach_prop)

    # What proportion of students with parents who have associate's degrees completed the test prep course?
    students_asso = filter_edu_level("associate's degree")
    asso_prop = parentedu_testprep_proportion(students_asso["test_preparation_course"])
    print(asso_prop)

    # What proportion of students with parents who have some college experience completed the test prep course?
    students_college = filter_edu_level("some college")
    college_prop = parentedu_testprep_proportion(students_college["test_preparation_course"])
    print(college_prop)

    # What proportion of students with parents who graduated high school completed the test prep course?
    students_hs = filter_edu_level("high school")
    hs_prop = parentedu_testprep_proportion(students_hs["test_preparation_course"])
    print(hs_prop)

    # What proportion of students with parents who have some high school experience completed the test prep course?
    students_high = filter_edu_level("some high school")
    high_prop = parentedu_testprep_proportion(students_high["test_preparation_course"])
    print(high_prop)

    q3_data = pd.DataFrame({
    'parental_edu_level': ['master', 'bach', 'asso', 'college', 'hs', 'high'],
    'test_prep_proportion': [master_prop, bach_prop, asso_prop, college_prop, hs_prop, high_prop]})

    # Create a bar plot showing the difference of average scores between those who took the prep course and those 
    # who did not, grouped by parental education level.
    barplot = create_barplot(q3_data, "parental_edu_level", "test_prep_proportion")
    barplot

if __name__ == "__main__":
    main()