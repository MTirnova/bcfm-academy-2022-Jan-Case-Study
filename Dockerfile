FROM python:alpine
COPY . /Mustafa_TIRNOVA_Bcfm_Academy_Case_Study
WORKDIR /Mustafa_TIRNOVA_Bcfm_Academy_Case_Study
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py