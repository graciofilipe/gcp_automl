
# TODO(developer): Uncomment and set the following variables
project_id = 'cp100-164016'
compute_region = 'us-central1'
dataset_display_name = 'automl_data'
model_display_name = 'model20200122'
train_budget_milli_node_hours = 1
include_column_spec_names = None
exclude_column_spec_names = None

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)
client.set_target_column(dataset_display_name=dataset_display_name, column_spec_display_name='purchased')
import ipdb; ipdb.set_trace()

# Create a model with the model metadata in the region.
response = client.create_model(
    model_display_name,
    train_budget_milli_node_hours=train_budget_milli_node_hours,
    dataset_display_name=dataset_display_name,
    include_column_spec_names=include_column_spec_names,
    exclude_column_spec_names=exclude_column_spec_names,
)

print("Training model...")
print("Training operation name: {}".format(response.operation.name))
print("Training completed: {}".format(response.result()))