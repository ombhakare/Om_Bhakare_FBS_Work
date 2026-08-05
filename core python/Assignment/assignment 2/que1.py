#Q1.Convert the time entered in hh,min and sec into seconds.??

hours = int(input('enter the hours: '))
min =  int(input('enter the minutes: '))
sec =  int(input('enter the seconds: '))

#converts hours into seconds
hours_sec = hours * 3600

#converts minutes into seconds 
min_sec = min * 60

#converts seconds into seconds
total_sec = hours_sec + min_sec + sec

#output
print(f'the total second is: {total_sec}')
