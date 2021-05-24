FROM centos:latest
RUN yum install python3  python3-devel   gcc-c++ -y && \
    python3 -m pip install --upgrade --force-reinstall pip && \
    yum install sudo -y && \
    yum install --assumeyes  python3-pip && \
    pip install keras && \
    pip install tensorflow --no-cache-dir  tensorflow && \
    pip install --upgrade pip tensorflow && \
    pip3 install flask && \
    pip3 install joblib && \
    pip3 install sklearn && \
    mkdir  /heart_app &&  \
    mkdir /heart_app/templates
COPY  heartdisease_predicting_model.h5    /heart_app
COPY  app.py  /heart_app
COPY  templates/  /heart_app/templates
EXPOSE  1234
WORKDIR  /heart_app
CMD export FLASK_APP=app.py
ENTRYPOINT flask  run --host=0.0.0.0    --port=1234