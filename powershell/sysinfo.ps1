function getIP {
 (Get-NetIPaddress).IPv4address | select-string "192*" 
}
function getDATE {
Get-Date
}

$IP = getIP
$USER = $env:USERNAME
$HOSTT = hostname
$PSVERSION= $PSversionTable
$DATE = getDATE

$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HOSTT. Powershell version is $PSVERSION. Today's Date is $DATE."


Send-MailMessage -To "botheaj@ucmail.uc.edu" -From "dhruvj2424@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 