$n = $args[0]

foreach ($i in $n) {
    if ($n -eq "backup") {
        docker exec b07479c3bb6e /usr/bin/mysqldump -u root --password=root imagerepo > backup.sql
        Write-Host "The database has been stored in backup.sql"
    } elseif ($n -eq "restore") {
        Get-Content backup.sql | docker exec -i b07479c3bb6e /usr/bin/mysql -u root --password=root imagerepo
        Write-Host "The database has been restored from backup.sql"
    }
}