$ErrorActionPreference = 'SilentlyContinue'
$env:PSStyle.Output = 'None'

Write-Host '=== C: drive ==='
Get-PSDrive C | Select-Object Used,Free | Format-Table | Out-String | Write-Host

Write-Host ''
Write-Host '=== Top 20 dirs in C:\Users\denni (size in GB) ==='
Get-ChildItem 'C:\Users\denni' -Directory | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse -File | Measure-Object Length -Sum).Sum
    [PSCustomObject]@{Name=$_.Name; SizeGB=[math]::Round($size/1GB,2)}
} | Sort-Object SizeGB -Descending | Select-Object -First 20 | Format-Table | Out-String | Write-Host

Write-Host ''
Write-Host '=== AppData\Local > 500MB ==='
Get-ChildItem 'C:\Users\denni\AppData\Local' -Directory | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse -File | Measure-Object Length -Sum).Sum
    if ($size -gt 500MB) {
        [PSCustomObject]@{Name=$_.Name; SizeGB=[math]::Round($size/1GB,2)}
    }
} | Sort-Object SizeGB -Descending | Select-Object -First 20 | Format-Table | Out-String | Write-Host

Write-Host ''
Write-Host '=== Temp size ==='
$tmp = 'C:\Users\denni\AppData\Local\Temp'
$s = (Get-ChildItem $tmp -Recurse -File | Measure-Object Length -Sum).Sum
'Temp: {0:N2} GB ({1:N0} files)' -f ($s/1GB), (Get-ChildItem $tmp -Recurse -File | Measure-Object).Count | Write-Host

Write-Host ''
Write-Host '=== Windows\Temp ==='
$wt = 'C:\Windows\Temp'
$s2 = (Get-ChildItem $wt -Recurse -File | Measure-Object Length -Sum).Sum
'Windows\Temp: {0:N2} GB ({1:N0} files)' -f ($s2/1GB), (Get-ChildItem $wt -Recurse -File | Measure-Object).Count | Write-Host