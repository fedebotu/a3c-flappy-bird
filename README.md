# A3C Flappy Bird

Deep Reinforcement Learning implementation in Keras of an AI controlling the popular Flappy Bird videogame, using Asynchronous Advantage Actor Critic (A3C.

<p align="center">
  <img src="https://github.com/Juju-botu/a3c-flappy-bird/blob/master/assets/sprites/FlappyBackground.png">
</p>

By Federico Berto: 
Bachelor's degree thesis for Joint double degree for Tongji University and University of Bologna. For more details, please contact me at: berto.federico2@gmail.com

Original implementation:
For more information about the project details, see this [blog post](https://shalabhsingh.github.io/Deep-RL-Flappy-Bird/) associated with this project.

See LICENSE for further details
Copyright (c) 2019 Federico Berto
based on:
Copyright (c) 2017 Shalabh Singh

# Installation of Dependencies
* Python 3.5
* Keras 2.0
* pygame 
* scikit-image

# How to Run?
Clone the repository or download it. To test the pretrained model, run the "test.py" file. To retrain the model from scratch, run the "train_network.py" file and the trained models at different stages will be saved in "saved_models" folder.

# Disclaimer
This work is based on the following repos and blogs-

1. https://github.com/yenchenlin/DeepLearningFlappyBird
2. https://github.com/jaara/AI-blog
3. http://karpathy.github.io/2016/05/31/rl/


# Python Files Explanation:

* play.py --> press SPACE to flap the bird
* test.py --> test one network model
* train_network.py --> train a network
