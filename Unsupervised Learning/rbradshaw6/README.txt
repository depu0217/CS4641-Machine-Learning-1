All of the raw data from the tests run can be found in the data folder and in the provided Excel file.

WEKA was used to run the Neural Network.
WEKA was used for the visualization of clusters.
Gyazo was used for screenshotting.

The RandomProjection filter can be found under Filter->Unsupervised->attribute. Press apply.

To generate PCA, ICA, and Insignificant Component Analysis datasets:
    Open up ml-project-3-master in Eclipse.
    Add necessary dependencies (ABAGAIL and WEKA to classpath)
    transformed ARFF files are saved in the src/data directory when you run the java files in the following format:
        ExampleRunner <arff path> <variance thresholds>
    RPRunner takes in a list of attributes to keep as its second argument instead of variance thresholds

The eigenvalues/eigenvectors for PCA are produced in the buffer of WEKA's PCA (with Ranker selected) due to limitations with the github code.

