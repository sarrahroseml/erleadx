!pip install umap-learn
import umap
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

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

