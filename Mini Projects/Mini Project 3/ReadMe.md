# Mini Project 3- Learning Objectives

This repository contains solutions to a series of exercises designed to improve understanding of advanced topics in machine learning, specifically focusing on Support Vector Machines (SVM) and neural networks.

## What You'll Learn

### Question 1

1. **SVM on IRIS Dataset:** The goal of this question is to experiment with the SVM algorithm on the well-known IRIS dataset. Follow these steps and include the requested items in your report along with the code:

    a. **Data Loading and Analysis:** Load the IRIS dataset and provide statistical and visual summaries, including the number of samples, dimensions, mean, variance, and correlations. Use t-SNE for dimensionality reduction and analyze if it is effective.

    b. **SVM Classification:** Use the SVM algorithm (both linear and kernel-based) to classify the data. Plot the decision boundaries and confusion matrices. Use dimensionality reduction to visualize the decision boundaries in 2D space.

    c. **Kernel Comparison:** Implement SVM with various kernels (e.g., polynomial) for degrees 1 to 10. Compare and analyze the results using appropriate metrics. Create a GIF showing decision boundaries for each degree.

    d. **Implement SVM from Scratch:** Implement the SVM algorithm without using the `scikit-learn` library. Ensure your implementation includes methods for fitting, predicting, and polynomial kernels. Compare the accuracy of your implementation with the `scikit-learn` implementation for degrees 1 to 10 and create a GIF to visualize the results.

### Question 2

1. **GenSVM Paper Review:** Read the paper "GenSVM: A Generalized Multiclass Support Vector Machine." Summarize the problem, innovative ideas, and methodology presented in the paper. Discuss how this approach differs from traditional SVM methods.

    a. **Reproduce Results:** Implement the methodology from the GenSVM paper using the IRIS dataset. Compare your results with those presented in the paper using all appropriate libraries and tools.

- <a href="https://github.com/shimanaseri/ML-coarse/blob/main/Mini%20Projects/Mini%20Project%203/q2.ipynb"><strong>Q2 code »</a>

### Question 3

1. **Credit Card Fraud Detection:** Review the paper "Credit Card Fraud Detection Using Autoencoder Neural Network." Answer the following questions based on the paper:

    a. **Challenges in Fraud Detection:** Discuss the major challenges in developing fraud detection models and the methods used in the paper to address these challenges.

    b. **Network Architecture:** Provide a brief explanation of the neural network architecture presented in the paper.

    c. **Model Training:** Implement the model presented in the paper using the credit card fraud detection dataset. Ensure to use techniques to avoid overfitting and validate the model properly.

    d. **Evaluation Metrics:** Evaluate the model using accuracy, precision, recall, and F1-score. Discuss why accuracy might not be the best metric for this imbalanced dataset.

    e. **Threshold Analysis:** Analyze the model performance with different threshold values for oversampling, similar to Figure 7 in the paper. Plot the accuracy and recall for different thresholds.

    f. **Noise and Imbalanced Data:** Compare the results of the model trained on imbalanced and noise-free data with the original model. Discuss the differences and possible improvements.

- <a href="https://github.com/shimanaseri/ML-coarse/blob/main/Mini%20Projects/Mini%20Project%203/q3.ipynb"><strong>Q3 code »</a>

## License

This project is licensed under the [MIT License](LICENSE)

<p align="right">(<a href="#top">back to top</a>)</p>
