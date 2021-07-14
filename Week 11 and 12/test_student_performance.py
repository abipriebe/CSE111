# Import libraries and functions
import pytest
import pandas as pd
from student_performance import filter_edu_level
from student_performance import average_of_3scores
from student_performance import average_of_2scores
from student_performance import parentedu_testprep_proportion

# Load the data set 
students = pd.read_csv('/Users/abigailcluff/Documents/cse111/Week 11 and 12/StudentPerformance.csv')

# Test the functions
def test_average_of_3scores():
    score1 = students.math_score
    score2 = students.reading_score
    score3 = students.writing_score

    average_score = average_of_3scores(score1, score2, score3)
    for student in students:
        assert average_score == round((score1 + score2 + score3)/3)

def test_average_of_2scores():
    score1 = 1
    score2 = 2

    average_score = average_of_2scores(score1, score2)
    assert average_score == round((score1 + score2)/2)

def test_parentedu_testprep_proportion():
    series = students.parental_education
    target = "completed"
    proportion = parentedu_testprep_proportion(series, target)

    assert proportion == ((series[series == target].count())/series.count())
'''
def parentedu_testprep_proportion(data, series, target):
    num = data[series == target].count()
    denom = series.count()
    return num / denom
'''

def test_filter_edu_level():
    """Verify that the filter_for_meter function works correctly."""

    # Call the filter_edu_level function.
    data = students
    series = students.parental_education
    target = "master's degree"
    filtered_df = filter_edu_level(data, series, target)

    # Verify that the filtered data frame contains at least one row.
    assert len(filtered_df.index) > 0

    # Verify that all the meter numbers in the
    # filtered data frame are the correct number.
    for value in filtered_df["parental_education"]:
        assert value == target

pytest.main(["-v", "--tb=line", "-rN", "/Users/abigailcluff/Documents/cse111/Week 11 and 12/test_student_performance.py"])