Step 1 - First all columns containing 'date' in the end are transposed, keeping fix the columns ('Employee Code' , "manger Code', 'Date of Exit' 'Date of joining' . Asumption string 'date' used at variable end should not be changed.
step2 - End Date is calculate by first taking the lead of all dates by one and then subtracting it from 1 .
step3 - Base data with emplye code and the event happened between the start date and end date is tagged in a column.
step 4 - Taking all the compensation, event and engagement in a table by doing the transpose an d merging with the base data . will give us all the column populated.

Note: The code is designed in such a fashion the n number of event, compensation and engagement added, the output we will get in the same format.
