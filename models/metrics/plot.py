import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import visualization_utils

stat_file = 'metrics_stat.csv'

stat_metrics, sys_metrics = visualization_utils.load_data(stat_file, None)
if stat_metrics is not None:
    visualization_utils.plot_accuracy_vs_round_number(stat_metrics, True, plot_stds=False)