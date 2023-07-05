""""
This file is meant to train a UMAP plot and use test data on it.
""""

##Part 1
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df_umap = pd.read_csv("/Users/sarrahrose/Downloads/hello_ds./FoldChange- Test Data 20Feb.csv")
X = df_umap[[ 'Biomarker 3','Biomarker 5','Biomarker 6','Biomarker 7','Biomarker 11','Biomarker 9','Biomarker 16','Biomarker 15']]  # assuming the first two columns are IDs and labels

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

# Part 2 
df_train = pd.read_csv("Users/sarrahrose/Downloads/hello_ds./FoldChange Final - Test Data 20Feb.csv")
X = df_train[['Disease', 'Biomarker 3','Biomarker 5','Biomarker 6','Biomarker 7','Biomarker 11','Biomarker 9','Biomarker 16','Biomarker 15']]

df_test=pd.read_csv("Users/sarrahrose/Downloads/hello_ds./FoldChange Final - Test Data 20Feb.csv")
Y = df_test [['Disease','Biomarker 3','Biomarker 5','Biomarker 6','Biomarker 7','Biomarker 11','Biomarker 9','Biomarker 16','Biomarker 15']]
Y = Y.iloc[:,2:] 

# Perform dimensionality reduction with UMAP
#umap_model = umap.UMAP(n_neighbors=12, min_dist=0.70, n_components=3, metric='manhattan',random_state=42)
umap_model = umap.UMAP(n_neighbors=20, min_dist=0.50, n_components=4, metric='manhattan',random_state=42)
umap_result = umap_model.fit_transform( X.iloc[:,2:] , df_train['Disease'])


# Apply the UMAP model to the new data
valid_embedding = umap_model.transform()

# Generate UMAP1 scores
umap2_scores = valid_embedding[:, 0]

# Generate predictions based on UMAP1 scores
predictions = []
for score in umap2_scores:
    if score <-7 :
        predictions.append(0)
    else:
        predictions.append(1)

# Add the predictions to the new dataset
new_data['Predictions'] = predictions

