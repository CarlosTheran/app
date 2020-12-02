# APP
This repositori contains an user interface that connect users from an app to the cloud platform.
In order to built the structure of the project follow these steps;
1. Create a folder name app_cawt.
2. Clone this repositori inside the folder app_cawt.
3. run the command ```python -m flask run ``` into the folder app_cawt.

IMPORTANT: remember to install all the dependencies [requerements](https://github.com/CarlosTheran/app/blob/main/requirements.txt) to be able to run the code web service.

# CAWT WEB SERVICES
```
   1. Create new folder HDFS
      This service require the enter path where you will create the new folder. e.g. /user/new_folder.   
```
```
   2. Delete a existing folder into HDFS 
      This service require the enter path where you will delete the folder folder. e.g. /user/folder_2_delete.
```
```
   3. Upload your data to our HDFS
      This service require the enter path from and where you will upload your data. e.g. Local folder=/home/ubuntu/data_covid/csv_covi19  and HDFS folder=/user/folder_2_uploadFile. 
```
```
   4. Download your data from HDFS into a local folder
      This service require the enter path where you will create the new folder. e.g. Local folder=/home/ubuntu/folder and HDFS folder=/user/folder_2_downloadFile/file_name. 
```
```
   5. Run Elemnet and Irnet achitecture for chemical analysis
      This service require only press the botton Execute <architecture>, for future implementation a path where the code belong will be requier.
```