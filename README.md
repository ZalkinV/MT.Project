# Arrhythmia detection

This repo visualize ECG files from [this dataset][dataset] which contains part of the whole data used in following [article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6784839/) from Stanford University.

## Dataset description
This dataset contains 328, 30sec strips of ECG captured at 200 Hz. Each ECG file is saved in int16 binary format. Filenames ending in _grp[0-2] are reference labels, which are annotated by a group of cardiologists. In addition to reference files, each ECG strip also has 6 additional labels, with filenames ending in _rev[0-5] that correspond to 6 individual cardiologists annotating the data separately. Annotation files are saved in json format, with the list of rhythms saved under an "episodes" key.

## How to use
1. Install packages from reqirements.txt.
1. Create directory `data` near `cardiol_reader.py`.
1. [Download dataset][dataset] and place its content (.ecg and .json files) in `data`.
1. Run the script `cardiol_reader.py`
1. Result will be saved in directory `results`. Each ECG file will have its own directory (named same as ECG id) containing images with revisions from different reviewers for this ECG.

## Output examples
For ECG `0ad9398983ae9cf82a6dca3afb905ab7_0001`:  
![3](https://user-images.githubusercontent.com/32573127/69493366-23c6e080-0ebf-11ea-9c48-6134cbe195d5.png)
![4, 5, 6](https://user-images.githubusercontent.com/32573127/69493340-d77ba080-0ebe-11ea-8e87-23a596534f2c.png)

For ECG `0f2ec83439a8d5495ff4613aee236851_0002`:  
![2](https://user-images.githubusercontent.com/32573127/69493358-101b7a00-0ebf-11ea-9725-c6c013c2dcbd.png)
![3](https://user-images.githubusercontent.com/32573127/69493380-58d33300-0ebf-11ea-875a-1cdca730ac1a.png)



[dataset]: https://irhythm.github.io/cardiol_test_set/
