import streamlit as st
import os
import re
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

st.title("Keras Training Basic UI")
st.header("A Streamlit based Web UI To Create And Train Models")
st.subheader("Create Network:")