# OOP - 2023/24 - Assignment 1

This is the base repository for assignment 1.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/2023_24_OOP.pdf) for the content of the exercise.

## How to carry out your assignment

1. Clone this template into a private repository.
2. Please add your partner and `oop-otoz` to the collaborators.
3. Create a new branch called `submission`.
4. Create your code in the `main` branch.
5. Once you are done with the assignment (or earlier), create a pull request from the `main` branch to your `submission` branch and add `oop-otoz` to the reviewers.

The assignment is divided into 4 blocks.
Block 1, 2, and 3 all define different classes.

Put the three classes in three separate files in the `src` folder, with the names specified in the PDF.
**Leave the __init__.py file untouched**.

Put the **main.py** script **outside** of the `src` folder, in the root of this repo.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the branch you were working on to the `submission` branch.

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 main.py`. If your code does not throw any errors, it will be marked as reproducible.
3. Style - runs `flake8` on your code to ensure adherence to style guides.

---

## Your report

In general, we set all the attributes and methods of the classes private that the users should not use and see.
We consider using setters and getters to access and change the values of the attributes cleaner and safer in the sense
that setting an attribute or method private indicates that it is "hidden" from the outside and reduces the chances of
unintended interference. Overall, private attributes and methods hide internal details and helps in managing the
complexity thus encouraging encapsulation and abstraction.

# class MultipleLinearRegression:

## Constructor:
The first method in the MultipleLinearRegression class is the constructor. We implemented the constructor to be a
"default constructor" which dos not take any parameters/arguments and does not return anything (returns None). The
class has one attribute, coefficients, which we decided to make private and the only way to get/set/change the coefficients
is by using the getter and setter functions. This is because we do not want the user to be able to access and possibly change the
coefficients by chance.

## Getter and setter method of coefficients:
The get_coefficients() method returns a np.ndarray which contains the coefficients of the model and the
set_coefficients() method takes a np.ndarray which contains the coefficients the user wants to set for the model and it
does not return anything. These two functions are necessary as coefficients is a private attribute and to be able to
access and change the values from different classes we need these helper functions. Because of the same reason we
decided to make the getter and setter public.

## Train:
The train() method takes 2 np.ndarrays, X_train and y_train, and it does not return anything. We decided to keep this
method public, as it is something we wanted to be able to access/call from different classes and the user will need to
use this method to train a multiple linear regression model.

## Predict:
The predict method takes one np.ndarray, X_test, and returns another np.ndarray, y_pred, which contains the predicted
target values. Similarly to the train() method, this method is also public and we made this design choice after
considering that we want the user to be able to use it to make predictions based on their trained model.


# class RegressionPlotter:

## Constructor:
The constructor of the plotter takes one argument, model, which can be any machine learning model and does not return
anything (returns None). The class has one attribute, model, which we decided to set private. The explanation for that
is that the user should not be able to directly access model and make changes to it.

## Getter for model:
As the model attribute of the class is private, we created a getter in order to be able to access the model from
different classes. The getter does not take arguments and returns the model.

## Plotting methods:

The method plot_model takes 2 np.ndarrays as arguments (X_test, y_test) and also a string, plot_type and returns
nothing. This is the only plotting method that we decided to set public, so the users can access and call this method
and this method will call one of the other 3 plotting methods based on the input of the user without the user having to
think about how the plotting has to be done for the specific number of features they provided.

The methods plot_regression, plot_3D_regression and plot_generic are all private methods, as the users do not have to
be abel to use these, they will interact with the plot_model method as mentioned above and the plot_model method will
call the adequate method out of the 3 private methods. These methods do not return anything (they print the plots) and
they take as arguments 2 np.ndarrays. 

# class ModelSaver:

## Constructor:
The model saver does not have any attributes thus the constructor is an empty constructor, where we do not have to
initialize any values and the constructor does not return anything.

## Save and load model:

The method save_model() takes a model as an argument and 2 string values, format_type and filename. The method does not
return anything but rather saves a model specified by the user as either json or csv file under a certain file name.
The method load_model() takes 2 strings, format_type and filename and returns a np.ndarray with the
weights of the model. These two methods we decided to set public, as these methods are the ones which the user has to be
able to use and access in order to save and load their models. The load and save methods call the private load and 
save methods specific for the format_type.

The methods save_csv, save_json, load_csv, load_json we decided to set to private. As previously mentioned, the users
will be using the save_model and load_model methods that will call the private method that is appropriate based on the
argument given by the user. Because of this reason the specific save and load methods can be set private and by this we
make the interaction for the user more clear and simple (by adding a level of abstraction).

# Main:

In the main file we implemented some functions to make the demonstration of the functionality cleaner.

Overall we create and train 4 models, two of which have 1 feature and one model with 2 and one model with 4 features
using the create_dataset() function.

To showcase the functionality of the multiple linear regression we use the two
models with 1 feature and the functions test_regression_model and compare_model_coefficients. One of these models is
created by using our MultipleLinearRegression and the other one by using the LinearRegression by sklearn to make a
comparison of the output possible.

To test the plotter, we use models with different numbers of features, the methods test_regression_plotter,
test_regression_plotter_generic and showcase the functionality of all 3 of the private plotting functions (2D, 3D,
generic/sequence of 2D plots).

To demonstrate the functionality of the saver class, we use the test_model_saver method and call it once with a json
format and then with csv format.

