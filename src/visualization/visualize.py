import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

# --------------------------------------------------------------
# Load data
# --------------------------------------------------------------
df = pd.read_pickle("../../data/interim/01_data_processed.pkl")

# --------------------------------------------------------------
# Plot single columns
# --------------------------------------------------------------
set_df = df[df["set"] == 1]

plt.plot(set_df["acc_y"].reset_index(drop=True))

# --------------------------------------------------------------
# Plot all exercises
# --------------------------------------------------------------
df["label"].unique()

for label in df['label'].unique():
    subset = df[df['label'] == label]
    fig, ax  = plt.subplots()
    plt.plot(subset["acc_y"].reset_index(drop=True),label = label)
    plt.legend()
    plt.show()
    
for label in df['label'].unique():
    subset = df[df['label'] == label]
    fig, ax  = plt.subplots()
    plt.plot(subset[:100]["acc_y"].reset_index(drop=True),label = label)
    plt.legend()
    plt.show()

# --------------------------------------------------------------
# Adjust plot settings
# --------------------------------------------------------------
# Customizing Matplotlib with style sheets and rcParams
import matplotlib as mpl
mpl.style.use('seaborn-v0_8-deep')
mpl.rcParams['figure.figsize'] = (20,5)
mpl.rcParams['figure.dpi'] = 100
# After this we use forloop to check is it showing or not 
for label in df['label'].unique():
    subset = df[df['label'] == label]
    fig, ax  = plt.subplots()
    plt.plot(subset[:100]["acc_y"].reset_index(drop=True),label = label)
    plt.legend()
    plt.show()
# --------------------------------------------------------------
# Compare medium vs. heavy sets
# --------------------------------------------------------------

category_df = df.query("label == 'squat'").query("participant == 'A' ").reset_index()



fig, ax = plt.subplots()
category_df.groupby('category')['acc_y'].plot(ax=ax)
ax.set_ylabel('acc_y')
ax.set_xlabel('samples')
ax.legend(title='category')
plt.show()


# --------------------------------------------------------------
# Compare participants
# --------------------------------------------------------------
participants_df = df.query("label == 'bench' ").sort_values('participant').reset_index()

fig, ax = plt.subplots()
participants_df.groupby('participant')['acc_y'].plot(ax=ax)
ax.set_ylabel('acc_y')
ax.set_xlabel('samples')
ax.legend(title='participant')
plt.show()

# --------------------------------------------------------------
# Plot multiple axis
# --------------------------------------------------------------
lebel = "squat"
participant = "A"
all_axis_df = df.query(f'label == "{label}"').query(f'participant == "{participant}"').reset_index()

fig, ax = plt.subplots()
all_axis_df[['acc_x','acc_y','acc_z']].plot(ax = ax)
ax.set_ylabel('acc_y')
ax.set_xlabel('samples')
ax.legend()
plt.show()
# --------------------------------------------------------------
# Create a loop to plot all combinations per sensor
# --------------------------------------------------------------
labels = df["label"].unique()
participants = df['participant'].unique()

for label in labels:
    for participant in participants:

        all_axis_df = (
            df.query(f'label == "{label}"')
              .query(f'participant == "{participant}"')
              .reset_index(drop=True)
        )

        # Skip empty combinations
        if all_axis_df.empty:
            continue

        fig, ax = plt.subplots(figsize=(12, 4))
        all_axis_df[['acc_x', 'acc_y', 'acc_z']].plot(ax=ax)
        ax.set_xlabel('samples')
        ax.set_ylabel('acceleration')
        ax.set_title(f"{label} ({participant})".title())
        ax.legend()
        plt.show()

#for gryscope data
for label in labels:
    for participant in participants:

        all_axis_df = (
            df.query(f'label == "{label}"')
              .query(f'participant == "{participant}"')
              .reset_index(drop=True)
        )

        # Skip empty combinations
        if all_axis_df.empty:
            continue

        fig, ax = plt.subplots(figsize=(12, 4))
        all_axis_df[['gyr_x', 'gyr_y', 'gyr_z']].plot(ax=ax)
        ax.set_xlabel('samples')
        ax.set_ylabel('acceleration')
        ax.set_title(f"{label} ({participant})".title())
        ax.legend()
        plt.show()

# --------------------------------------------------------------
# Combine plots in one figure
# --------------------------------------------------------------
import matplotlib.pyplot as plt
label = 'row'
participant = 'A'
# Filter data
combined_plot_df = (
    df[(df['label'] == label) & (df['participant'] == participant)]
    .reset_index(drop=True)
)
# Create subplots
fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(20, 10))
# Accelerometer plot
combined_plot_df[['acc_x', 'acc_y', 'acc_z']].plot(ax=ax[0])
ax[0].set_ylabel('Acceleration')
ax[0].set_title(f'{label} ({participant}) - Accelerometer'.title())
# Gyroscope plot
combined_plot_df[['gyr_x', 'gyr_y', 'gyr_z']].plot(ax=ax[1])
ax[1].set_ylabel('Gyroscope')
ax[1].set_xlabel('Samples')
ax[1].set_title(f'{label} ({participant}) - Gyroscope'.title())
# Legends
ax[0].legend(
    loc="upper center",
    bbox_to_anchor=(0.5, 1.15),
    ncol=3,
    fancybox=True,
    shadow=True
)
ax[1].legend(
    loc="upper center",
    bbox_to_anchor=(0.5, 1.15),
    ncol=3,
    fancybox=True,
    shadow=True
)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------
# Loop over all combinations and export for both sensors
# --------------------------------------------------------------

labels = df["label"].unique()
participants = df['participant'].unique()

for label in labels:
    for participant in participants:

       combined_plot_df = (
            df.query(f'label == "{label}"')
              .query(f'participant == "{participant}"')
              .reset_index(drop=True)
        )
       
       if len(combined_plot_df) > 0:
           
            fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(20, 10)) 
            combined_plot_df [["acc_x", "acc_y", "acc_z"]].plot(ax=ax[0]) 
            combined_plot_df [["gyr_x", "gyr_y", "gyr_z"]].plot(ax=ax[1])
            ax[0].legend( loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True,)
            ax[1].legend( loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True)
            ax [1].set_xlabel("Samples")
            plt.savefig(f"../../reports/figures/{label.title()} ({participant}).png") #save 
            plt.show()