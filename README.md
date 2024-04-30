
## Project Title: SGD Optimizer

### Team Name: AI Wizards

### Team Members:
1. Lokeshprasanth Gadesula, S02059399, Graduate
2. Siva Kalyan Reddy Kancharla, S02054983, Graduate
3. Gottam Sri Pawan Kalyan Reddy, S02061041, Graduate
4. Raghu Satram, S02058552, Graduate
5. Cyril Chowdary Thoomu, S02059332, Graduate
6. Shake Tanver Mahmud, S02061733, Graduate
7. Venkata Ravindra, S02060445, Graduate

### Project Overview:
This project focuses on implementing quadratic regression using Gradient Descent (GD) and Stochastic Gradient Descent (SGD) optimization algorithms. The goal is to fit a quadratic curve to a set of data points using a model with at least three features. The project includes two main parts: 
1. Gradient Descent Optimization
2. Stochastic Gradient Descent Optimization

### Project Components:
1. **Data Loading:** The provided dataset consists of pairs of (X, Y) values, which are loaded for training the regression model.
2. **Model Definition:** A quadratic model with the equation 𝑌=𝑎𝑋^2+𝑏𝑋+𝑐 is defined, where 𝑎, 𝑏, and 𝑣 are the features to be learned by the model.
3. **Gradient Descent Optimization:** The GD optimizer is implemented to update the feature weights 𝑎, 𝑏, and 𝑣 using the provided learning rate. The fitting curve for each epoch and the history of feature weights update are logged.
4. **Stochastic Gradient Descent Optimization:** The SGD optimizer is implemented to update the feature weights using a mini-batch approach. Similar to GD, the fitting curve for each epoch and the history of feature weights update are logged.
5. **Extended Feature Experiments:** Experiments are conducted with models incorporating more than three features to evaluate performance variations with increasing model complexity. Models with four and five features are tested, and the results are analyzed.
6. **Learning Rate Experiment:** The impact of different learning rates on the training of the quadratic model using SGD is observed. Three different learning rates (0.001, 0.01, and 0.1) are evaluated, and the results are compared.

### Source Code:
The source code for each component of the project is provided in Python using TensorFlow library for implementing the optimization algorithms and Matplotlib for visualization.

### Instructions for Running the Code:
1. Ensure that Python and required libraries (TensorFlow, NumPy, Matplotlib) are installed.
2. Run each source code file in a Python environment to execute the corresponding experiment.
3. View the output plots to observe the training progress and results of each experiment.

### Note:
- For Gradient Descent and Stochastic Gradient Descent, extra points can be obtained by experimenting with different numbers of features and learning rates as specified in the project requirements.
- The code provides detailed comments and documentation for better understanding of the implementation and experiment results.

### Conclusion:
This project provides a comprehensive exploration of quadratic regression using optimization algorithms like Gradient Descent and Stochastic Gradient Descent. By conducting experiments with varying model complexities and learning rates, the project aims to deepen understanding of optimization techniques in machine learning regression tasks.

# Neural Network 

## Motivation and Significance
Predictive maintenance is crucial in industrial settings to minimize downtime and ensure safety. This project aims to use machine learning to predict equipment failures based on vibration data, allowing for proactive maintenance and resource optimization.

## References
- Sikorska, J.Z., et al. "Prognostic modelling options for remaining useful life estimation by industry." Mechanical Systems and Signal Processing 25.5 (2011): 1803-1836.
- Lei, Y., et al. "A review on empirical mode decomposition in fault diagnosis of rotating machinery." Mechanical Systems and Signal Processing 35.1-2 (2013): 108-126.

## Methodology
- Data Preprocessing: Vibration data was collected and preprocessed, including noise filtering and feature extraction.
- Model Training: A Random Forest classifier was trained on historical data labeled with 'normal operation' and 'failure' states.
- Evaluation: The model's performance was evaluated using metrics such as accuracy, precision, and feature importance.

## Results
The model achieved an accuracy of 95%, with a precision of 96% for failure detection. Key features such as RMS and kurtosis were identified as significant predictors of failures.

## Strengths and Limitations
Strengths:
- High accuracy and precision in failure prediction.
- Real-time implementation using existing sensor data.

Limitations:
- Dependency on high-quality, labeled training data.
- Potential cost and time implications for obtaining labeled data.

## Usage
1. Install required dependencies: `pip install -r requirements.txt`
2. Run the `predictive_maintenance.py` script to train the model and make predictions.

## Contributors
- Lokeshprasanth Gadesula
- Siva Kalyan Reddy Kancharla
- Gottam Sri Pawan Kalyan Reddy
- Raghu Satram
- Cyril Chowdary Thoomu
- Shake Tanver Mahmud
- Venkata Ravindra

## Acknowledgments
We would like to express our gratitude to Professor Fabio Santos for his guidance and support throughout this project.

