$a = $args[0]

foreach ($i in $a) {
    if ($a -eq "backup") {
        docker exec imagerepo-db-1 /usr/bin/mysqldump -u root --password=root imagerepo > backup.sql
        Write-Host "The database has been stored in backup.sql"
    } elseif ($a -eq "restore") {
        Get-Content backup.sql | docker exec -i imagerepo-db-1 /usr/bin/mysql -u root --password=root imagerepo
        Write-Host "The database has been restored from backup.sql"
    }
}