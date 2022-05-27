# Book Recommendation System API #
## 1. Introduction 
This repository consists of a recommendation engine which predicts and returns the most similar books on the basis of the user's history.

## 2. Dataset

* For the dataset, I searched about the [Project Gutenberg](https://www.gutenberg.org/) which is a library of over 60,000 free eBooks. It's mission is: To encourage the creation and distribution of eBooks.

* To access the free eBooks, the site has an option for offline catalogs.

- ![image](https://i.imgur.com/myS0pkH.png)

* In that section, there is an option 6., i.e., for The Project Gutenberg Catalog Metadata in Machine-Readable Format.

- ![image](https://i.imgur.com/txZYGrx.png)

* On clicking that, a [link](https://www.gutenberg.org/ebooks/offline_catalogs.html#the-project-gutenberg-catalog-metadata-in-machine-readable-format) is provided for an excel-compatible CSV spreadsheet of eBook metadata. On accessing that, a pg_catalog.csv file is downloaded.

- ![image](https://i.imgur.com/WykVkAe.png)

* #### **Sanitization of data**- ####
In this, the books with incomplete data like that of author or the language are removed from the csv file.

* #### **book_id concept**- ####
For the ease of searching, the book elements are assigned an 'id' according to their serial numbers. 

## 3. Build

The **Recommendation System** is made using **[Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/en/2.1.x/)** and is based on the **[Cosine Similarity Algorithm](https://en.wikipedia.org/wiki/Cosine_similarity)**.

The **Prototyping** is done using the **[Google Colab](https://colab.research.google.com/?utm_source=scs-index)** platform. Here is a working example, **[Book_Recommendation](https://colab.research.google.com/drive/1vd0HCRFAOgezkd4IvcS1N7uIkk4gGQdE?usp=sharing)** for the same. 

## 4. Deployment

The server is also deployed on **[Heroku](https://www.heroku.com)** as **[Recommendation_Engine](https://glacial-hamlet-68829.herokuapp.com/)**. 