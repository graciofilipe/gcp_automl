# TODO(developer): Uncomment and set the following variables
project_id = 'cp100-164016'
compute_region = 'us-central1'
dataset_display_name = 'automl_data'
path = 'gs://automl-tables-filipegracio/train_head_data.csv'

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)

response = None
if path.startswith("bq"):
    response = client.import_data(
        dataset_display_name=dataset_display_name, bigquery_input_uri=path
    )
else:
    # Get the multiple Google Cloud Storage URIs.
    input_uris = path.split(",")
    response = client.import_data(
        dataset_display_name=dataset_display_name,
        gcs_input_uris=input_uris,
    )

print("Processing import...")
# synchronous check of operation status.
print("Data imported. {}".format(response.result()))