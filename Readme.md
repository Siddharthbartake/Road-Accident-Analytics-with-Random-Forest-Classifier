# Road Accident Analytics using 3 Different Machine Learning Algorithms
* Extracted Crash Incidents using an API call from NHTSA website (US Federal Government Site).
* Crash Data is available from 2010 upto 2022.
* No Personal Identifiers are listed in the entire dataset.
* API is called by iterating the parameters in formatted URL - Year, StateID, Gender, and Injury Severity Level.
* Injury Severity Level is the Dependent Variable(Predictor) and is described using the KABCO scale.
* 9 contributing attributes for an accident and are all Categorical.
* Classification Model is used for building a prediction model.

## Code and Resources Used
* **Python Version** : 3.11.4.
* **Packages :** pandas, sklearn, matplotlib, seaboard, json, defaultdict.
* **API and Data Source:** https://crashviewer.nhtsa.dot.gov/CrashAPI.
* **Machine Learning Algorithms :** Ordinal Logistic Regressor, Naïve Bayes, Random Forest Classifier.
