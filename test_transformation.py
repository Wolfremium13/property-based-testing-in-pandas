import numpy as np
import pandas as pd
import pytest
from hypothesis import given, strategies as st, settings, Verbosity

from transformation import Transformation


def test_series_transformation_return_sum_of_columns():
    transformation = Transformation()
    val1 = 1.0
    val2 = 2.2
    df_given = pd.DataFrame(
        {
            'column_1': [val1],
            'column_2': [val2],
        }
    )
    expected_result = pd.Series([val1 + val2])

    df_calculated = transformation.sum_two_columns_and_generate_result(df_given, 'column_1', 'column_2')

    pd.testing.assert_series_equal(df_calculated.result, expected_result, check_names=False)


@pytest.mark.parametrize('val1, val2', [
    (0.1, 0.0),
    (1, -1),
    (0.000000001, 7.0),
    (np.nan, 0.0),
])
def test_pytest_transformation_return_sum_of_columns(val1: float, val2: float):
    transformation = Transformation()
    df_given = pd.DataFrame(
        {
            'column_1': [val1],
            'column_2': [val2],
        }
    )
    expected_result = pd.Series([val1 + val2])

    df_calculated = transformation.sum_two_columns_and_generate_result(df_given, 'column_1', 'column_2')

    pd.testing.assert_series_equal(df_calculated.result, expected_result, check_names=False)


@settings(verbosity=Verbosity.verbose)
@given(val1=st.floats(),
       val2=st.floats())
def test_hypothesis_transformation_return_sum_of_columns(val1: float, val2: float):
    transformation = Transformation()
    df_given = pd.DataFrame(
        {
            'column_1': [val1],
            'column_2': [val2],
        }
    )
    expected_result = pd.Series([val1 + val2])

    df_calculated = transformation.sum_two_columns_and_generate_result(df_given, 'column_1', 'column_2')

    pd.testing.assert_series_equal(df_calculated.result, expected_result, check_names=False)
