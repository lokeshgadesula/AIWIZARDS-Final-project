# Quadratic Model Training with Varying Learning Rates

This repository contains a Python script that demonstrates how to train a quadratic regression model using Stochastic Gradient Descent (SGD) with different learning rates. The purpose of this project is to explore the effects of varying the learning rate on the model's training process and convergence.

## Project Description

The script trains a quadratic model defined by the equation `Y = aX^2 + bX + c`. It tests three different learning rates to observe and compare their impacts on the training dynamics and the final model accuracy. The learning rates tested are:
- 0.001 (Low)
- 0.01 (Medium)
- 0.1 (High)

The training process for each learning rate is visualized by plotting the fitting curve against the provided data points, allowing for an intuitive understanding of how well the model fits the data at the end of training.

## Dependencies

- Python 3.6 or above
- TensorFlow 2.x
- Matplotlib
- Numpy

## Setup and Installation

Ensure that you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/). After installing Python, you can install the required packages using pip:

```bash
pip install tensorflow matplotlib numpy
