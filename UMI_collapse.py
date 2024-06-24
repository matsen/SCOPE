import gzip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
import sys


def collapse_UMIs(library_csv, output_file):
    start_1 = time.time()
    
    library = pd.read_csv(library_csv, usecols = ["R1_full_bc", "R1_UMI", "SR", "R2_UMI", "R2_full_bc"])
    
    print(f"library loaded; time taken: {time.time() - start_1}")

    pre_collapse_len = len(library)
    print(f"pre-collapse: {pre_collapse_len}")
    
    start_2 = time.time()

    library.sort_values(by=['R1_full_bc'], inplace=True)

    print(f"library sorted; time taken: {time.time() - start_2}")

    start_3 = time.time()

    library.drop_duplicates(inplace=True)

    print(f"library duplicates dropped, time taken: {time.time() - start_3}")

    start_4 = time.time()

    library.to_csv(output_file)

    print(f"library to csv done, time taken: {time.time() - start_4}")

    post_collapse_len = len(library)
    print(f"post-collapse: {post_collapse_len}")
    
    print(f"dedup ratio: {post_collapse_len/pre_collapse_len}")




collapse_UMIs(sys.argv[1], sys.argv[2])

"""

sys.argv[1]: pre collapse csv file (input)
sys.argv[1]: post collapse csv file (output)

"""