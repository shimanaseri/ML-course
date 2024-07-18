# Mini Project 2 - Learning Objectives

## Overview

This repository contains solutions to Mini Project 2, which focuses on advanced machine learning concepts and techniques.

## What You'll Learn

### Question 1: Activation Functions and Neural Networks
1. **Activation Functions:** Assume a binary classification problem with the last layer of your network using either a Sigmoid or ReLU activation function. Discuss what happens in each case.
   - **Equation for ELU:**
     - ELU(x) = x if x >= 0
     - ELU(x) = α (e^x - 1) if x < 0

2. **McCulloch-Pitts Neuron:** Design a simple neural network using a McCulloch-Pitts neuron to separate the shaded triangular area shown in Figure 1(a). The network should randomly generate 2000 points and classify them into two classes. Use two different activation functions and plot the decision boundary.

- <a href="https://github.com/shimanaseri/ML-coarse/blob/main/Mini%20Projects/Mini%20Project%202/q1.ipynb"><strong>Q1 code »</a>

### Question 2: Bearing Fault Detection
1. **CWRU Bearing Dataset:** Extend your knowledge from a previous mini project on the CWRU Bearing dataset. Add three more fault classes (OR007@6_X and 2B007_X). Provide a brief explanation of the different fault types in these files.

2. **Feature Extraction and Model Training:** Perform all tasks from question 2 of the previous mini project on this new dataset. Implement and explain the use of "validation" in addition to training and testing splits.

3. **Multi-Layer Perceptron:** Train a simple Multi-Layer Perceptron (MLP) model with 2 or more hidden layers on the prepared data. Optimize and select appropriate loss functions and optimizers. Plot the loss and accuracy for both training and validation sets. Provide a detailed analysis using classification reports and confusion matrices.

4. **Optimizer and Loss Function Comparison:** Compare the results with a different optimizer and loss function from the previous steps. Analyze how the change affects the results.

- <a href="https://github.com/shimanaseri/ML-coarse/blob/main/Mini%20Projects/Mini%20Project%202/q2.ipynb"><strong>Q2 code »</a>

### Question 3: Decision Trees and Ensemble Methods
1. **Dataset for Classification:** Choose a dataset related to drug or forest cover type classification. Split the data into training and testing sets. Explain your method of selecting data for the training and testing splits.

2. **Decision Tree Classifier:** Implement a decision tree classifier on the dataset. Evaluate the model using at least three performance metrics and a confusion matrix. Analyze the results thoroughly.

3. **Effect of Hyperparameter Tuning:** Explore the effect of hyperparameter tuning on the performance of the decision tree. Explain the advantages and disadvantages of pruning the tree.

4. **Ensemble Methods:** Explain how ensemble methods like Random Forest and AdaBoost can improve the results. Implement one of these methods with suitable hyperparameters and compare the results with the previous steps.

- <a href="https://github.com/shimanaseri/ML-coarse/blob/main/Mini%20Projects/Mini%20Project%202/q3.ipynb"><strong>Q3 code »</a>


### Question 4: Heart Disease Dataset Analysis

1. **Heart Disease Dataset:** Use the heart disease dataset to classify the presence of heart disease. Split the data into training and testing sets, ensuring proper preprocessing.

2. **Naive Bayes Classifier:** Implement a Gaussian Naive Bayes classifier. Use confusion matrices and classification reports to compare Micro and Macro average metrics.

3. **Prediction Comparison:** Randomly select five data points from the test set and compare the predicted results with the actual results.

- <a href="https://github.com/shimanaseri/ML-coarse/blob/main/Mini%20Projects/Mini%20Project%202/q4.ipynb"><strong>Q4 code »</a>

## License

This project is licensed under the [MIT License](LICENSE)

<p align="right">(<a href="#top">back to top</a>)</p>
