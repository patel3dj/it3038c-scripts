function getIP {
 (Get-NetIPaddress).IPv4address | select-string "192*" 
}
$IP = getIP
write-host("This machine's IP is $IP")
write-host("this machine's IP is {0}" -f $IP)

