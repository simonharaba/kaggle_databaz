# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import pandas as pd
import numpy as np
import seaborn as sns

data_frame = pd.read_csv('../input/graphics-card-full-specs/gpu_specs_v6.csv')
data_frame

data_frame["manufacturer"].unique()

data_frame.describe

#data_frame["memSize"].hist()
data_frame["memClock"].hist()
data_frame["gpuClock"].hist()

data_frame["memBusWidth"].hist()

data_frame[data_frame["manufacturer"]=="NVIDIA"]

data_frame.sort_values("memSize", ascending=False)

data_frame.groupby("memType").mean()

data_frame.groupby("manufacturer").mean()

data_frame.dropna()
data_frame.reset_index()

for columns in data_frame.columns:
    print(columns)

    # lets see who manufactures the best GPUs
important_gpu_specs = pd.DataFrame(data_frame, columns=["manufacturer", "memSize", "memBusWidth", "gpuClock", "tmu", "memClock"])
important_gpu_specs

sns.set()
sns.scatterplot(x="memSize", y="memBusWidth", data=important_gpu_specs)

sns.scatterplot(x="gpuClock", y="memClock", data=important_gpu_specs)

sns.relplot(x="memSize", y="tmu", hue="memSize", style="tmu", data=important_gpu_specs)

sns.relplot(x="memClock", y="gpuClock", hue="memSize", data=important_gpu_specs)

graph1 = sns.relplot(x="memSize", y="memBusWidth", kind="line", ci=None, sort=False, data=important_gpu_specs)
graph1.figure.autofmt_xdate()

memorysize_to_memorybandwidth = sns.relplot(x="memSize", y="memBusWidth", kind="line", ci=None, sort=True, data=important_gpu_specs)
memorysize_to_memorybandwidth.figure.autofmt_xdate()

graph2 = sns.relplot(x="gpuClock", y="tmu", kind="line", ci=None, data=important_gpu_specs)
graph2.figure.autofmt_xdate()

gpu_clock_speeds = sns.displot(important_gpu_specs, x="gpuClock", hue="manufacturer", multiple="stack")

from bokeh.plotting import figure,show
from bokeh.models import HoverTool

TOOLTIPS = HoverTool(tooltips=[
    ("(memSize,memBusWidth)", "(@memSize, @memBusWidth)"),
    ("(memClock,gpuClock)", "(@memClock, @gpuClock)"), 
    ("manufacturer", "@manufacturer")
])

p = figure(title="Soccer 2019", x_axis_label='memSize', y_axis_label='memBusWidth', plot_width=700, plot_height=700, tools=[TOOLTIPS])
p.circle('memSize', 'memBusWidth', size=10, source=important_gpu_specs)
p.circle('memClock', 'gpuClock', size=10, source=important_gpu_specs)
show(p)

gpu_memorysize_to_memorybandwidth = sns.displot(important_gpu_specs,x="memBusWidth", hue="manufacturer", multiple="stack")

important_gpu_specs.sort_values("tmu", ascending=False)

important_gpu_specs.groupby("memSize").mean()

important_gpu_specs.describe()

high_memory_size_gpus = important_gpu_specs[important_gpu_specs["memSize"]>3.113803]
print(high_memory_size_gpus.shape)
print(important_gpu_specs.shape)
print(f'there are only {high_memory_size_gpus.shape[0]} gpus with memory size more than the average of 3.113803')

gpus_with_faster_processing_highGPUClocks = high_memory_size_gpus[high_memory_size_gpus["gpuClock"]>661.126687]
gpus_with_faster_processing_highGPUClocks_andBandwidth = gpus_with_faster_processing_highGPUClocks[gpus_with_faster_processing_highGPUClocks["memBusWidth"]>274.874445]
gpus_with_faster_processing_highGPUClocks_andBandwidth

gpus_with_faster_processing_highGPUClocks_andBandwidth.shape
# so it eventually looks like there are just 162 very good GPUs

gpus_with_faster_processing_highGPUClocks_andBandwidth["manufacturer"].unique()
# only the top three companies manufacture these best gpus