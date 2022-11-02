# Programming Assignment 3: Fortune Cookie Classifier


## Assignment Outline
You will build a binary fortune cookie classifier. This classifier will be used to classify fortune cookie messages into two classes
- Messages that predict what will happen in the future (class 1)
    - Example: "You will go far in your endeavours"
- Messages that just contain a wise saying (class 0)
    - Example: "Never go in against a Sicilian when death is on the line"

### Provided Files
There are three sets of files. All words in these files are lower case and punctuation has been removed
1) The training data:
    - `traindata.txt`: This is the training data consisting of fortune cookie messages
    - `trainlabels.txt`: This file contains the class labels for the training data
2) The testing data:
    - `testdata.txt`: Contains testing data consisting of fortune cookie messages.
    - `testlabels.txt`: Contains the class lables for testing data
3) A list of stop words: `stoplist.txt`

### Instructions
There are two steps: The pre-processing step and the classification step. 

In the pre-processing step, you will convert fortune cookie messages into features to be used by your classifier. You will be using a bag of words representation. The following steps outline the process involved
- **Form the vocabulary**. The vocabulary consists of the set of all the words that are in the training data with stop words removed (stop words are common, uninformative words such as "a" and "the" that are listed in `stoplist.txt`). The vocabulary will now be the features of your training data. Keep the vocabulary in alphabetical order to help with debugging
- **Convert the training data into a set of features**: 
    - Let $M$ be the size of your vocabulary. For each messages, you will convert it into a feature vector of size $M$. Each slot in that vector takes the value of 0 or 1.
    -  For these $M$ slots, if the $i^{\text{th}}$ slot is 1, it means that the $i^{\text{th}}$ word in the vocabulary is present in the messages
    -  Otherwise, if it's 0, then the $i^{\text{th}}$ word is not present in the message. 
    - Most of these slots will be 0. Since you are keeping the vocabulary in alphabetical order, the first feature will be the first word alphabetically in the vocabulary
- Implement a binary classifier with perceptron weight update as shown below. Use learning rate $\eta = 1$

#### Algorithm 1 Online Binary-Classifier Learning Algorithm
***
**Input:** $D =$ training examples, $T = $ maximum number of training iterations  
**Output:** $w$, the final weight vector
***

1. Initialize the weights $w = 0$
2. **for** each training iteration $\text{itr} \in \{1, 2, \dots, T\}$ **do**
3. **for** each training example $(x_t, y_t) \in D$ **do**
4. $\hat{y}_t = \text{sign}(w * x_t)$ predict using current weights
5. **if** mistake **then**
6. $w = w + \eta * y_t * x_t$ update the weights
7. **end if**
8. **end for**
9. **end for**
10. **return** final weight vector $w$
***

**a)** Compute the number of mistakes during each iteration (1 to 20)  
**b)** Compute the training accuracy and testing accuracy after each iteration (1 to 20)  
**c)** Compute the training accuracy and testing accuracy after 20 iterations withy standard perceptron and averaged perceptron

#### Algorithm 2 Online Multi-Class Classifier Learning Algorithm
***
**Input**: $D =$ Training examples, $k =$ number of classes, $T =$ max number of training iterations  
**Output**: $w_1, w_2, \dots, w_k$ the final weight vectors for $k$ classes
***
1. Initialize the weights $w_1, w_2, \dots, w_k = 0$  
2. **for** each training iteration $\text{itr} \in \{1, 2, \dots, T\}$
3. **for** each training example $(x_t, y_t) \in D$ **do**
4. $\hat{y}_t = \text{arg max}_{y \in \{1, 2, \dots, k\}} w_y * x_t$ predict using current weights
5. **if** mistake **then**
6. $w_{yt} = w_{yt} + \eta * x_t$ update weights
7. $w_{\hat{y} t} = w_{\hat{y}t} - \eta * x_t$ update weights
8. **end if**
9. **end for**
10. **end for**
11. **return** final weight vectors $w_1, w_2, \dots, w_k$
***

#### Task
You will build an optical character recognition (OCR) classifier: given an image of a handwritten character, we need to predict the corresponding letter. You are provided with a training and testing set

#### Data format
Each non-empty line corresponds to one input-output pair. 128 binary values after "im" correspond to the input features (pixel values of a binary image). The letter immediately afterwards is the corresponding output label.

**a)** Compute the number of mistakes made during each iteration (1 to 20)  
**b)** Compute the training accuracy and testing accuracy after each iteration (1 to 20)  
**c)** Compute the training accuracy and testing accuracy after 20 iterations with standard perceptron and average perceptron

### Output Format
The output of your program should be dumped in a file called `output.txt` in the following format. One block for binary classifier and another similar block for the multi-class classifer
```
iteration-1 num-of-mistakes
...
...
iteration-20 num-of-mistakes

iteration-1 training-accuracy, testing-accuracy
...
...
iteration-20 training-accuracy, testing-accuracy

standard-perceptron-training-accuracy, averaged-perceptron-testing-accuracy
```
