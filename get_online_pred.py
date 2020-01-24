# TODO(developer): Uncomment and set the following variables
project_id = 'cp100-164016'
compute_region = 'us-central1'
model_display_name = 'model20200122'
inputs = {'price':-1, 'yearOfBirth':1, 'country':"France"}

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)
feature_importance=True

response = client.predict(
    model_display_name=model_display_name,
    inputs=inputs,
    feature_importance=feature_importance)

import ipdb; ipdb.set_trace()

print("Prediction results:")
for result in response.payload:
    print(
        "Predicted class name: {}".format(result.tables.value.string_value)
    )
    print("Predicted class score: {}".format(result.tables.score))

    if feature_importance:
        # get features of top importance
        feat_list = [
            (column.feature_importance, column.column_display_name)
            for column in result.tables.tables_model_column_info
        ]
        feat_list.sort(reverse=True)
        if len(feat_list) < 10:
            feat_to_show = len(feat_list)
        else:
            feat_to_show = 10

        print("Features of top importance:")
        for feat in feat_list[:feat_to_show]:
            print(feat)
