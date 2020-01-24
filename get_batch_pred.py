
# TODO(developer): Uncomment and set the following variables
project_id = 'cp100-164016'
compute_region = 'us-central1'
model_display_name = 'model20200122'
gcs_input_uris = 'gs://automl-tables-filipegracio/for_batch_pred.csv'
gcs_output_uri = 'gs://automl-tables-filipegracio/'

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)

# Query model
response = client.batch_predict(gcs_input_uris=gcs_input_uris,
                                gcs_output_uri_prefix=gcs_output_uri,
                                model_display_name=model_display_name)
print("Making batch prediction... ")
response.result()
print("Batch prediction complete.\n{}".format(response.metadata))
