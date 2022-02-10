echo . > "C:\sent\cisco_cable_diagnostic\cisco_cable_diagnostic_log-%date:~0,2%-%date:~3,2%-%date:~6,4%.txt"
py C:\\py\asw_tdr_cable_int.py > C:\sent\cisco_cable_diagnostic\cisco_cable_diagnostic_log-%date:~0,2%-%date:~3,2%-%date:~6,4%.txt
py C:\\py\mail_sender.py

