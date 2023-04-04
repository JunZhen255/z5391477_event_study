"""yf_example 3"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year: int):
    csv_filename = f"qan_prc_{year}.csv"
    pth = os.path.join(cfg, csv_filename)
    yf_example2.yf_prc_to_csv("QAN.AX", year, csv_filepath)

if __name__ == "__main__":
         qan_prc_to_csv(2020)
