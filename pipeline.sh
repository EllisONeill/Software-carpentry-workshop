echo cleanup
rm *.txt
rm *.tmp
rm *.csv

echo download data
curl https://github.com/zonca/swcarpentry-workshop-pandas/blob/master/rawdata/rawdata.zip?raw=true -o rawdata.zip -L

echo unpack data
unzip rawdata.zip
rm rawdata.zip

rm *.tmp

echo rename txt
for f in *.txt
do
mv $f ${f/txt/csv}
done

echo ~
echo ~
echo Available .csv files:
ls *.csv
echo ~
echo ~

for f in *data.csv
do
~/anaconda/bin/ipython analyze_mosquito_data_script.py $f
done

mv *png figures/
mv *parameters.csv parameters/
 