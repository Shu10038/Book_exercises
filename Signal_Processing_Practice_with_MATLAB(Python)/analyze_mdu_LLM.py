"""
 analyze_mdu_LLM.py
 Created on Tue Jul 11 2023
 @author: S.OHSAWA 

 PyInstallerやNuitkaでexe化することを想定している

"""

import glob
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI



def main(input_csv):
    
    llm = OpenAI(api_token="YOUR-TOKEN")
    pandas_ai = PandasAI(llm, conversational=True)

    csv_df = pd.read_csv(input_csv)
    pandas_ai.run(csv_df, prompt='Scoreが一番大きい日付は？')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv")

    argv = parser.parse_args()

    main(argv.input_csv)