import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------
single_file_acc = pd.read_csv("../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv")#Acclerometer Data
single_file_gyr = pd.read_csv("../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv") #Gyroscope Data
# --------------------------------------------------------------
# List all data in data/raw/MetaMotion
# --------------------------------------------------------------
files = glob("../../data/raw/MetaMotion/*.csv") #list all the csv file in the dataset
len(files)


# 
#-------------------------------------------------------------
# Extract features from filename
# --------------------------------------------------------------

data_path = "../../data/raw/MetaMotion/"
f = files[0] #first file
participate = f.replace("\\", "/").split("/")[-1].split("-")[0]
lable = f.split("-")[1]
category = f.split("-")[2].rstrip("123")



df = pd.read_csv(f)

df['participate'] = participate
df['lable'] = lable
df['category'] = category

# --------------------------------------------------------------
# Read all files
# --------------------------------------------------------------
acc_df = pd.DataFrame()
gyr_df = pd.DataFrame()

acc_set = 1
gyr_set = 1

for f in files:
    participate = f.replace("\\", "/").split("/")[-1].split("-")[0]
    label = f.split("-")[1]
    category = f.split("-")[2].rstrip("2").rstrip("_MetaWear_2019")
    
    df = pd.read_csv(f)
    
    df['participate'] = participate
    df['label'] = label
    df['category'] = category
    
    if "Accelerometer" in f:
        df['set'] = acc_set
        acc_set += 1
        acc_df = pd.concat([acc_df, df], ignore_index=True)
        
    if "Gyroscope" in f:
        df['set'] = gyr_set
        gyr_set += 1
        gyr_df = pd.concat([gyr_df, df], ignore_index=True)

# acc_df[acc_df['set'] == 1]   
    


# --------------------------------------------------------------
# Working with datetimes
# --------------------------------------------------------------

acc_df.info()
gyr_df.info()

pd.to_datetime(df['epoch (ms)'],unit='ms')


acc_df.index = pd.to_datetime(acc_df['epoch (ms)'],unit='ms')
gyr_df.index = pd.to_datetime(gyr_df['epoch (ms)'],unit='ms')

del acc_df ["epoch (ms)"]
del acc_df ["time (01:00)"]
del acc_df ["elapsed (s)"]

del gyr_df ["epoch (ms)"]
del gyr_df ["time (01:00)"]
del gyr_df["elapsed (s)"]


# df['time (01:00)'].dt.week
# pd.to_datetime(df['time (01:00)']).dt.month


# --------------------------------------------------------------
# Turn into function - this is the main part 
# --------------------------------------------------------------
files = glob("../../data/raw/MetaMotion/*.csv")

def read_data_frame_files(files):
    acc_df = pd.DataFrame()
    gyr_df = pd.DataFrame()

    acc_set = 1
    gyr_set = 1

    for f in files:
        
        participate = f.replace("\\", "/").split("/")[-1].split("-")[0]
        label = f.split("-")[1]
        category = f.split("-")[2].rstrip("2").rstrip("_MetaWear_2019")
        
        df = pd.read_csv(f)
        
        df['participate'] = participate
        df['label'] = label
        df['category'] = category
        
        if "Accelerometer" in f:
            df['set'] = acc_set
            acc_set += 1
            acc_df = pd.concat([acc_df, df], ignore_index=True)
            
        if "Gyroscope" in f:
            df['set'] = gyr_set
            gyr_set += 1
            gyr_df = pd.concat([gyr_df, df], ignore_index=True)
            
    acc_df.index = pd.to_datetime(acc_df['epoch (ms)'],unit='ms')
    gyr_df.index = pd.to_datetime(gyr_df['epoch (ms)'],unit='ms')

    del acc_df ["epoch (ms)"]
    del acc_df ["time (01:00)"]
    del acc_df ["elapsed (s)"]

    del gyr_df ["epoch (ms)"]
    del gyr_df ["time (01:00)"]
    del gyr_df["elapsed (s)"]
    
    return acc_df,gyr_df

acc_df,gyr_df = read_data_frame_files(files)



# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------

data_merged = pd.concat([acc_df.iloc[:,:3],gyr_df],axis=1)# axis=1 column wise concate

# data_merged.head(50)

data_merged.columns = [
    "acc_x",
    "acc_y",
    "acc_z",
    "gyr_x",
    "gyr_y",
    "gyr_z",
    "participant",
    "label",
    "category",
    "set",
]

# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------
# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz
data_merged.columns

sampling = {
    'acc_x':'mean', 
    'acc_y':'mean',
    'acc_z':'mean',
    'gyr_x':'mean',
    'gyr_y':'mean',
    'gyr_z':'mean',
    'participant':"last",
    'label': "last",
    'category': "last",
    'set':"last",
}

data_merged[:] # all rows and columns
data_merged[:100] #ist 100 rows

data_merged[:100].resample('200ms').mean(numeric_only=True)


data_merged[:100].resample('200ms').apply(sampling)

# split with day
days =  [g for n , g in data_merged.groupby(pd.Grouper(freq= "D"))]
days[0] # 11th january

data_resampled = pd.concat([df.resample(rule='200ms').apply(sampling).dropna() for df in days])


data_resampled.info()
data_resampled['set'] = data_resampled['set'].astype('int')

# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------

data_resampled.to_pickle("../../data/interim/01_data_processed.pkl")

