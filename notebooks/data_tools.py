import pandas as pd

field_descriptions_fpath = "../data/raw/field_descriptions.txt"


def feature_name(field_df, col_num):
    field_name = FIELD_DATAFRAME.iloc[col_num][0].strip(":")
    return field_name.strip()


def parse_field_descriptions(fpath):
	df = pd.read_csv(fpath, delimiter="\t", header=None)
	df[0] = df[0].str.rstrip(":")
	df[0] = df[0].str.lower()
	return df