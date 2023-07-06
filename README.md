Upwork task:

Ask for file location. read excel file. 
add column AA named Font. 
add column AB named Letter 1. 
add column AC named Text 1. 
add column AD named Text 2. 
add column AE named Text 3. 
add column AF named Text 4. 
add column AG named Color. 
IF order number is greater than 1000000000 do the following search item name for "Color/Finish" and extract the next word and copy to Color Column. 
IF order number is greater than 1000000000 do the following search item name for "Personalization" and extract all of the text following it to the Text 1 Column. 
iF order number is greater than 1000000000 do the following search SKU if ends in "-02" font column equals "Cambria". this is a numerical column 
iF order number is less than 1000000000 do the following search Item Name for "Color:" and extract the next word and copy to Color column. 
iF order number is less than 1000000000 do the following search Item Name for "Name: (Please limit to one word)" and extract text until "Choose" and copy to Text 1 column. 
iF order number is less than 1000000000 do the following search Item Name for "Custom Text:" and extract text until "Choose" and copy to Text 1 Column. 
iF order number is less than 1000000000 do the following search Item Name for "Choose your Font:" and extract the word after and copy to Font Column. 
iF order number is less than 1000000000 do the following search Item Name for "Customer Note:" and extract text until "_customily" and copy to Customer Comments Column. 
iF order number is less than 1000000000 do the following search Item Name for "Letter:" and extract the next letter and copy to Letter 1 Column, if "Letter:" is not found skip. 
iF order number is less than 1000000000 do the following search Item Name for "(Top):" and extract text until "Choose" and copy to Text 1 Column, if "(Top):" is not found skip. 
iF order number is less than 1000000000 do the following search Item Name for "(Center):" and extract text until "Choose" and copy to Text 2 Column, if "(Center):" is not found skip. 
iF order number is less than 1000000000 do the following search Item Name for "(Bottom):" and extract text until "Choose" and copy to Text 3 Column, if "(Bottom):" is not found skip. 
