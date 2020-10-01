FROM tensorflow/tensorflow:2.3.0
RUN pip install spacy nltk langdetect seaborn pandas numpy python-dotenv keras scikit-learn
RUN mkdir /code
COPY ./dssg_disinfo /code/dssg_disinfo
COPY ./toy_dataset_new.csv.enc /code/toy_dataset_new.csv.enc
ENV PYTHONPATH "/code"
ENV DATA_PATH "/data"
ENV CLEAN_DATA articles_v3.csv
ENV NEGATIVE_DATA negative_articles_v3.csv
ENV POSITIVE_DATA positive_articles_v3.csv
ENV ALL_FEATURES_DATA toy_dataset_new.csv
COPY ./docker-start.sh /docker-start.sh

CMD /docker-start.sh
