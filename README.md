# Google Playstore

Il DataSet utilizzato può essere consultato e/o scaricato al seguente link
https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps

# Linux
Per l'utilizzo sul sistema operativo Linux, effettuare i seguenti passi, una volta scaricato il DataSet:
  ## 1. Installazione di Python
  ```
    $ sudo apt-get update
    $ sudo apt-get install python.
  ```
  ## 2. Installazione di Spark
  ```
    $ sudo apt install default-jre pip
    $ pip install pyspark
    $ source ~/.profile
  ```
  ## 3. Installazione di Inquirer
  ```
    $ pip install inquirer
  ```

## Cloud

1. **Creazione del Cluster**
   
Nella console di Cloud:
```
$ gcloud dataproc clusters create example-cluster --region europe-west6 --master-boot-disk-size 50GB --worker-boot-disk-size 50GB --enable-component-gateway
```
2. **Creazione Bucket** 
   - Navigation menu () > Cloud Storage > Buckets.
   - Click CREATE.
   - Inserire le informazione del bucket information and CONTINUE
   - Click CREATE
   - Caricare i file che si intende eseguire nel Bucket
    
3. **Inviare il progetto di Spark dal Cloud Shell**
   ```
   BUCKET=gs://<YOUR_BUCKET_NAME>
   gcloud dataproc jobs submit pyspark --cluster example-cluster --region=europe-west6 $BUCKET/file.py
