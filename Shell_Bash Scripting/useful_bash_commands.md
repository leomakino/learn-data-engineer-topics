## Manipulating Files

### Count number of files
ls /home/user/folder/file_name_2023* | wc -l

### Split csv keeping extension
split -l 20000 -d --additional-suffix=.csv file_being_split.csv filename_

### Concat - link n files together
cat /home/user/folder/file_name_2023* > /home/user/folder/file_name_2023.csv.gz

### Extract tar
tar -xf /home/user/folder/file_name_2023*

### From tar to gz
tar -ixvf /home/user/folder/file_name_2023* && cat /home/user/folder/tar_folder/file_name_2023* > cat /home/user/folder/file_name_2023.csv.gz

### Replacing text in a file
sed -i "s/\"Double quote to simple quote replace/'Double quote to simple quote replace/g"

### select lines according to a text and saves it into a file (-E interpret patterns as Regex; | means or)
grep -E "2020-01|2020-02" > file_2020_Jan_Feb.csv


## Gsutil

### Upload from directory to Cloud Storage
gsutil cp /home/user/folder/file_name_2023.csv.gz gs://bucket_name

### Download from Cloud Storage
gsutil cp gs://bucket_name/file_name_2023.csv.gz /home/user/folder

### Multiples commands example
gsutil cp cp gs://bucket_name/file_name_2023* /home/user/folder \
&& tar -ixvf /home/user/folder/file_name_2023* \
&& ls /home/user/folder/tar_file/file_name_2023* | wc -l \
&& cat /home/user/folder/tar_file/file_name_2023* > /home/user/folder/upload_folder/file_name_2023.csv.gz \
&& rm -r /home/user/folder/tar_file/ \
&& gsutil cp /home/user/folder/upload_folder/file_name_2023.csv.gz gs://bucket_name/

### Loop through blobs to get date
for str in $(gsutil ls gs://bucket_name/folder/files_*.csv)
do
echo "$(echo $str | grep -E -o '[0-9]+[0-9]+[0-9]'), date of the csv"

## Directories
### Copy
cp /home/user/folder/file_name_2023* /home/user/folder_2


### Delete directory
rm -r /home/user/folder_2