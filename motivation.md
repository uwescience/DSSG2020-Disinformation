---
layout: page
title: Motivation
---

**Background**

The production and consumption of news has changed dramatically over the past decade. Specifically, the move from predominantly print to predominantly electronic formats has heralded numerous new challenges. One such challenge is the proliferation of disinformation websites and the corresponding spread of unreliable, untrustworthy, or even purposefully incendiary or deceptive content. In the US and globally, this proliferation of online disinformation has eroded public trust in mainstream media, political actors, and even public health officials. 
 
The deleterious impact of disinformation is perhaps most consequential in regard to the ongoing coronavirus pandemic. Disinformation related to the coronavirus poses a broad threat to national and global public health, particularly if individuals  disregard the public health measures (e.g., socially-distancing, wearing a mask, etc.) necessary to mitigate the continued transmission of the virus. Further, this type of disinformation has also contributed to the direct loss of lives after self-administration of unproven medications promoted by online disinformation. 

Examples of coronavirus related disinformation narratives:

![Image of disinformation narratives](assets/img/coronavirus_map.png)
*Source: https://disinformationindex.org/wp-content/uploads/2020/07/GDI_Ad-funded-COVID-19-Disinformation-1.pdf*

Examples of possible harms of coronavirus related disinformation narratives:

![Image of possible harms](assets/img/coronavirus_table.png)
*Source: https://disinformationindex.org/wp-content/uploads/2020/07/GDI_Ad-funded-COVID-19-Disinformation-1.pdf*

Our partner organization, **The Global Disinformation Index (GDI)**, is already engaged in work to identify and defund disinformation on the internet. Their current focus involves identifying disinformation websites via a system of scoring the degree of disinformation risk at the domain-level.

To this end, GDI under the general guidance of the Technical Advisory Group[1], has developed and piloted an index that provides disinformation risk ratings for news sites in media markets across the globe. This risk rating is based on expert-identified disinformation ‘flags’ that can be combined to estimate accurate and unbiased risk assessment of a news domain. 

The actual process by which a site’s risk rating is determined consists of both automated and manual assessments. Evaluation of published content for credibility, sensationalism, hate speech and impartiality is done manually by an analyst with subject matter expertise. Artificial intelligence, developed from a sample of 20,000 known disinformation domains, is deployed in assessing domain metadata and computational signals. Furthermore, an independent review of the news site’s compliance with Journalism Trust Initiative (JTI) is used to assess domain’s trust and reliability. Lastly, the domain is assessed by an independent expert survey for reputational practices, reliability and trustworthiness. All four assessments are combined to assign the domain an aggregate rating based on a score of 0 to 100, where a lower score indicates a higher risk of disinformation. Importantly, this score does not establish that a site actually carries disinformation, but rather provides a risk assessment metric.
 
GDI index risk score is intended to help brands and ad tech firms have more transparent and trusted information about the news sites where they place ads, allowing them in principle to make more informed decisions about where ads are served, based on their own self-determined risk thresholds.

This DSSG project is focused on addressing online disinformation related to coronavirus. In collaboration with GDI, we will produce a machine learning model to accurately classify articles as disinformation or not. This work may be generalized to other substantive domains or to disinformation more broadly. Our goal is to add transparency to the process by which brands and advertisers fund disinformation. The existing tools used by advertisers, such as blocking websites based on the presence of certain keywords, is blunt. We want to build a tool that can inform the advertisers and brands to pull their ads from such sites. Our approach builds specificity and granularity that will not only improve precision of targeting disinformation sites but also add the protection of profitability for legitimate news which are currently being blocked based on keyword parameters. This will limit the profitability of disinformation websites.

 
**Questions**

1. What makes an article disinformation?

2. How do you automate classification of articles as genuine/disinformation? (we are looking at more than just articles, so maybe online news content? 

3. What are the preprocessing steps needed to have a successful NLP machine learning model that will accurately predict disinformation classification of online news articles?

4. How can such a model be built to detect disinformation in a perpetually evolving landscape of disinformation narratives? 


**Stakeholders**

The project consists of direct stakeholders who are involved from the early stages of developing the models and indirect stakeholders who will be affected by the operation of the model or use it at later stages. The direct stakeholders of this project are:
 
* **Global Disinformation Index (GDI)**: GDI works with governments, businesses and civil society to defund and down-rank disinformation websites. They have built various classifiers to support detection of disinformation in news articles. GDI’s Maggie Engler (Lead Data Scientist) and Lucas Wright (Senior Researcher) are the project leads.
 
* **University of Washington eScience Institute**: This project is part of the Data Science for Social Good (DSSG) program hosted by the e-Science Institute at the University of Washington. The eScience Institute provides the administrative teams and data scientists (Noah Benson and Vaughn Iverson).
 
* **Data Science for Social Good Fellows**: This group of stakeholders consist of students from different universities who are working as interns. The fellows are working directly with project lead and data scientists to develop the model.

* **Ad exchange companies**: Ad exchange companies (e.g., Google) will be the primary users of the model to identify articles that have disinformation. (I thought this was a direct stakeholder)

Meanwhile, the indirect stakeholders of this project are:
 
* **Global Alliance for Responsible Media (GARM)**: GARM brings together advertisers, agencies, media companies, platforms and industry organizations to improve public safety. GDI will deliver the model to GARM to be shared with other stakeholders within GARM.
 
* **Data scientists and researchers**: The model will be open source and it will be available on GitHub for other data scientists and researchers to access it and use it in their research projects.


**Ethics**

The following ethical concerns are the most important for the project:

There is a possibility that the model might automatically label a “genuine” article as “disinformation” because it covered a topic which is about disinformation. In such a situation, the model might harm the reputation of the authors, publishers, or website associated with that article.

At the heart of this problem lies the difficulty of measuring the extent of disinformation in a given article. Are there half-truths present? And does the article mostly contain factual information save for a couple of sentences? Any tool built to automatically classify articles as disinformation then needs to make a trade-off between truthful and disinformation content. 
 
Due to the open-source nature of this project, it is possible that groups invested in the creation and propagation of digital disinformation may utilize our code and documentation in order to produce content which would escape detection in our final model.

Publicly labelling an article as “disinformation” must be supported by substantial evidence and rigorous protocols which might be lacking in some of the machine learning models that the team decides to use. The model will also be limited by the nuances of the training data.

We will be undertaking the following steps to address the ethical questions:

* Detailed process documentation
* Laying out the assumptions
* Sharing the metrics/ criterion used
* Building model alternatives and performing cross-model-validation


---

[1] Index members include  Camille François (Graphika) and Dr. Scott Hale (Meedan/Oxford Internet Institute), Olaf Steenfadt (Reporters without Borders/Journalism Trust Inititiave), and Cristina Tardáguila (International Fact Checking Network/Poynter),
