import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import seaborn.objects as so


from PIL import Image

# Set plot style
sns.set(color_codes=True)
sns.set_style("darkgrid")
sns.diverging_palette(h_neg=0, h_pos=355, s=100, l=50, sep=1, n=16, center="dark", as_cmap=False)
plt.rcParams["figure.figsize"] = 15, 8

def plot_barplot_pie(
    df: pd.DataFrame,
    target: str,
    suptitle: str | None = None,
    savepath: str | None = None
    ) -> None:
    """
    Plots a bar and pie chart for the target variable distribution.
    Saves the output to a file if savepath is provided, or defaults to ./assets/{target}_distribution.jpg
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    target (str): The target variable for which the distribution is to be plotted.
    suptitle (str | None): The title for the plot. If None, defaults
        to "{target} distribution".
    savepath (str | None): The path where the plot will be saved. If None, defaults to "./assets/{target}_distribution.jpg".
    If savepath does not end with .jpg, it will be appended with .jpg.
    Returns:
    None: The function saves the plot to the specified path and displays it.
    """
    plt.figure(figsize=(15, 8))

    # Bar chart
    plt.subplot(1, 2, 1)
    plt.bar(df[target].value_counts().index, df[target].value_counts().values)
    plt.xticks(rotation=335)

    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(
        x=df[target].value_counts(),
        labels=df[target].value_counts().index,
        autopct="%1.1f%%",
        shadow=True,
    )
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    if suptitle is None:
        suptitle = f"{target} distribution"
    plt.suptitle(suptitle, fontdict={"fontsize": 10})
    # plt.subplots_adjust(top=0.85)
    plt.show()
    plt.tight_layout()

    # Create ./assets if missing
    os.makedirs("./assets", exist_ok=True)
    savepath = savepath

    # If savepath is None, set default path
    # Finalize savepath
    if savepath is None:
        savepath = f"./assets/{target}_distribution.jpg"
        
    elif not savepath.endswith(".jpg"):
        savepath = f"./assets/{savepath}.jpg"
       
    else:
        savepath = f"./assets/{savepath}"
    plt.savefig(savepath, format="jpg", dpi=300, bbox_inches="tight")
    
    # img = Image.open(savepath)
    plt.show()
    plt.close()

    print(f"[INFO] Saved plot to {savepath}")

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv("./src/data/dataset.csv")
    target = 'Funnel_category'
    suptitle = 'Funnel Category'
    plot_barplot_pie(df, target=target, suptitle=suptitle)