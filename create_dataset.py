project_id = 'cp100-164016'
compute_region = 'us-central1'
dataset_display_name = 'automl_data'

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)

# Create a dataset with the given display name
dataset = client.create_dataset(dataset_display_name)

# Display the dataset information.
print("Dataset name: {}".format(dataset.name))
print("Dataset id: {}".format(dataset.name.split("/")[-1]))
print("Dataset display name: {}".format(dataset.display_name))
print("Dataset metadata:")
print("\t{}".format(dataset.tables_dataset_metadata))
print("Dataset example count: {}".format(dataset.example_count))
print("Dataset create time:")
print("\tseconds: {}".format(dataset.create_time.seconds))
print("\tnanos: {}".format(dataset.create_time.nanos))