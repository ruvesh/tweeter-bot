import gspread

gc = gspread.service_account('./auth/gcredentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("tweet sheet").sheet1

# Fetch the tweet on the 2nd row of 1st column 
tweet = wks.acell('A2').value

print(tweet)