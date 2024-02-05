# Course Introduction
Artificial intelligence and machine learning represent an important evolution in information technologies that are quickly transforming a wide range of industries.

New tools and methodologies are needed to manage what’s being collected, analyze it for insights, and then act on those insights.

This course explores how organizations can use AI and ML to transform their business processes

## AI and ML funcdamentals
Generative AI is a type of artificial intelligence that can produce new content–including text, images, audio, and synthetic data. Generative AI can be used in a variety of applications, such as conversational bots, content generation, document synthesis, and product discovery.

Most data analysis and business intelligence is based on historical data, used to calculate metrics or identify trends. But to create value in your business, you need to use that data to make decisions for future business. AI and ML are the key to unlocking these capabilities.

ML provides a method to teach a computer how to solve problems by feeding it examples of the correct answers.

ML is suited to solve four common business problems:
- replacing or simplifying rule-based systems;
- automating processes;
- understanding unstructured data like images, videos, and audio;
- personalization.

Data is considered low quality if it’s not aligned to the problem or is biased in some way. If you feed an ML model low quality data, it's like teaching a child with incorrect information. An ML model can't make accurate predictions by learning from incorrect data.

To assess its quality, data is evaluated against 6 dimensions: 
- completeness: refers to whether all the required information is present; 
- uniqueness: Data should be unique; 
    - If a model is trained on a data set with a high number of duplicates, the ML model may not be able to learn accurately
- timeliness: refers to whether the data is up-to-date and reflects the current state of the phenomenon that is being modeled; 
- validity: ensures that data is in an acceptable range;
    - An example of invalid data is a date of 05-02-2024 when the standard format is defined as “YYYY/mm/dd.”
- accuracy: reflects the correctness of the data such as the correct birth date or the accurate number of units sold;
    - Whereas validity focuses on type, format and range, accuracy is focussed on form and content
- consistency: refers to whether the data is uniform and doesn’t contain any contradictory information.

Most of these problems can be solved simply by getting more high-quality data.

It’s critical that AI is used responsibly.

Google has established principles that guide Google AI applications:
- Be socially beneficial;
- Avoid creating or reinforcing unfair bias;
- Be built and tested for safety;
- Be accountable to people;
- Incorporate privacy design principles;
- Uphold high standards of scientific excellence;
- be made available for uses that accord with these principles.

Google will not design or deploy AI in the following application areas:
- technologies that cause or are likely to cause overall harm;
- weapons or other technologies whose principal purpose or implementation is to cause or directly facilitate injury to people;
- technologies that gather or use information for surveillance;
- violating internationally accepted norms;
- technologies whose purpose contravenes widely accepted principles of international law and human rights.


Explainable AI is Google Cloud’s set of tools and frameworks to help you understand and interpret predictions made by your machine learning models. These tools are natively integrated with several Google products and services to ensure transparent AI development.

## GC's AI and ML Solutions
Google Cloud offers four options for building machine learning models:
- BigQuery ML
    - It's a tool for using SQL queries to create and execute machine learning models in BigQuery
    - If you already have your data in BigQuery and your problems fit the predefined ML models, this could be your choice.
- pre-trained APIs
    - use machine learning models that were built and trained by Google
    - if you don’t have enough training data or sufficient machine learning expertise in-house.
- AutoML (Vertex AI);
    - is a no-code solution, letting you build your own machine learning models on Vertex AI through a point-and-click interface.
- custom training.
    - code your very own machine learning environment, the training, and the deployment, which gives you flexibility and provides control over the ML pipeline.


### BigQuery ML
Although BigQuery started solely as a data warehouse, over time it has evolved to provide additional features that support the data-to-AI lifecycle.
BigQuery ML democratizes the use of machine learning by empowering data analysts, the primary data warehouse users, to build and run models by using existing business intelligence tools and spreadsheets. 

Models are trained and accessed directly in BigQuery by using SQL, which is a language familiar to data analysts. It reduces complexity because fewer tools are required. It also increases speed to production, because moving and formatting large amounts of data for Python-based ML frameworks is not required for model training in BigQuery. BigQuery ML also integrates with Vertex AI, Google Cloud's end-to-end AI and ML platform.

### Pre-trained APIs
It is a great option if you don’t have your own training data. These are ideal in situations where an organization doesn’t have specialized data scientists, but it does have business analysts and developers. It is the fastest and lowest effort of the machine learning approaches, but is less customizable than the others. Provide access to ML models for common tasks like analyzing images, videos, and text.
 - Vision API: automatically detect faces, objects, text, and even sentiment in images.
 - Natural Language API: discovers syntax, entities, and sentiment in text, and classifies text into a predefined set of categories.
 - The Cloud Translation API: converts text from one language to another.
 - Speech-to-Text API: converts audio to text for data processing.
 - Text-to-Speech API: converts text into high-quality voice audio.
 - Video Intelligence API: recognizes motion and action in video.

Google has lots of images, text, and ML researchers to train its pre-trained models.


### AutoML
Vertex AI comes in it's necessary to train models by using your own data.

AutoML on Vertex AI lets you build and train machine learning models from end-to-end by using graphical user interfaces (GUIs), without writing a line of code. AutoML chooses the best machine learning model for you by comparing different models and tuning parameters. This lets machine learning practitioners focus on the problems that they are trying to solve, instead of the details of machine learning.

AutoML is a great option for businesses that want to produce a customized ML model but are not willing to spend too much time coding and experimenting with thousands of models.

AutoML Natural Language: 
- if your text examples don't fit neatly into the Natural Language API’s sentiment-based and you want to use your own specialized data instead.

### Custom models
Vertex AI is also for creating custom end-to-end machine learning models. This is the process that takes the longest and requires a specialized team of data scientists and engineers but it gives the business the most differentiation and innovative results.

### TensorFlow
All machine learning models are built on top of Google Cloud’s AI foundational infrastructure. A part of this foundation is TensorFlow, which is an end-to-end open source platform for machine learning.

TensorFlow has a flexible ecosystem of tools, libraries, and community resources that enable researchers to innovate in ML and developers to build and deploy ML powered applications.

### Other AI Solutions
- Contact Center AI: models for speaking with customers and assisting human agents, increasing operational efficiency and personalizing customer care to transform your contact center;
- Document AI: unlocks insights by extracting and classifying information from unstructured documents such as invoices, receipts, forms, letters, and reports.;
- Discovery AI for Retail: select the optimal ordering of products on a retailer's ecommerce site when shoppers choose a category;
- Cloud Talent Solution: job search and talent acquisition capabilities, matches candidates to ideal jobs faster, and allows employers to attract and convert higher quality candidates.

There are several decisions and tradeoffs to consider when selecting which AI/ML solutions to employ.
1. Speed: how quickly do you need to get your model to production?
1. Differentiation: how unique is your model, or how unique does it need to be?
1. **Effort** required to build: This depends on several factors, including the complexity of the problem, the amount of data available, and the experience of the team.
