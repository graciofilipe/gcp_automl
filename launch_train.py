
# TODO(developer): Uncomment and set the following variables
import ipdb
from google.cloud import automl_v1beta1 as automl
project_id = 'cp100-164016'
compute_region = 'us-central1'
dataset_display_name = 'automl_data'
model_display_name = 'model20200122'
train_budget_milli_node_hours = 1000
include_column_spec_names = None
exclude_column_spec_names = None


client = automl.TablesClient(project=project_id, region=compute_region)
client.set_target_column(
    dataset_display_name=dataset_display_name, column_spec_display_name='purchased')

# get datatypes right:
types_dict = {"brand": "CATEGORY",
              "changeThumbnail": "FLOAT64",
              "country": "CATEGORY",
              "customerId": "CATEGORY",
              "days_on_site": "FLOAT64",
              "isFemale": "CATEGORY",
              "median_spend": "FLOAT64",
              "num_brand_purchase": "FLOAT64",
              "num_prod_purchase": "FLOAT64",
              "num_type_purchase": "FLOAT64",
              "num_views": "FLOAT64",
              "onSale": "CATEGORY",
              "price": "FLOAT64",
              "productId": "CATEGORY",
              "productType": "CATEGORY",
              "purchased": "CATEGORY",
              "sizeGuide": "FLOAT64",
              "total_spend": "FLOAT64",
              "view360": "FLOAT64",
              "viewCatwalk": "FLOAT64",
              "viewOnly": "FLOAT64",
              "yearOfBirth": "FLOAT64"}


for col_name, col_type in types_dict.items():
    print(col_name)
    client.update_column_spec(dataset_display_name=dataset_display_name,
                              column_spec_display_name=col_name,
                              type_code=col_type)

# Create a model with the model metadata in the region.
response = client.create_model(
    model_display_name,
    train_budget_milli_node_hours=train_budget_milli_node_hours,
    dataset_display_name=dataset_display_name,
    include_column_spec_names=['price', 'yearOfBirth', 'country'],
    optimization_objective=None,
    model_metadata=None,
    disable_early_stopping=False,
)

print("Training model...")
print("Training operation name: {}".format(response.operation.name))
print("Training completed: {}".format(response.result()))
