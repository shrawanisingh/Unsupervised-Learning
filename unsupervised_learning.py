import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def load_data(path: Path) -> pd.DataFrame:
    """Load car attributes from a JSON file into a DataFrame."""
    with path.open() as f:
        data = json.load(f)
    return pd.DataFrame(data)


def elbow_method(df: pd.DataFrame, output: Path) -> None:
    """Generate an elbow plot for K values from 2 to 10."""
    scaler = StandardScaler()
    X = scaler.fit_transform(df)
    inertias = []
    ks = range(2, 11)
    for k in ks:
        kmeans = KMeans(n_clusters=k, n_init="auto", random_state=42)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)

    plt.figure()
    plt.plot(list(ks), inertias, marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method for K-Means")
    plt.tight_layout()
    plt.savefig(output)


def train_kmeans(df: pd.DataFrame, n_clusters: int):
    """Train KMeans and append cluster labels to the DataFrame."""
    scaler = StandardScaler()
    X = scaler.fit_transform(df)
    model = KMeans(n_clusters=n_clusters, n_init="auto", random_state=42)
    labels = model.fit_predict(X)
    labeled_df = df.copy()
    labeled_df["cluster"] = labels
    return model, scaler, labeled_df


def main() -> None:
    data_path = Path("Car-Attributes.json")
    elbow_plot = Path("elbow_plot.png")
    df = load_data(data_path)
    elbow_method(df, elbow_plot)

    model, scaler, labeled_df = train_kmeans(df, n_clusters=4)
    labeled_df.to_csv("clustered_cars.csv", index=False)
    print(labeled_df.groupby("cluster").size())

    # Predict cluster for a sample using the feature means
    sample = df.mean().to_frame().T
    sample_scaled = scaler.transform(sample)
    cluster = model.predict(sample_scaled)[0]
    print("Mean feature sample assigned to cluster:", cluster)


if __name__ == "__main__":
    main()
