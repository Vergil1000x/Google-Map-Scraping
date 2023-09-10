# Google-Map-Scraping
Pretty easy to use... for me atleast, lol.

Well it's free and easy(really)

Just basic python knowledge required, unless you understand the below instructions!


### How to use-

Open map.py

Edit the following lines-

+ Edit the line with location where your chromedriver.exe is
```python
   service = Service(
        r"C:\Users\Vergil1000\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
   )
```



+ Edit this linw with the file path of the excel sheet you want the data to be stored in
```python
   file_path = r"C:\Users\Vergil1000\Downloads\AesCliMal.xlsx"
```
   

+ Edit the link with the link you need like this, for example if you need to scrape restraunts in Tokyo, Japan, the given code needs to be changed
```python
    driver.get(
        f"https://www.google.com/maps/search/restaurants+near+New+York,+NY,+USA/@{x},{y},14z/data=!3m1!4b1?entry=ttu"
    )
```
For that the google map website link would be - https://www.google.com/maps/search/restaurants+in+Tokyo,+Japan/@35.6623336,139.6905891,13z/data=!3m1!4b1?entry=ttu
So the above lines of code becomes -
```python
    driver.get(
        f"https://www.google.com/maps/search/restaurants+in+Tokyo,+Japan/@{x},{y},14z/data=!3m1!4b1?entry=ttu"
    )
```


+ Edit the link with the link you need like this, for example if you need to scrape restraunts in Tokyo, Japan
```python
    divx = driver.find_element(
        "xpath", "//div[@aria-label='Results for Aesthetic Clinic in kuala lumpur']"
    )
```
For that the the google map website link would be - https://www.google.com/maps/search/restaurants+in+Tokyo,+Japan/@35.6623336,139.6905891,13z/data=!3m1!4b1?entry=ttu
So the above line becomes driver.get code becomes -
```python
    divx = driver.find_element(
        "xpath", "//div[@aria-label='Results for restaurants in Tokyo, Japan']"
    )
```


+ Next you need to edit the x and y
x and y is latitude and longitude
```python
    x = 3.056058
    while x < 3.218067:
       y = 101.647851
       while y < 101.748686:
          y += 0.1
          lol(x, y)
       x += 0.1
```
Suppose you want to scrape the whole Tokyo, then open google maps and search tokyo

![image](https://github.com/Vergil1000x/Google-Map-Scraping/blob/main/Screenshot%202023-09-10%20182521.png)
![image](https://github.com/Vergil1000x/Google-Map-Scraping/blob/main/Screenshot%202023-09-10%20182921.png)

From the image we took two points for which x=(35.547053,35.909462) and y=(138.945085,139.866140)
So change in code will be-
```python
    x = 35.547053
    while x < 35.909462:
       y = 138.945085
       while y < 139.866140:
          y += 0.1
          lol(x, y)
       x += 0.1
```

That's it for the changes in map.py

Run map.py using the following command in the termninal, open the terminal from the same folder

```
python map.py
```

Next open the excel and remove the duplicates

Next open whatlol.py

Edit the following lines-

+ Change the path with path in which you scraped and added the details map links using map.py  - Line 9
```python
    file_path = r"C:\Users\Vergil1000\Downloads\AesCliMal.xlsx"
```


+ Change the path with path of the excel file in which you want to store the details  - Line 27
```python
    file_path = r"C:\Users\Vergil1000\Downloads\testX.xlsx"
```


+ Change the path with path of chromedriver.exe - Line 27
```python
    service = services.Chromedriver(
        binary=r"C:\Users\Vergil1000\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    )
```


Run whatlol.py using the following command in the termninal, open the terminal from the same folder
python whatlol.py


And then you will have the list whatever you wanted to scrape


Hmm... I think I should make a video tut lol
