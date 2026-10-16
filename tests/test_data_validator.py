# tests/test_data_validator.py

import pytest

from src import validate_dataframe


def test_validate_dataframe_removes_invalid_ratings(sample_df):
    # TODO: Set the required and numeric column names.
    # TODO: Call validate_dataframe().
    # TODO: Assert that 98 rows remain and all five columns are preserved.
    required_columns = ['record_id','name','rating','category','status']
    numeric_column_names = ['rating']
    cleaned_df = validate_dataframe(sample_df,required_columns, numeric_column_names)
    assert len(cleaned_df) == 98
    assert len(cleaned_df.columns) == 5




def test_validate_dataframe_with_missing_column(sample_df):
    # TODO: Set required_columns to include a nonexistent column.
    # TODO: Use pytest.raises(ValueError) around validate_dataframe().
    
    required_columns = ['Nonexistent_column']

    with pytest.raises(ValueError):
        validate_dataframe(sample_df, required_columns,len(required_columns))
