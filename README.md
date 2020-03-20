# tfjs_firefox_issue
Issue related to firefox getting crashed when trying to save a model created in python

# Step1:
Run the python code that creates a model and saves in tfjs-layers format using below code.

python empty_model.py

# Step2:
Do Quantization on the model using below code.

tensorflowjs_converter --input_format tfjs_layers_model --output_format tfjs_layers_model --quantization_bytes 2 <model.json path> <target_dir>

# Step3:
Run the upload_model.html (using intellij or a server) and upload the weights and model.json

# Current Result:
The firefox 74.0 crashes
Works okay in Chrome

# Expected Result:
Should work fine in both the browsers (firefox and chrome)
