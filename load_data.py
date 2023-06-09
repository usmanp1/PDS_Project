import pandas as pd
import glob

def load_data(folder_path):
    
    file_list = glob.glob(folder_path + "/*.csv")
    
    data_frame = []
    
    for filename in file_list:
        df = pd.read_csv(filename, index_col=None, header=0)
        data_frame.append(df)
            
    combined_df = pd.concat(data_frame, axis=0, ignore_index=True)
            
    return combined_df