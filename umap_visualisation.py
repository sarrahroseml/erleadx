!pip install umap-learn
import umap.umap_ as umap
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

#RawCT
df_umap = pd.read_csv("/Users/sarrahrose/Downloads/29May_RawCT - Sheet1 (1).csv")
X = df_umap[[ 'Biomarker 1','Biomarker 2','Biomarker 3','Biomarker 5','Biomarker 9','Biomarker 10','Biomarker 12','Biomarker 16']]  

# Perform dimensionality reduction with UMAP
umap_model = umap.UMAP(n_neighbors=20, min_dist=0.50, n_components=4, metric='manhattan',random_state=42)
umap_result = umap_model.fit_transform(X, df_umap['Disease'])

# Add x and y axis labels
plt.xlabel('UMAP1')
plt.ylabel('UMAP2')

# Visualize the results
plt.scatter(umap_result[:, 0], umap_result[:, 1], c=df_umap['Disease'])
plt.colorbar()
plt.show()

# assume that X is your data and y is your cluster labels
silhouette_coefficient = silhouette_score(umap_result, df_umap['Disease'])
davies_bouldin_index = davies_bouldin_score(umap_result, df_umap['Disease'])
calinski_harabasz_index = calinski_harabasz_score(umap_result, df_umap['Disease'])

print("Silhouette Coefficient: ", silhouette_coefficient)
print("Davies-Bouldin Index: ", davies_bouldin_index)
print("Calinski-Harabasz Index: ", calinski_harabasz_index)
