import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import visualization_utils
SHOW_WEIGHTED = True # show weighted accuracy instead of unweighted accuracy
PLOT_CLIENTS = False
stat_file = 'metrics_stat.csv' # change to None if desired
sys_file = None # change to None if desired

stat_metrics, sys_metrics = visualization_utils.load_data(stat_file, sys_file)
if stat_metrics is not None:
    visualization_utils.plot_accuracy_vs_round_number(stat_metrics, True, plot_stds=False)