import pandas as pd
import functools

LOCAL = True
data_fpath = '../data/raw/' if LOCAL else '/kaggle/input/protein-localization/'
field_descriptions_fpath = f"{data_fpath}field_descriptions.txt"


def feature_name(field_df, col_num):
    field_name = field_df.iloc[col_num][0].strip(":")
    return field_name.strip()


def parse_field_descriptions(fpath):
    df = pd.read_csv(fpath, delimiter="\t", header=None)
    df[0] = df[0].str.rstrip(":")
    df[0] = df[0].str.lower()
    return df


def col_to_feat_map(fpath):
    fields = parse_field_descriptions(fpath)
    d = fields[0].to_dict().items()
    return {col : feat_name.strip() for col, feat_name in d}


def feat_to_col_map(fpath):
    fields = parse_field_descriptions(fpath)
    d = fields[0].to_dict().items()
    return {feat_name.strip() : col for col, feat_name in d}