# Machine Learning Final Project: Zernike Feature Extraction and Classification
This repository contains the code and data for a machine learning project focused on Zernike feature extraction and classification using various machine learning models.The goal of this project is to classify image data by leveraging Zernike feature extraction and machine learning techniques. Zernike moments are used to capture image features, which are then fed into various classifiers such as Support Vector Machines (SVM), Decision Trees (DT), and Random Forests (RF).

## Required Dependencies Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
pip install --upgrade "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
```
## Results
The project demonstrates the effectiveness of using Zernike moments for feature extraction in image classification tasks. The MLP with Renyi Loss is the optimal choice for applications that require high accuracy, fast execution time, and simplicity in development. The MLP model is also suitable for more general applications that require a balance between accuracy and ease of development. The SVM model is recommended for applications that require more complexity and the ability to fine-tune parameters. The decision tree model is suitable for quick decision-making with minimal complexity. Finally, the random forest model is recommended for applications that require high accuracy and the ability to process large datasets.

## Conclusion
This project successfully implemented a pipeline for image classification using Zernike feature extraction and various machine-learning models. The results indicate that MLP with Renyi Loss are particularly effective for this task. Further work could explore deep learning approaches and further optimization of feature extraction techniques.

## License

This project is licensed under the [MIT License](LICENSE)

<p align="right">(<a href="#top">back to top</a>)</p>
