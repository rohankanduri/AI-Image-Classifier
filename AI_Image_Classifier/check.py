import os

# Set the environment variable to disable or enable oneDNN optimizations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'  # Enable oneDNN optimizations

import tensorflow as tf

print(tf.__version__)  # This will print the TensorFlow version
