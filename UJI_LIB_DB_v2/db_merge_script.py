import os
import pandas as pd

# Function to merge CSV files
def merge_csv_files(input_folder, output_folder, st):
    data_frames_rss = [] 
    data_frames_crd = [] 


    rss_files = [f for f in os.listdir(input_folder) if f.startswith(st) and f.endswith("rss.csv")]
    crd_files = [f for f in os.listdir(input_folder) if f.startswith(st) and f.endswith("crd.csv")]

    # Sort files to maintain proper ordering (assuming filenames contain numerical indexes)
    rss_files.sort()
    crd_files.sort()

    # print(rss_files)

    # Loop through the files in each folder
    for rss_file, crd_file in zip(rss_files, crd_files):
        rss_filename = os.path.join(input_folder, rss_file)
        crd_filename = os.path.join(input_folder, crd_file)

        # Read and append data to respective lists
        data_frames_rss.append(pd.read_csv(rss_filename))
        data_frames_crd.append(pd.read_csv(crd_filename))

        print(data_frames_rss)

    # Concatenate data frames along columns
    # merged_rss = pd.concat(data_frames_rss, axis=0, ignore_index=True)
    # merged_crd = pd.concat(data_frames_crd, axis=0, ignore_index=True)

    # # Write merged data to new CSV file
    # os.makedirs(output_folder, exist_ok=True)

    # merged_rss.to_csv(output_folder + st + "_rss.csv", index=False)
    # merged_crd.to_csv(output_folder + st + "_crd.csv", index=False)

input_folder = "db/" 
output_filename = "merged_db/" 

for i in range(1,2):
    merge_csv_files(f"{input_folder}{str(i).zfill(2)}/", f"{output_filename}{str(i).zfill(2)}/", "trn")
    merge_csv_files(f"{input_folder}{str(i).zfill(2)}/", f"{output_filename}{str(i).zfill(2)}/", "tst")
