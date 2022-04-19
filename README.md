# Find and download GTU BE exam papers
This repository contains a python script which can be used to download BE GTU exam papers.
To use this script first install the required python modules by typing following in the terminal.
```
pip install -r requirements.txt
```

Usage:
```
Download BE papers from https://www.gtu.ac.in/uploads/[term]/BE/[SubCode].pdf  
Options:
-d              Download and save file(s) after fetching
-v              Show verbose output
-l N            Last year to check untill(Default is 4 years from current year)
                    (e.g: '-l 2019' would check from current year to 2019)     
-h|--help       Show this help message
Example: '.\FindAndDownloadPapers.py -dvl 2019' would download all the papers from current year to 2019.
```


NOTE: By default the script will just find and save the valid urls of the found papers in __validUrls.txt__. To download the papers use the -d option.

Example:
Let's say you want to download all the papers of subject code __3150713__ from current year till 2019. You can use the following command.
```
.\FindAndDownloadPapers.py -dvl 2019
```
You will be asked to enter the subject code. Enter the code and press enter.
Output:
```
./FindAndDownloadPapers.py -vdl 2019
Enter subject codes separeted with commas: 3150713
Following valid Subject Codes found:
3150713
-------------Fetching URLs-----------
Got 404 for https://www.gtu.ac.in/uploads/S2022/BE/3150713.pdf
Got 404 for https://www.gtu.ac.in/uploads/W2022/BE/3150713.pdf
https://www.gtu.ac.in/uploads/S2021/BE/3150713.pdf will be downloaded!
https://www.gtu.ac.in/uploads/W2021/BE/3150713.pdf will be downloaded!
Got 404 for https://www.gtu.ac.in/uploads/S2020/BE/3150713.pdf
https://www.gtu.ac.in/uploads/W2020/BE/3150713.pdf will be downloaded!
Got 404 for https://www.gtu.ac.in/uploads/S2019/BE/3150713.pdf
Got 404 for https://www.gtu.ac.in/uploads/W2019/BE/3150713.pdf
-------------Downloading-------------
[*]Downloding https://www.gtu.ac.in/uploads/S2021/BE/3150713.pdf, and will be saved as S2021_3150713.pdf
[+]Downloaded https://www.gtu.ac.in/uploads/S2021/BE/3150713.pdf to S2021_3150713.pdf
[*]Downloding https://www.gtu.ac.in/uploads/W2021/BE/3150713.pdf, and will be saved as W2021_3150713.pdf
[+]Downloaded https://www.gtu.ac.in/uploads/W2021/BE/3150713.pdf to W2021_3150713.pdf
[*]Downloding https://www.gtu.ac.in/uploads/W2020/BE/3150713.pdf, and will be saved as W2020_3150713.pdf
[+]Downloaded https://www.gtu.ac.in/uploads/W2020/BE/3150713.pdf to W2020_3150713.pdf
NOTE: File Urls are saved in ValidUrls.txt
```

___TIP: You can give multiple subject codes separated by commas to download multiple subject papers.___

Like this:
``` 
Enter subject codes separeted with commas: 3150713,3150711,3150710,3150703,3150714
```
