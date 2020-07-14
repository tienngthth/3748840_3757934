from crontab import CronTab
    
cron = CronTab(user='pi')
cron.remove_all()

job  = cron.new(command='/home/pi/Sensors_Database/04_timesense.py')

job.second.every(10)
cron.write()
