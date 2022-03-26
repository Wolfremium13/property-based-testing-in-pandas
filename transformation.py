import pandas as pd


class Transformation:

    def sum_two_columns_and_generate_result(self, df: pd.DataFrame, first_column_name: str,
                                            second_column_name: str):
        df['result'] = df[first_column_name] + df[second_column_name]
        return df
