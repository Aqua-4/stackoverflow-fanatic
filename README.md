# stackoverflow-fanatic
Requirement: Visit the site(stackoverflow) each day for 100 consecutive days. (Days are counted in UTC.)

* Crontab script - runs the script twice daily and dumps the output to a file
 0 */12 * * *  cd /home/pi/stackoverflow-fanatic/ && DISPLAY=:0 python3 run_me.py >> output_count
